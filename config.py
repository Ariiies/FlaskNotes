class Config:
    secret_key = "clave_secreta_flask"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PORT = 3308
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'Reviews'


config = {'development': DevelopmentConfig}