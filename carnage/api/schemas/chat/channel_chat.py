from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.chat import ChannelChatModel


class ListChannelChatSchema(
    sqlalchemy_to_pydantic(ChannelChatModel),  # type: ignore
):
    pass


class UpdateChannelChatSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ChannelChatModel,
        config=None,
    ),
):
    pass


class CreateChannelChatSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ChannelChatModel,
        config=None,
    ),
):
    pass
