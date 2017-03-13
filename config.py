class Config(object):
    """
    Common Configuration
    """
    # Put any common configuration here

class DevelopmentConfig(Config):
    """
    Development configuration
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production Config
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
