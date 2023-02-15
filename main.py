from Encryption_Key_Gen import encryption_key
from flask import Flask, render_template, request

import os

app = Flask(__name__)
#app.secret_key = os.environ.get('APP_SECRET_KEY')

@app.route('/', methods=['GET'])
def index():
    return render_template('encryption_key_gen.html')

@app.route('/', methods=['POST'])
def get_encryption():
    password = request.args.get('password')
    salt = request.args.get('salt')
    print(password)
    print(salt)
    key = encryption_key(password, salt)
    key = key.get_key()
    return(key)

if __name__ == '__main__':
    app.run()

#password = 'Testing'
#salt = "Right"
#test = encryption_key(password, salt)
#key = test.get_key()
#print(key)
