from os import getenv
from dotenv import load_env

load_env()
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME")
CHATS = getenv("AUTHORIZED_CHATS",None)
if CHATS:
    CHATS = CHATS.split("")
TESTERS = getenv("TESTERS",None)
if TESTERS:
    TESTERS = TESTERS.split("")
