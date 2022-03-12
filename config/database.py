from decouple import config
from motor import motor_asyncio

# Connection
client = motor_asyncio.AsyncIOMotorClient(config("DATABASE_URL"))

# Database
db = client['shortener']

# Collections
collection_redirect = db['redirect']
