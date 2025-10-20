import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "6924389613").split()))

API_ID = int(os.getenv("API_ID", "21800647"))

API_HASH = os.getenv("API_HASH", "f088e630dbf4a16cb89830f2e411f6af")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7312972618:AAEWIMr7UV9-mIqA2UXulD8A5r22T2MX03E")

OWNER_ID = int(os.getenv("OWNER_ID", "6924389613"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ibraramdan376_db_user:lzvLg6KeU84bVWj5@ubotku.mogdzhf.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002807087960"))
