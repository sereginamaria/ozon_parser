from __init__ import logger, app
from ozon

@app.route('/')
def hello():
    return 'Hello!'

@app.route('get_verification_information', methods=['GET'])
def get_verification_information():
    return 'q'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)