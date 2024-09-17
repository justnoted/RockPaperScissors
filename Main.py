from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import User

app = Flask(__name__)
app.secret_key = "1234"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game.html')
# What do I put here?

@app.route('/results.html')
def result():
    ret_val = request.args.get('id')

    return render_template("imageresult.html", ret_val=ret_val)


@app.route('/social.html')
def social():
    if session.get('username'):
        return render_template("social.html")


if __name__ == '__main__':
    app.run()
