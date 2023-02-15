from Encryption_Key_Gen import encryption_key
from flask import Flask, render_template, request
import logging
import settings
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_encryption():
    passphrase = request.form.get('passphrase')
    salt = request.form.get('salt')
    key = encryption_key(passphrase, salt)
    key = key.get_key()
    # app.logger.debug(f"Test")
    return render_template("key.html", key=key)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)