import pandas as pd

df_bat = pd.read_csv("../finished-data/training_bat.csv")

df_bat_team = pd.read_csv("../prediction-data/2022battingraw.csv")
df_bat_team = df_bat_team[["playerID", "teamID"]]

df_bat_fielding = pd.read_csv("../baseballdatabank/core/Fielding.csv")
df_bat_fielding = df_bat_fielding[["playerID", "POS", "yearID"]]

df_bat_people = pd.read_csv("../baseballdatabank/core/People.csv")
df_bat_people = df_bat_people[["playerID", "nameFirst", "nameLast"]]

df_bat = df_bat.merge(df_bat_people)
df_bat = df_bat.merge(df_bat_team)

df_bat["yearID"] = 2020
df_bat = df_bat.merge(df_bat_fielding)
df_bat = df_bat.drop(["yearID"], 1)
# df_bat.drop_duplicates("playerID", keep="last", inplace=True)

df_bat.to_csv("../finished-data/batting-final.csv", index=False)

# ------------------------------------------------------------------------

df_pitch = pd.read_csv("../finished-data/training_pitch.csv")

df_pitch_team = pd.read_csv("../prediction-data/2022pitchingraw.csv")
df_pitch_team = df_pitch_team[["playerID", "teamID"]]

df_pitch_people = pd.read_csv("../baseballdatabank/core/People.csv")
df_pitch_people = df_pitch_people[["playerID", "nameFirst", "nameLast"]]

df_pitch = df_pitch.merge(df_pitch_team)
df_pitch = df_pitch.merge(df_pitch_people)

df_pitch.to_csv("../finished-data/pitching-final.csv", index=False)