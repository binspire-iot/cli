import os
from dotenv import load_dotenv
from db.database import Database

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

db = Database(DATABASE_URL)

db.connect()
