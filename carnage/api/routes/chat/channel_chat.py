from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.chat import (
    CreateChannelChatSchema,
    ListChannelChatSchema,
    UpdateChannelChatSchema,
)
from carnage.database.repository.chat import ChannelChatRepository


class ChannelChatRoute(BaseRoute):
    list_schema = ListChannelChatSchema
    create_schema = CreateChannelChatSchema
    update_schema = UpdateChannelChatSchema

    def __init__(
        self,
        name: str = "channel_chat",
        tags: list[str] = ["channel_chat"],
        repository: Type[ChannelChatRepository] = ChannelChatRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListChannelChatSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListChannelChatSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateChannelChatSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateChannelChatSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = ChannelChatRoute()
