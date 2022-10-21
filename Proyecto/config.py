class Config:
    SECRET_KEY = 'Kgsggsgs!"#aammdsnsn'
    
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'proyecto'
    
config = {
    'development': DevelopmentConfig
}