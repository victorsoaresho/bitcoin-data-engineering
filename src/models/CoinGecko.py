from dotenv import load_dotenv
import os

load_dotenv()

class CoinGecko():
    def __init__(self):
        self.url = 'https://pro-api.coingecko.com/api/v3/'
        self.api_key = os.getenv('API_KEY')
        