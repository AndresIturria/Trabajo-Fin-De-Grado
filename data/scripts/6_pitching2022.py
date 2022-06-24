import pandas as pd
import sys


#  Leer los datos
filename = "../prediction-data/2022pitchingraw.csv"
df_pitch = pd.read_csv(filename)

filename2 = "../baseballdatabank/core/People.csv"
df_people = pd.read_csv(filename2)
df_people = df_people[["playerID", "birthYear"]]

df_global = df_pitch.merge(df_people)

# Edad
df_global["age"] = 2022 - df_global["birthYear"]

#Quitamos birthYear y yearID
df_global = df_global.drop(["birthYear", "yearID"], 1)


# Quitamos jugadores que no están en los datos de entrenamiento.
filename4 = "../intermediate-steps/pitching_step2.csv"
df_training = pd.read_csv(filename4)
df_training_list = df_training["playerID"]

df_global = df_global[df_global['playerID'].isin(df_training_list)]
df_global.to_csv("../intermediate-steps/pitchingprediction_step1.csv", index=False)

sys.exit()