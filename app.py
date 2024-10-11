# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Suresh Raja</h1>
    <p>B.E. in Electronics and Communication Engineering</p>
    <p>Azure Cloud Administrator | DevOps Engineer</p>
    <p>Email: sureshraja3007@gmail.com</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
