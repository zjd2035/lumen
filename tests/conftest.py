import pytest

from lumen.app import create_app


@pytest.fixture()
def app():
    """
    Create an instance of the flask application
    """
    return create_app()


@pytest.fixture()
def app_client(app):
    """
    A flask test client allows you to invoke http methods against an instance of the application
    """
    yield app.test_client()
