class BaseConfig:
    """
    Base configuration object where default values are set.

    All other configuration classes should inherit from `BaseConfig`
    """
    DEBUG = False
    TESTING = False

class LocalConfig(BaseConfig):
    """
    Configuration for local development
    """
    DEBUG = True
    FOO = 'Joshua'

class TestingConfig(BaseConfig):
    """
    Configuration for testing environment, when the `pytest` command is run
    """
    TESTING = True

class DevConfig(BaseConfig):
    """
    Configuration for development environment, which should represent our hosted dev setup in kubernetes.

    Contrary to local development where application code should be written, "dev" is our playground to test out infrastructure level changes
    """

class ProdConfig(BaseConfig):
    """
    Configuration for production environment, hosted in Kubernetes
    """