from typing import Any, Type

from cryptography.fernet import Fernet

from carnage.database.repository.setting import SettingRepository
from carnage.database.seeds.base import BaseSeed


class SettingSeed(BaseSeed):
    name: str = "setting"
    data: list[dict[str, Any]] = [
        {
            "secret_key": Fernet.generate_key(),
            "environment": "development",
        },
    ]

    def __init__(
        self,
        repository: Type[SettingRepository] = SettingRepository,
    ) -> None:
        super().__init__(repository=repository)
