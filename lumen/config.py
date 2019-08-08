import os


class BaseConfig:
    """
    Base configuration object where default values are set.

    All other configuration classes should inherit from `BaseConfig`
    """

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(BaseConfig):
    """
    Configuration for local development
    """

    ENV = "local"
    DEBUG = True


class TestingConfig(BaseConfig):
    """
    Configuration for testing environment, when the `pytest` command is run
    """

    ENV = "testing"
    TESTING = True


class DevConfig(BaseConfig):
    """
    Configuration for development environment, which should represent our hosted dev setup in kubernetes.

    Contrary to local development where application code should be written, "development" is our playground to test out infrastructure level changes
    """

    ENV = "development"


class ProdConfig(BaseConfig):
    """
    Configuration for production environment, hosted in Kubernetes
    """

    ENV = "production"
