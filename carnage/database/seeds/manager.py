import logging

from carnage.database.seeds.account import AccountSeed
from carnage.database.seeds.aligment import AligmentSeed
from carnage.database.seeds.base import BaseSeed
from carnage.database.seeds.chat import ChannelChatSeed
from carnage.database.seeds.condition import ConditionSeed
from carnage.database.seeds.difficulty import DifficultySeed
from carnage.database.seeds.dungeon import (
    DungeonDifficultySeed,
    DungeonSchemaSeed,
    DungeonSeed,
)
from carnage.database.seeds.game_mode import GameModeSeed
from carnage.database.seeds.item import (
    ItemBaseTypeSeed,
    ItemMagicalTypeSeed,
    ItemRaritySeed,
    ItemSeed,
)
from carnage.database.seeds.monster import MonsterSeed, MonsterTypeSeed
from carnage.database.seeds.player import PlayerSeed
from carnage.database.seeds.race import RaceSeed
from carnage.database.seeds.size import SizeSeed
from carnage.database.seeds.spell import (
    SpellDurationTypeSeed,
    SpellRangeTypeSeed,
    SpellSchoolSeed,
    SpellSeed,
)
from carnage.database.seeds.vocation import VocationSeed, VocationSpellSeed

logger = logging.getLogger(__name__)


class SeedManager:
    def seed_mapping(self) -> dict[str, BaseSeed]:
        """Method that maps the current database seeds and their order.

        .. note::
            Do not change the order of the seeds as they have a specific
            dependency order to run.

        :return: A dictionary with the seed name as key and a seed class
            instance as value.
        """
        return {
            AccountSeed.name: AccountSeed(),
            AligmentSeed.name: AligmentSeed(),
            SizeSeed.name: SizeSeed(),
            MonsterTypeSeed.name: MonsterTypeSeed(),
            MonsterSeed.name: MonsterSeed(),
            SpellSchoolSeed.name: SpellSchoolSeed(),
            SpellRangeTypeSeed.name: SpellRangeTypeSeed(),
            SpellDurationTypeSeed.name: SpellDurationTypeSeed(),
            SpellSeed.name: SpellSeed(),
            ItemRaritySeed.name: ItemRaritySeed(),
            ItemBaseTypeSeed.name: ItemBaseTypeSeed(),
            ItemMagicalTypeSeed.name: ItemMagicalTypeSeed(),
            ItemSeed.name: ItemSeed(),
            RaceSeed.name: RaceSeed(),
            VocationSeed.name: VocationSeed(),
            VocationSpellSeed.name: VocationSpellSeed(),
            DungeonDifficultySeed.name: DungeonDifficultySeed(),
            DungeonSchemaSeed.name: DungeonSchemaSeed(),
            DungeonSeed.name: DungeonSeed(),
            PlayerSeed.name: PlayerSeed(),
            ChannelChatSeed.name: ChannelChatSeed(),
            ConditionSeed.name: ConditionSeed(),
            DifficultySeed.name: DifficultySeed(),
            GameModeSeed.name: GameModeSeed(),
        }

    def seed(
        self,
        all_seeds: bool = True,
        seed_name: str | None = None,
    ) -> None:
        """Method that seeds the database.

        This method can run only one seed or multiple if needed.

        .. note::
            If both `all_seeds` and `seed_name` are specified, then the program
            will crash and exit, as they cannot be used together.

        :param all_seeds: A boolean flag that indicates if all seeds needs to
            run.
        :param seed_name: A seed name to run only one seed,
        :raises AssertionError: If the `seed_name` passed to this method does
            not exist.
        """
        seeds_mapping = self.seed_mapping()
        if all_seeds:
            for _, seed in seeds_mapping.items():
                seed.seed()
        else:
            if seed_name not in seeds_mapping:
                raise AssertionError("Couldn't find the desired seed.")

            seed = seeds_mapping[seed_name]
            seed.seed()

        logger.info("Done with seeding.")
