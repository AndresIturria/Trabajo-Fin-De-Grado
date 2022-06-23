from load_data import load, load_historic
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

batters, catcher, first, second, third, ss, of, pitcher = load()
bat_historic, pitch_historic = load_historic()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.jinja2")

    if request.method == 'POST':

        return render_template("app.jinja2", batters=batters, catcher=catcher, first=first, second=second, third=third,
                               ss=ss, of=of, pitcher=pitcher)


@app.route('/batters/<string:playerID>')
def batters_info(playerID):
    player_historic = bat_historic[bat_historic['playerID'] == playerID]
    player_array = []
    for index, row in player_historic.iterrows():
        year = {"yearID": row['yearID'], "teamID": row['teamID'], "AB": row['AB'], "H": row['H'], "double": row['2B'],
                "triple": row['3B'], "HR": row['HR'], "R": row['R'], "RBI": row['RBI'], "SB": row['SB'], "BB": row['BB'],
                "IBB": row['IBB'], "SO": row['SO'], "HBP": row['HBP'], "nameFirst": row['nameFirst'],
                "nameLast": row['nameLast'], "bats": row['bats'], "throws": row['throws'], "age": row['age'],
                "points": row['points']}
        player_array.append(year)

    return render_template("batters_info.jinja2", player_array=player_array)


@app.route('/pitchers/<string:playerID>')
def pitchers_info(playerID):
    player_historic = pitch_historic[pitch_historic['playerID'] == playerID]
    player_array = []
    for index, row in player_historic.iterrows():
        year = {"yearID": row['yearID'], "teamID": row['teamID'], "W": row['W'], "GF": row['GF'], "SO": row['SO'],
                "ER": row['ER'], "IPouts": row['IPouts'], "BB": row['BB'], "H": row['H'], "HBP": row['HBP'],
                "IBB": row['IBB'], "nameFirst": row['nameFirst'], "nameLast": row['nameLast'], "throws": row['throws'],
                "age": row['age'], "points": row['points']}
        player_array.append(year)

    return render_template("pitchers_info.jinja2", player_array=player_array)


if __name__ == '__main__':
    app.run()
