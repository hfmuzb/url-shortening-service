import os


class Config:
    SHORTENED_STRING_LENGTH = int(os.getenv("SHORTENED_STRING_LENGTH", 5))
    DEFAULT_DAYS_VALID = int(os.getenv("DEFAULT_DAYS_VALID", 90))

    # Database configuration
    DB_STRING = 'postgresql://{username}:{password}@{container}:{port}/{db_name}'
    DB_USERNAME = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'mysecretpassword')
    DB_CONTAINER = os.getenv('POSTGRES_CONTAINER_NAME', 'localhost')
    DB_PORT = os.getenv('POSTGRES_PORT', '8001')
    DB_NAME = os.getenv('DB_NAME', 'postgres')

    DB_STRING = DB_STRING.format(username=DB_USERNAME,
                                 password=DB_PASSWORD,
                                 container=DB_CONTAINER,
                                 port=DB_PORT,
                                 db_name=DB_NAME)

    ROOT_URL = os.getenv("ROOT_URL", "localhost:8000")


config = Config()
