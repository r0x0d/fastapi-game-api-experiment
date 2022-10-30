import logging

from carnage.database.seeds.account import AccountSeed
from carnage.database.seeds.aligment import AligmentSeed
from carnage.database.seeds.base import BaseSeed
from carnage.database.seeds.item import (
    ItemBaseTypeSeed,
    ItemMagicalTypeSeed,
    ItemRaritySeed,
    ItemSeed,
)
from carnage.database.seeds.map import (
    MapDifficultySeed,
    MapSchemaSeed,
    MapSeed,
)
from carnage.database.seeds.monster import MonsterSeed, MonsterTypeSeed
from carnage.database.seeds.player import PlayerSeed
from carnage.database.seeds.race import RaceSeed
from carnage.database.seeds.setting import SettingSeed
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
    @property
    def seed_mapping(self) -> dict[str, BaseSeed]:
        # WARNING: Do not change the order of this dictionary.
        return {
            SettingSeed.name: SettingSeed(),
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
            MapDifficultySeed.name: MapDifficultySeed(),
            MapSchemaSeed.name: MapSchemaSeed(),
            MapSeed.name: MapSeed(),
            PlayerSeed.name: PlayerSeed(),
        }

    def seed(
        self,
        all_seeds: bool = True,
        seed_name: str | None = None,
    ) -> None:
        """ """
        if all_seeds:
            for _, seed in self.seed_mapping.items():
                seed.seed()
        else:
            if seed_name not in self.seed_mapping:
                raise AssertionError("Couldn't find the desired seed.")

            seed = self.seed_mapping[seed_name]
            seed.seed()

        logger.info("Done with seeding.")
