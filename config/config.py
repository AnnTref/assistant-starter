import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_TOKEN")


APP_NAME = "Clinic Assistant"

URL = {
    'user-agent': "https://httpbin.org/user-agent",
    'headers': "https://httpbin.org/headers",
    'delay': "https://httpbin.org/delay/2",
}

if __name__ == '__main__':
    print(TELEGRAM_BOT_TOKEN)