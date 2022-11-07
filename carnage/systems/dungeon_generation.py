import json
import logging
import re
from functools import lru_cache
from random import choice, randint
from typing import Any

import jinja2

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
    template = jinja2.Template(schema)
    rendered_template = template.render(jinja_arguments)
    return json.loads(
        re.sub(r'("(?:\\?.)*?")|,\s*([]}])', r"\1\2", rendered_template),
    )


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
