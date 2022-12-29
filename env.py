import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "13673662").strip()
API_HASH = os.getenv("API_HASH", "90a8ca652259ec84f9ab4afdc7e3846e").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5144413993").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://amritsinghbaba01:1998@cluster0.3tacgfj.mongodb.net/?retryWrites=true&w=majority").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "arbackup1")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
