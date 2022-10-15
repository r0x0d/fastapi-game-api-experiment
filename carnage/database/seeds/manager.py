from carnage.database.seeds.aligment import AligmentSeed
from carnage.database.seeds.base import BaseSeed
from carnage.database.seeds.monster import MonsterSeed
from carnage.database.seeds.monster_type import MonsterTypeSeed
from carnage.database.seeds.size import SizeSeed

# WARNING: Do not change the order of this dictionary.
MAPPING_OF_SEEDS: dict[str, BaseSeed] = {
    AligmentSeed.name: AligmentSeed(),
    SizeSeed.name: SizeSeed(),
    MonsterTypeSeed.name: MonsterTypeSeed(),
    MonsterSeed.name: MonsterSeed(),
}


class SeedManager:
    def __init__(self) -> None:
        pass

    def seed(
        self,
        all_seeds: bool = True,
        seed_name: str | None = None,
    ) -> None:
        """ """
        if all_seeds:
            for _, seed in MAPPING_OF_SEEDS.items():
                seed.seed()
            return

        if seed_name not in MAPPING_OF_SEEDS:
            raise AssertionError("Couldn't find the desired seed.")

        seed = MAPPING_OF_SEEDS[seed_name]
        seed.seed()
