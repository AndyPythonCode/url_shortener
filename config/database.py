import asyncio
from decouple import config
from motor import motor_asyncio

# Connection
client = motor_asyncio.AsyncIOMotorClient(config("DATABASE_URL"))
client.get_io_loop = asyncio.get_event_loop

# Database
db = client['shortener']

# Collections
collection_redirect = db['redirect']

