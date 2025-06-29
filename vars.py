#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28201702"))
API_HASH = environ.get("API_HASH", "31c9bbed9c688b89736d94da7e89653b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7526345865"))
CREDIT = "𝑨𝒄𝒆 ℬ𝒐𝒕𝒛𝒛 〠"
AUTH_USER = os.environ.get('AUTH_USERS', '6831195071').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
