import os
from dotenv import load_dotenv


class Setting:
    load_dotenv()
    API_KEY = os.environ.get("API_KEY")

setting = Setting()
