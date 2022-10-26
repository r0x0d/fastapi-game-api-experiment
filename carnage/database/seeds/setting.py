from typing import Any, Type

from cryptography.fernet import Fernet

from carnage.constants import DEVELOPMENT
from carnage.database.repository.setting import SettingRepository
from carnage.database.seeds.base import BaseSeed


class SettingSeed(BaseSeed):
    name: str = "setting"
    data: list[dict[str, Any]] = [
        {
            "secret_key": Fernet.generate_key(),
            "environment": "production",
        },
    ]

    def validate_seed(self, seed: dict[str, str]) -> bool:
        print(
            f"Validating the current seed with environment: {seed['environment']}",  # noqa
        )

        result = self.repository.select_by_environment(  # type: ignore
            environment=seed["environment"],
        )
        if result:
            print("Seed already exists in the database")
            return True

        return False

    def __init__(
        self,
        repository: Type[SettingRepository] = SettingRepository,
    ) -> None:
        super().__init__(repository=repository)

    def seed(self) -> None:
        if DEVELOPMENT:
            self.data.append(
                {
                    "secret_key": Fernet.generate_key(),
                    "environment": "development",
                },
            )

        super().seed()
