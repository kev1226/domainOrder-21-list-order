import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["orders"]


async def find_orders_by_email(email: str):
    cursor = collection.find({"user.email": email})
    return await cursor.to_list(length=None)
