from my_parsers.parser_web_server.ozon_routes import ozon
from my_parsers.parser_web_server.wb_routes import wb
from my_parsers.parser_web_server import app

from main_config import BASE_URL

app.register_blueprint(ozon)
app.register_blueprint(wb)

if __name__ == "__main__":
    app.run(host=BASE_URL, port=5002, debug=True)