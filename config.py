DEBUG = True

USERNAME = 'root'
PASSWORD = '123456'
SERVER = 'localhost'
DB = 'tabela_brasileirao'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'aplicacao_flask'
