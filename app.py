from load_data import load
from flask import Flask, render_template, request

app = Flask(__name__)

batters, catcher, first, second, third, ss, of, pitcher = load()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.jinja2")

    if request.method == 'POST':

        return render_template("app.jinja2", batters=batters, catcher=catcher, first=first, second=second, third=third,
                               ss=ss, of=of, pitcher=pitcher)


@app.route('/player/<string:playerID>')
def player(playerID):

    return render_template("player.jinja2", playerID=playerID)


if __name__ == '__main__':
    app.run()
