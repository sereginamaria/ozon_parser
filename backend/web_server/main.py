from web_server.ozon_routes import ozon
from web_server.wb_routes import wb
from web_server import app

app.register_blueprint(ozon)
app.register_blueprint(wb)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    # app.run(host="195.133.46.183", port=5001, debug=True)