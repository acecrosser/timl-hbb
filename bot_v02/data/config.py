import os
from py_dotenv import read_dotenv

path = os.path.abspath('.' + 'env')
read_dotenv(path)

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins = [
    os.getenv('ADMIN_ID')
]