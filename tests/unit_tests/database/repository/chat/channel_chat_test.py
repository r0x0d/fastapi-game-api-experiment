from carnage.database.repository import chat


def test_channel_chat_repository_init(database_session_mock):
    repository = chat.ChannelChatRepository()
    assert repository.session is not None
