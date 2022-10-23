from carnage.database.repository import base
from tests.unit_tests.conftest import DummySqlModel


def test_base_repository_init(database_session_mock):
    repository = base.BaseRepository()
    assert repository.session is not None


def test_insert(database_session_mock):
    repository = base.BaseRepository(model=DummySqlModel)
    repository.insert(values={"test": 1})
    assert repository.session.execute.called_once()
    assert repository.session.commit.called_once()


def test_select(database_session_mock):
    repository = base.BaseRepository(model=DummySqlModel)
    repository.select()

    assert repository.session.execute.called_once()


def test_select_first(database_session_mock):
    repository = base.BaseRepository(model=DummySqlModel)
    repository.select_first()
    assert repository.session.execute.called_once()


def test_select_by_id(database_session_mock):
    repository = base.BaseRepository(model=DummySqlModel)
    repository.select_by_id(identifier="c32c033a-4d00-11ed-979e-641c67e34d72")
    assert repository.session.execute.called_once()


def test_select_by_name(database_session_mock):
    repository = base.BaseRepository(model=DummySqlModel)
    repository.select_by_name(name="test")
    assert repository.session.execute.called_once()


def test_update(database_session_mock):
    repository = base.BaseRepository(model=DummySqlModel)
    repository.update(
        values={"test": 1},
        identifier="c32c033a-4d00-11ed-979e-641c67e34d72",
    )
    assert repository.session.execute.called_once()
    assert repository.session.commit.called_once()


def test_delete(database_session_mock):
    repository = base.BaseRepository(model=DummySqlModel)
    repository.delete(identifier="c32c033a-4d00-11ed-979e-641c67e34d72")
    assert repository.session.execute.called_once()
    assert repository.session.commit.called_once()
