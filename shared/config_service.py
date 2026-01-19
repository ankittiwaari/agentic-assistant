from dotenv import load_dotenv
from os import getenv
load_dotenv()

def get_config(key):
    key = getenv(key)
    if key == "":
        print("Key not found")
    return key 