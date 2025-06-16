import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path='.env'
)
DB_CONFIG = {
    'dbname': 'books',
    'user': 'postgres',
    'password': 'books',
    'host': 'localhost',
    'port': 5432
}
