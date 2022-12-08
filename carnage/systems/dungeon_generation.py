import logging
from functools import lru_cache
from random import choice, randint
from typing import Any

import jinja2
import yaml

from carnage.database.models.monster.monster import MonsterModel
from carnage.database.repository.dungeon import DungeonSchemaRepository
from carnage.database.repository.monster import MonsterRepository

monster_repository = MonsterRepository()
dungeon_schema_repository = DungeonSchemaRepository()

logger = logging.getLogger(__name__)


@lru_cache
def _pick_random_monster(monsters: tuple[MonsterModel]) -> tuple[str, bool]:
    return choice(monsters)


def _render_jinja_template(
    schema: str,
    jinja_arguments: dict[str, Any],
) -> dict[str, Any]:
    template = jinja2.Template(schema, autoescape=True)
    rendered_template = template.render(jinja_arguments)
    # We were supposed to use json.loads, but we generate an invalid json, so
    # yaml it is!.
    return yaml.safe_load(rendered_template)


def generate_dungeon(
    dungeon_difficulty_id: str,
) -> dict[str, Any]:
    dungeon_schema = dungeon_schema_repository.select_by_dungeon_difficulty(
        dungeon_difficulty_id,
    )
    monsters = tuple(monster_repository.select())

    dungeon = _render_jinja_template(
        dungeon_schema[0].schema,
        jinja_arguments={
            "randint": randint,
            "monsters": monsters,
            "pick_random_monster": _pick_random_monster,
        },
    )
    return dungeon
