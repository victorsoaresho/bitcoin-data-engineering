from dotenv import load_dotenv
import os
import requests

load_dotenv()

class CoinGecko:
    def __init__(self):
        self.domain = 'https://api.coingecko.com/api/v3/'
        self.api_key = os.getenv('API_KEY')

    def get_info(self, coin):
        url = f"{self.domain}coins/{coin}"
        headers = self.create_headers()

        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def get_market_chart(self, coin, currency, days):
        url = f"{self.domain}coins/{coin}/market_chart"
        headers = self.create_headers(currency=currency, days=days)

        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def create_headers(self, currency=None, days=None):
        headers = {"x-cg-demo-api-key": self.api_key}

        if currency:
            headers["vs_currency"] = currency
        if days:
            headers["days"] = days
        
        return headers

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro {response.status_code}: {response.text}")
