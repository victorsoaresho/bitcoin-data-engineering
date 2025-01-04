from flask import Flask, jsonify, request
from models.CoinGecko import CoinGecko

app = Flask(__name__)
coin_gecko = CoinGecko()

@app.route('/coin_info/<coin>', methods=['GET'])
def get_coin_info(coin):
    try:
        data = coin_gecko.get_info(coin)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/market_chart/<coin>', methods=['GET'])
def get_market_chart(coin):
    currency = request.args.get('currency', default='usd')
    days = request.args.get('days', default=30)
    
    try:
        data = coin_gecko.get_market_chart(coin, currency, days)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
