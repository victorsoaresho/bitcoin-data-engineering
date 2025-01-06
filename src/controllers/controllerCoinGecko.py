from flask import Blueprint, jsonify, request
from models.CoinGecko import CoinGecko

coingecko_blueprint = Blueprint('CoinGecko', __name__)
coin_gecko = CoinGecko()

@coingecko_blueprint.route('/coin_info/<coin>', methods=['GET'])
def get_coin_info(coin):
    try:
        data = coin_gecko.get_info(coin)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@coingecko_blueprint.route('/market_chart/<coin>', methods=['GET'])
def get_market_chart(coin):
    currency = request.args.get('currency', default='usd')
    days = request.args.get('days', default=30)

    try:
        data = coin_gecko.get_market_chart(coin, currency, days)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500