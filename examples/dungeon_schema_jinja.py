import pprint
from carnage.systems.dungeon_generation import generate_dungeon

from carnage.database.repository.dungeon import DungeonDifficultyRepository

dungeon_difficulty_repository = DungeonDifficultyRepository()

# pprint.pprint(
#     generate_dungeon(
#         dungeon_difficulty_id=dungeon_difficulty_repository.select_by_level(
#             level="Easy"
#         )[0].id
#     )
# )

# pprint.pprint(
#     generate_dungeon(
#         dungeon_difficulty_id=dungeon_difficulty_repository.select_by_level(
#             level="Medium"
#         )[0].id
#     )
# )

# pprint.pprint(
#     generate_dungeon(
#         dungeon_difficulty_id=dungeon_difficulty_repository.select_by_level(
#             level="Hard"
#         )[0].id
#     )
# )

dungeon = generate_dungeon(
    dungeon_difficulty_id=dungeon_difficulty_repository.select_by_level(
        level="Nightmare"
    )[0].id
)
