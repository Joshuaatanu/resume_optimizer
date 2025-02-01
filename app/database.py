import os
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorGridFSBucket

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "resume_optimizer"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
fs = AsyncIOMotorGridFSBucket(db)
