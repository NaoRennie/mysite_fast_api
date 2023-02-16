from decouple import config
import motor.motor_asyncio

MONGO_API_KEY = config('MONGO_API_KEY')


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_API_KEY)
database = client.MYSITE_DB
collection_user = database.user
collection_todo= database.todo


async def db_create_todo(data: dict) -> dict:
    todo = await collection_todo.insert_one(data)