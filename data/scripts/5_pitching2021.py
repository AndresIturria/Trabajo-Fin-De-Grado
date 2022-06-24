import pandas as pd
import sys


# Ojo: la columna yearID de el fichero de 2021, tiene el año 2020, esto es para poder hacer el merge con
# el park, no la necesitamos para calcular la edad, ya que venia en el fichero, y después la quitamos.

filename = "../2021/2021pitching.csv"
df_pitch = pd.read_csv(filename)

# Arreglamos la columna name para dejar solo el playerID
playerID = []
for name in df_pitch["Name"]:
    result = name.split("\\")
    playerID.append(result[1])


df_pitch["Name"] = playerID
df_pitch = df_pitch.rename(columns={"Name": "playerID"})

# Tomamos solo columnas que nos interesan y juntamos con el resto de los datos

df_pitch = df_pitch[["playerID", "age", "W", "GF", "SO", "ER", "IPouts", "BB", "H", "HBP", "IBB"]]


# Creamos la columna points

df_global = df_pitch

points = 8*df_global["GF"] + 8*df_global["W"] + 3*df_global["SO"] - 3*df_global["ER"] + df_global["IPouts"] - \
         1.3*df_global["BB"] - 1.3*df_global["IBB"] - 1.3*df_global["H"] - 1.3*df_global["HBP"]

df_global["points"] = points

#Eliminamos columnas que ya no necesitamos

df_global = df_global.drop(["W", "GF", "SO", "ER", "IPouts", "BB", "H", "HBP", "IBB"], 1)

# Ahora unimos con el csv global

filename4 = "../intermediate-steps/pitching_step1.csv"
df_old = pd.read_csv(filename4)
df_global = df_old.append(df_global, ignore_index=True)


# Ordenamos y guardamos en csv
df_global.sort_values(by=["points"], ascending=False, inplace=True)
df_global.to_csv("../intermediate-steps/pitching_step2.csv", index=False)

sys.exit()