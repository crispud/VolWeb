import os

class Database:
    NAME = os.getenv('POSTGRES_DB','volweb')
    USER = os.getenv('POSTGRES_USER','volweb')
    PASSWORD = os.getenv('POSTGRES_PASSWORD','volweb')
    HOST = os.getenv('DATABASE_HOST',"localhost")
    PORT = os.getenv('DATABASE_PORT',5432)

class Secrets:
    SECRET_KEY = os.getenv('DJANGO_SECRET','DevSecretKey')
    BROKER_URL = os.getenv('BROKER_URL','amqp://admin:mypass@localhost:5672')
    VT_API_KEY = os.getenv('VT_API_KEY',"YOUR_VT_API_KEY_HERE")


class Debug:
    DEBUG_MODE = os.getenv('DEBUG_MODE','True')
