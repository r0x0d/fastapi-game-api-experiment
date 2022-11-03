from unittest import mock

import pytest

from carnage.systems import dungeon_generation


def test_pick_random_monster():
    result = dungeon_generation._pick_random_monster(
        monsters=("monster_1", "monster_2"),
    )

    assert result


@pytest.mark.parametrize(
    ("schema", "jinja_arguments", "expected"),
    (
        (
            """\
{
    "test": "jinja",
    "replace": "{{ monster_id }}"
}
            """,
            {"monster_id": "cdb56c58-5ef1-11ed-a1b3-641c67e34d72"},
            {
                "test": "jinja",
                "replace": "cdb56c58-5ef1-11ed-a1b3-641c67e34d72",
            },
        ),
        (
            """\
{
    "test": "jinja",
    "replace": "{{ monster_id }}",
    "another_replace": "{{ replace }}"
}
            """,
            {
                "monster_id": "cdb56c58-5ef1-11ed-a1b3-641c67e34d72",
                "replace": "test",
            },
            {
                "test": "jinja",
                "replace": "cdb56c58-5ef1-11ed-a1b3-641c67e34d72",
                "another_replace": "test",
            },
        ),
        (
            """\
{% set monsters = ("cdb56c58-5ef1-11ed-a1b3-641c67e34d72",) %}
{
    "test": "jinja",
    "replace": "{{ monster_id }}",
    "another_replace": "{{ replace }}",
    "random_monster_id": "{{ _pick_random_monster(monsters) }}"
}
            """,
            {
                "monster_id": "cdb56c58-5ef1-11ed-a1b3-641c67e34d72",
                "replace": "test",
                "_pick_random_monster": dungeon_generation._pick_random_monster,  # noqa
            },
            {
                "test": "jinja",
                "replace": "cdb56c58-5ef1-11ed-a1b3-641c67e34d72",
                "another_replace": "test",
                "random_monster_id": "cdb56c58-5ef1-11ed-a1b3-641c67e34d72",
            },
        ),
    ),
)
def test_render_jinja_template(schema, jinja_arguments, expected):
    result = dungeon_generation._render_jinja_template(schema, jinja_arguments)
    assert result == expected


@mock.patch.object(dungeon_generation, "_render_jinja_template")
@mock.patch.object(dungeon_generation, "monster_repository")
@mock.patch.object(dungeon_generation, "dungeon_schema_repository")
def test_generate_dungeon(
    render_jinja_template_mock,
    monster_repository_mock,
    dungeon_schema_repository_mock,
    database_session_mock,
):
    dungeon = dungeon_generation.generate_dungeon("easy")
    assert dungeon
    assert render_jinja_template_mock.called_once
    assert monster_repository_mock.select.called_once
    assert dungeon_schema_repository_mock.select_by_dungeon_difficulty.called_with(  # noqa
        "easy",
    )
