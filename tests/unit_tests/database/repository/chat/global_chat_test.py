from carnage.database.repository import chat


def test_global_chat_repository_init(database_session_mock):
    repository = chat.GlobalChatRepository()
    assert repository.session is not None
