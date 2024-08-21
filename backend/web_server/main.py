from web_server.ozon_routes import ozon
from web_server.wb_routes import wb
from web_server import app

from main_config import BASE_URL

app.register_blueprint(ozon)
app.register_blueprint(wb)

if __name__ == "__main__":
    app.run(host=BASE_URL, port=5001, debug=True)