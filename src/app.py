from flask import Flask
from controllers.controllerCoinGecko import coingecko_blueprint

app = Flask(__name__)
app.register_blueprint(coingecko_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
