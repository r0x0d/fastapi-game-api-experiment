"""Module to represent an Channel Chat schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.chat import ChannelChatModel


class ListChannelChatSchema(
    sqlalchemy_to_pydantic(ChannelChatModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateChannelChatSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ChannelChatModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateChannelChatSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ChannelChatModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
