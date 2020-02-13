class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECERT_KEY = 'xd6+@+\xc6\x03\xaa\r>0>c\xb3\x1f2z\x9c;\x8f\xbaXoo\xc9'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15

class DevelopmengtConfig(BaseConfig):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
        'development':DevelopMentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
}


