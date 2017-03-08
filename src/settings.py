import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
CRAFT_CFG = {
    "owner": os.environ.get("CRAFT_OWNER"),
    "project": os.environ.get("CRAFT_PROJECT"),
    "token": os.environ.get("CRAFT_TOKEN"),
    "url": os.environ.get("CRAFT_URL")
}