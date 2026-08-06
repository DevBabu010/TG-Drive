from pyrogram import Client
from app.core.config import API_ID, API_HASH

app = Client(
    "tgdrive",
    api_id=API_ID,
    api_hash=API_HASH
)