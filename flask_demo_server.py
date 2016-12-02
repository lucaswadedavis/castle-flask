from flask import Flask
from flask import render_template
from flask import request

from castleio_flask.castle import Castle

app = Flask(__name__)

api_secret = '<PUT_YOUR_API_SECRET_HERE>'

@app.route('/')
def index():
    castle = Castle(request, api_secret=api_secret)
    castle.track(name='$login.succeeded', user_id='<REPLACE_WITH_FAKE_USER_ID>')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8181)
