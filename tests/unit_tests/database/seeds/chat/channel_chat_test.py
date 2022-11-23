from carnage.database.seeds import chat


def test_channel_chat_seed_init(database_session_mock):
    seed = chat.ChannelChatSeed()

    assert seed.name is not None
    assert seed.data is not None
