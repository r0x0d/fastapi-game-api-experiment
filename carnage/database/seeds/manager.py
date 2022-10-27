import logging

from carnage.database.seeds.account import AccountSeed
from carnage.database.seeds.aligment import AligmentSeed
from carnage.database.seeds.base import BaseSeed
from carnage.database.seeds.item import ItemSeed
from carnage.database.seeds.item_base_type import ItemBaseTypeSeed
from carnage.database.seeds.item_magical_type import ItemMagicalTypeSeed
from carnage.database.seeds.item_rarity import ItemRaritySeed
from carnage.database.seeds.monster import MonsterSeed
from carnage.database.seeds.monster_type import MonsterTypeSeed
from carnage.database.seeds.setting import SettingSeed
from carnage.database.seeds.size import SizeSeed
from carnage.database.seeds.spell import SpellSeed
from carnage.database.seeds.spell_duration_type import SpellDurationTypeSeed
from carnage.database.seeds.spell_range_type import SpellRangeTypeSeed
from carnage.database.seeds.spell_school import SpellSchoolSeed

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
