import pandas as pd
import sys

# Ojo: la columna yearID de el fichero de 2021, tiene el año 2020, esto es para poder hacer el merge con
# el park, no la necesitamos para calcular la edad, ya que venia en el fichero, y después la quitamos.

filename = "../2021/2021batting.csv"
df_bat = pd.read_csv(filename)

# Arreglamos la columna name para dejar solo el playerID
playerID = []
for name in df_bat["Name"]:
    result = name.split("\\")
    playerID.append(result[1])

df_bat["Name"] = playerID
df_bat = df_bat.rename(columns={"Name":"playerID"})
# df_bat = df_bat.rename(columns={"Tm":"teamID"})
# df_bat = df_bat.rename(columns={"Lg":"lgID"})

# Quitamos jugadores sin turnos al bate

df_bat = df_bat[df_bat.AB != 0]


# Tomamos solo columnas que nos interesan y juntamos con el resto de los datos

# df_bat = df_bat[["playerID", "yearID", "age", "teamID", "AB", "H", "2B", "3B", "HR", "R", "RBI", "SB",
#                 "BB", "IBB", "SO", "HBP"]]

df_bat = df_bat[["playerID", "yearID", "age", "AB", "H", "2B", "3B", "HR", "R", "RBI", "SB",
                 "BB", "IBB", "SO", "HBP"]]



filename2 = "../baseballdatabank/core/People.csv"
df_people = pd.read_csv(filename2)

# filename3 = "../baseballdatabank/core/Teams.csv"
# df_teams = pd.read_csv(filename3)

# df_bat = df_bat.merge(df_people)
df_global = df_bat
# df_people = df_people[["playerID", "bats"]]
# df_teams = df_teams[["teamID", "divID","lgID", "yearID", "park"]]


# df_global = df_bat.merge(df_people)
# df_global = df_global.merge(df_teams)


# Una vez hecho el merge podemos prescindir de yearID
df_global = df_global.drop(["yearID"], 1)


# Calculamos los puntos del 2021
points = 2.6*df_global["H"] + 5.2*df_global["2B"] + 7.8*df_global["3B"] + 10.4*df_global["HR"] + 1.9*df_global["R"] \
         + 1.9*df_global["RBI"] + 4.2*df_global["SB"] + 2.6*df_global["HBP"] + 2.6*df_global["BB"] + 2.6*df_global["IBB"]

df_global["points"] = points



# Ya calculados los puntos quitamos columnas usadas para calcularlos

df_global = df_global.drop(["AB", "H", "2B", "3B", "HR", "R", "RBI", "SB",
                 "BB", "IBB", "SO", "HBP"], 1)

# Ahora unimos con el csv global, de una vez quitamos birth country

filename4 = "../intermediate-steps/batting_step1.csv"
df_old = pd.read_csv(filename4)
# df_old = df_old.drop(["birthCountry"], 1)

df_global = df_old.append(df_global, ignore_index=True)


# Ordenamos y guardamos en csv
df_global.sort_values(by=["points"], ascending=False, inplace=True)
df_global.to_csv("../intermediate-steps/batting_step2.csv", index=False)

sys.exit()