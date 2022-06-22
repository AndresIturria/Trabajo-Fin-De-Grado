import pandas as pd


def load():
    df_bat = pd.read_csv("./data/finished-data/batting-final.csv")
    df_pitch = pd.read_csv("./data/finished-data/pitching-final.csv")

    batters_array = []
    catcher_array = []
    first_array = []
    second_array = []
    third_array = []
    ss_array = []
    of_array = []
    pitchers_array = []

    for index, row in df_bat.iterrows():
        batter = {"playerID": row["playerID"], "firstName": row["nameFirst"], "lastName": row["nameLast"],
                  "POS": row["POS"], "teamID": row["teamID"], "points": row["points"]}
        batters_array.append(batter)

    for index, row in df_pitch.iterrows():
        pitcher = {"playerID": row["playerID"], "firstName": row["nameFirst"], "lastName": row["nameLast"],
                   "teamID": row["teamID"], "points": row["points"]}
        pitchers_array.append(pitcher)

    for player in batters_array:

        if player["POS"] == "C":
            catcher_array.append(player)

        elif player["POS"] == "1B":
            first_array.append(player)

        elif player["POS"] == "2B":
            second_array.append(player)

        elif player["POS"] == "3B":
            third_array.append(player)

        elif player["POS"] == "SS":
            ss_array.append(player)

        elif player["POS"] == "OF":
            of_array.append(player)

    return (batters_array, catcher_array, first_array, second_array, third_array, ss_array, of_array, pitchers_array)

