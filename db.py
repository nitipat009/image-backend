from pymongo import MongoClient
from dotenv import dotenv_values
config = dotenv_values(".env")
conn = MongoClient(config.get("MONGODB_URL"))
db = conn.Toc