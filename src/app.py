from flask import Flask
from flask import request

app = Flask(__name__)

secret_key = 'zzm_secret'
clipboard = '空'

@app.route('/send', methods=['POST'])
def send():
    secret = request.form.get('secret')
    if secret != secret_key:
        return "error secret key!"
    else:
        global clipboard
        clipboard = request.form.get('clipboard')
        return "success"

@app.route('/get', methods=['POST'])
def get():
    secret = request.form.get('secret')
    if secret != secret_key:
        return "error secret key!"
    else:
        global clipboard
        return clipboard

if __name__ == "__main__":
    app.run(debug=True, port=8080)
