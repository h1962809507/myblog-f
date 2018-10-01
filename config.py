class Config:
    """flask配置"""
    DEBUG = True


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境"""
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
