from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection URL (local instance)
MONGO_URL = "mongodb://127.0.0.1:27017/management"

# Create a client and connect to the management database
client = AsyncIOMotorClient(MONGO_URL)
db = client.management

# Test connection by pinging the database
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
items_collection = db.get_collection("items")
counters_collection = db.get_collection("counters")
clockin_collection = db.get_collection("clockin")
