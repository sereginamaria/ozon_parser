from backend.web_server import logger, app
from backend.db import db
@app.route('/')
def hello():
    return 'Hello!'

@app.route('/get_verification_information', methods=['GET'])
def get_verification_information():
    logger.info('Получаем информацию о товаре для верификации')
    return list(db.get_verification_information())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)