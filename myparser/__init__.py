from flask import Flask
application = Flask(__name__, template_folder='../card_creator/templates')

if __name__ == "__main__":
    application.run(host="127.0.0.1", port=5000, debug=True)
