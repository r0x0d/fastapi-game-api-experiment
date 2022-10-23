from unittest import mock
from carnage.database import session


@mock.patch.object(session, "create_engine")
@mock.patch.object(session, "sessionmaker")
def test_create_session(create_engine_mock, sessionmaker_mock):
    session.create_session()
