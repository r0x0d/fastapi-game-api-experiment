import pytest

from carnage.database.seeds import setting


def test_setting_seed_init(database_session_mock):
    seed = setting.SettingSeed()

    assert seed.name is not None
    assert seed.data is not None


@pytest.mark.parametrize(("development"), (("1"), ("")))
def test_seed(development, monkeypatch, database_session_mock):
    monkeypatch.setattr(setting, "DEVELOPMENT", development)
    seed = setting.SettingSeed()
    seed.seed()

    for data in seed.data:
        assert "secret_key" in data
        assert "environment" in data


@pytest.mark.parametrize(
    ("seed_exist"),
    (
        (True),
        (False),
    ),
)
def test_validate_seed(seed_exist, database_session_mock, monkeypatch):
    seed = setting.SettingSeed()
    monkeypatch.setattr(
        seed.repository,
        "select_by_environment",
        lambda environment: seed_exist,
    )

    # We don't care too much about the rest
    assert seed.validate_seed(seed={"environment": "test"}) == seed_exist
