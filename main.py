from Encryption_Key_Gen import encryption_key
from flask import Flask, render_template, request
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

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
    return(key)

if __name__ == '__main__':
    app.run(host='0.0.0.0')