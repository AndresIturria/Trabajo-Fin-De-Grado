import sys

import pandas as pd

filename1 = "../baseballdatabank/core/Batting.csv"
df_bat = pd.read_csv(filename1)

filename2 = "../baseballdatabank/core/People.csv"
df_people = pd.read_csv(filename2)

df_bat = df_bat[["playerID", "yearID", "teamID", "AB", "H", "2B", "3B", "HR", "R", "RBI", "SB",
                 "BB", "IBB", "SO", "HBP"]]



df_bat = df_bat[df_bat.yearID > 2016]

df_people = df_people[["playerID", "birthYear", "nameFirst", "nameLast", "bats", "throws"]]

df_bat = df_bat.merge(df_people)

df_bat = df_bat[df_bat.birthYear != 0]
age = df_bat["yearID"] - df_bat["birthYear"]
df_bat["age"] = age
df_bat = df_bat.drop(["birthYear"], 1)

points = 2.6*df_bat["H"] + 5.2*df_bat["2B"] + 7.8*df_bat["3B"] + 10.4*df_bat["HR"] + 1.9*df_bat["R"] \
         + 1.9*df_bat["RBI"] + 4.2*df_bat["SB"] + 2.6*df_bat["HBP"] + 2.6*df_bat["BB"] + 2.6*df_bat["IBB"]
df_bat["points"] = points

# -----------------------------------------------------------------------------------------------------------


filename4 = "../2021/2021batting.csv"
df_bat2021 = pd.read_csv(filename4)

playerID = []
for name in df_bat2021["Name"]:
    result = name.split("\\")
    playerID.append(result[1])

df_bat2021["Name"] = playerID
df_bat2021 = df_bat2021.rename(columns={"Name": "playerID"})
df_bat2021 = df_bat2021.rename(columns={"Tm": "teamID"})

df_bat2021 = df_bat2021[["playerID", "age", "yearID", "teamID", "AB", "H", "2B", "3B", "HR", "R", "RBI", "SB",
                 "BB", "IBB", "SO", "HBP"]]
df_bat2021 = df_bat2021.assign(yearID=2021)

points2021 = 2.6*df_bat2021["H"] + 5.2*df_bat2021["2B"] + 7.8*df_bat2021["3B"] + 10.4*df_bat2021["HR"] + 1.9*df_bat2021["R"] \
         + 1.9*df_bat2021["RBI"] + 4.2*df_bat2021["SB"] + 2.6*df_bat2021["HBP"] + 2.6*df_bat2021["BB"] + 2.6*df_bat2021["IBB"]
df_bat2021["points"] = points2021

df_people2021 = pd.read_csv(filename2)
df_people2021 = df_people2021[["playerID", "nameFirst", "nameLast", "bats", "throws", "birthYear"]]



df_bat2021 = df_bat2021.merge(df_people2021)

age = df_bat2021["yearID"] - df_bat2021["birthYear"]
df_bat2021["age"] = age
df_bat2021 = df_bat2021.drop(["birthYear"], 1)

df_global = df_bat.append(df_bat2021, ignore_index=True)
df_global.sort_values(by=["yearID"], ascending=True, inplace=True)
df_global.to_csv("../finished-data/bat-historic.csv", index=False)

# -------------------------------------------------------------------------------------------------------------------------

filename = "../baseballdatabank/core/Pitching.csv"
df_pitch = pd.read_csv(filename)

filename2 = "../baseballdatabank/core/People.csv"
df_people = pd.read_csv(filename2)

df_pitch = df_pitch[["playerID", "teamID", "yearID", "W", "GF", "SO", "ER", "IPouts", "BB", "H", "HBP", "IBB"]]
df_pitch = df_pitch[df_pitch.yearID > 2016]

df_people = df_people[["playerID", "birthYear", "nameFirst", "nameLast", "throws"]]

df_pitch = df_pitch.merge(df_people)

df_pitch = df_pitch[df_pitch.birthYear != 0]
age = df_pitch["yearID"] - df_pitch["birthYear"]
df_pitch["age"] = age
df_pitch = df_pitch.drop(["birthYear"], 1)



points = 8*df_pitch["GF"] + 8*df_pitch["W"] + 3*df_pitch["SO"] - 3*df_pitch["ER"] + df_pitch["IPouts"] - \
         1.3*df_pitch["BB"] - 1.3*df_pitch["IBB"] - 1.3*df_pitch["H"] - 1.3*df_pitch["HBP"]

df_pitch["points"] = points

# ----------------------------------------------------------------------------------------------------
filename = "../2021/2021pitching.csv"
df_pitch2021 = pd.read_csv(filename)

playerID = []
for name in df_pitch2021["Name"]:
    result = name.split("\\")
    playerID.append(result[1])


df_pitch2021["Name"] = playerID
df_pitch2021 = df_pitch2021.rename(columns={"Name": "playerID"})
df_pitch2021 = df_pitch2021.rename(columns={"Tm": "teamID"})
df_pitch2021 = df_pitch2021[["playerID", "teamID", "yearID", "age", "W", "GF", "SO", "ER", "IPouts", "BB", "H", "HBP",
                             "IBB"]]



filename2 = "../baseballdatabank/core/People.csv"
df_people = pd.read_csv(filename2)

df_people = df_people[["playerID", "birthYear", "nameFirst", "nameLast", "throws"]]

df_pitch2021 = df_pitch2021.merge(df_people)

df_pitch2021 = df_pitch2021.assign(yearID=2021)

age = df_pitch2021["yearID"] - df_pitch2021["birthYear"]
df_pitch2021["age"] = age




points = 8*df_pitch2021["GF"] + 8*df_pitch2021["W"] + 3*df_pitch2021["SO"] - 3*df_pitch2021["ER"] + df_pitch2021["IPouts"] - \
         1.3*df_pitch2021["BB"] - 1.3*df_pitch2021["IBB"] - 1.3*df_pitch2021["H"] - 1.3*df_pitch2021["HBP"]
df_pitch2021["points"] = points


df_global = df_pitch.append(df_pitch2021, ignore_index=True)
df_global.sort_values(by=["yearID"], ascending=True, inplace=True)
df_global.to_csv("../finished-data/pitch-historic.csv", index=False)

sys.exit()