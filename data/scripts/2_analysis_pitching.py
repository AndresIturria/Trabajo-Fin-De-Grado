import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

filename = "../baseballdatabank/core/Pitching.csv"
df_pitch = pd.read_csv(filename)

filename2 = "../baseballdatabank/core/People.csv"
df_people = pd.read_csv(filename2)

# filename3 = "../baseballdatabank/core/Teams.csv"
# df_teams = pd.read_csv(filename3)

# Creamos dataframe con los campos necesarios para identificar a los jugadores y generar la columna points
# Creamos los dataframes para obtener edad, equipo, liga, división y estadio.
# Unimos los dataframe en uno global
df_pitch = df_pitch[["playerID", "yearID", "W", "GF", "SO", "ER", "IPouts", "BB", "H", "HBP", "IBB"]]

df_people = df_people[["playerID", "birthYear"]]

# df_teams = df_teams[["yearID", "teamID", "divID", "lgID", "park"]]

df_pitch = df_pitch.merge(df_people)
# df_pitch = df_pitch.merge(df_teams)

# los NaN son campos en donde no hay valores registrados y en el csv original vienen como "####", cambiamos a 0s
df_pitch.fillna(0, inplace=True)

# Filtro años que nos interesan

df_pitch = df_pitch[df_pitch.yearID > 2002]

# Creamos la columna age, antes quitamos las columnas donde el año de nacimiento es desconocido

df_pitch = df_pitch[df_pitch.birthYear != 0]
age = df_pitch["yearID"] - df_pitch["birthYear"]
df_pitch["age"] = age

# Creamos la columna points

points = 8*df_pitch["GF"] + 8*df_pitch["W"] + 3*df_pitch["SO"] - 3*df_pitch["ER"] + df_pitch["IPouts"] - \
         1.3*df_pitch["BB"] - 1.3*df_pitch["IBB"] - 1.3*df_pitch["H"] - 1.3*df_pitch["HBP"]

df_pitch["points"] = points

# Filtramos entradas de jugadores que tuvieron menos de 20 outs, para filtrar suplentes y lesionados.

df_pitch = df_pitch[df_pitch.IPouts > 20]


# Eliminamos columnas que ya no necesitamos

df_pitch = df_pitch.drop(["birthYear", "yearID", "W", "GF", "SO", "ER", "IPouts", "BB", "H", "HBP", "IBB"], 1)

# Ordenar los datos por la columna points.
df_pitch.sort_values(by=["points"], ascending=False, inplace=True)

# Guardar en csv
df_pitch.to_csv("../intermediate-steps/pitching_step1.csv", index=False)

# -------------------------------------------------------------------------------------------------------------------
# Calculamos media de puntos por edad para visualizar en gráfica.

min_age = int(min(df_pitch["age"]))
max_age = int(max(df_pitch["age"]))
averages = []

for i in range(min_age, max_age +1):
    age_filter = df_pitch[df_pitch.age == i]
    avg = np.mean(age_filter["points"])
    averages.append(avg)
    player_count = len(age_filter)

    print(i, avg, player_count)

# A partir de los 22 que tenemos una cantidad significativa de datos se ve como crece hasta los 30 años.
# Empieza a descender, pero después encontramos otro pico y desciende otra vez.
# En el pico hay menos datos, por lo cual se puede ver más influenciado por outliers.

fig, (ax1, ax2) = plt.subplots(2)

ax1.scatter(x=df_pitch["age"], y=df_pitch["points"])
ax1.set(xlabel="age", ylabel="points")
ax1.set_title("Points vs Age")
ax1.label_outer()  # Hide the x label in the top chart

ax2.scatter(x=list(range(min_age, max_age +1)), y=averages)
ax2.set(xlabel="Age", ylabel="points")
ax2.set_title("Points average per Age")

plt.savefig("../charts/points_age_pitching.png")

sys.exit()