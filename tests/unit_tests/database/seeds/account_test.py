import pytest

from carnage.database.seeds import account


def test_account_seed_init(database_session_mock):
    seed = account.AccountSeed()

    assert seed.name is not None
    assert seed.data is not None


@pytest.mark.parametrize(
    ("seed_exist"),
    (
        (True),
        (False),
    ),
)
def test_validate_seed(seed_exist, database_session_mock, monkeypatch):
    seed = account.AccountSeed()
    monkeypatch.setattr(
        seed.repository,
        "select_by_username",
        lambda username: seed_exist,
    )

    # We don't care too much about the rest
    assert seed.validate_seed(seed={"username": "test"}) == seed_exist
