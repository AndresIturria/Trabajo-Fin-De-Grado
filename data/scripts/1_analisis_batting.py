import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Creamos dataframe con los campos necesarios para identificar a los jugadores y generar la columna points

filename1 = "../baseballdatabank/core/Batting.csv"
df_bat = pd.read_csv(filename1)

filename2 = "../baseballdatabank/core/People.csv"
df_people = pd.read_csv(filename2)

df_bat = df_bat[["playerID", "yearID", "AB", "H", "2B", "3B", "HR", "R", "RBI", "SB",
                 "BB", "IBB", "SO", "HBP"]]

df_people = df_people[["playerID", "birthYear"]]

df_bat = df_bat.merge(df_people)

# los NaN son campos en donde no hay valores registrados, cambiamos a 0s
df_bat.fillna(0, inplace=True)

# Filtro años que nos interesan
df_bat = df_bat[df_bat.yearID > 2002]

# Creamos la columna points
points = 2.6*df_bat["H"] + 5.2*df_bat["2B"] + 7.8*df_bat["3B"] + 10.4*df_bat["HR"] + 1.9*df_bat["R"] \
         + 1.9*df_bat["RBI"] + 4.2*df_bat["SB"] + 2.6*df_bat["HBP"] + 2.6*df_bat["BB"] + 2.6*df_bat["IBB"]
df_bat["points"] = points

# Creamos la columna age, antes quitamos las columnas donde el año de nacimiento es desconocido
df_bat = df_bat[df_bat.birthYear != 0]
age = df_bat["yearID"] - df_bat["birthYear"]
df_bat["age"] = age

# Filtramos entradas de jugadores que no tuvieron turnos al bate.
df_bat = df_bat[df_bat.AB != 0]

# En una temporada completa un jugador tiene entre 500 a 600 turnos, filtramos jugadores con menos de 100 turnos.
# Estos suelen ser suplentes, o jugadores lesionados, cuyas temporadas no representan un dato significativo.
df_bat = df_bat[df_bat.AB > 100]


# Una vez calculados los puntos quitamos las columnas que se usan para calcularlos, quitamos también birthyear y yearID,
# usados para calcular la edad.
df_bat = df_bat.drop(["AB", "H", "2B", "3B", "HR", "R", "RBI", "SB",
                      "BB", "IBB", "SO", "HBP", "birthYear", "yearID"], 1)

# Calculamos media de puntos por edad para visualizar en gráfica.
min_age = int(min(df_bat["age"]))
max_age = int(max(df_bat["age"]))
averages = []

for i in range(min_age, max_age +1):
    age_filter = df_bat[df_bat.age == i]
    avg = np.mean(age_filter["points"])
    averages.append(avg)
    player_count = len(age_filter)
    print(i, avg, player_count)

# Los primeros años y los últimos fluctuan, una razón es que no hay tantos jugadores con esas edades, por lo cual
# jugadores con puntajes altos desvían bastante del promedio.
# En general podemos ver como lentamente crecen los puntos llegando al pico de los 29 años y después va bajando
# Mientras las capacidades físicas y reflejos de los jugadores se deterioran con los años.

fig, (ax1, ax2) = plt.subplots(2)

ax1.scatter(x=df_bat["age"], y=df_bat["points"])
ax1.set(xlabel="age", ylabel="points")
ax1.set_title("Points vs Age")
ax1.label_outer()  # Hide the x label in the top chart

ax2.scatter(x=list(range(min_age, max_age +1)), y=averages)
ax2.set(xlabel="Age", ylabel="points")
ax2.set_title("Points average per Age")

plt.savefig("../charts/points_age_batting.png")
df_bat.to_csv("../intermediate-steps/batting_step1.csv", index=False)
sys.exit()
