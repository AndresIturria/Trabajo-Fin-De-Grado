import pandas as pd
import numpy as np
import sys

df = pd.read_csv("../intermediate-steps/batting_step2.csv")

# A tensorflow hay que pasarle un solo tipo de datos, por lo cual pasamos playerID a codificación one hot

# Pasar la columna playerID a nombre de columna
df_hot = pd.concat([
    df, pd.DataFrame(columns=df["playerID"].drop_duplicates())
], axis=1)

schema = df_hot.drop(df_hot.index)

# Poner un 1 en la columna que corresponde.
for player in df_hot["playerID"]:
    df_hot.loc[df_hot.playerID == player, player] = 1

df_hot.fillna(0, inplace=True)
df_hot.drop(["playerID"], 1, inplace=True)
df_hot.to_csv("../intermediate-steps/batting_step3.csv", index=False)

# Ahora los datos a predecir:
df_prediction = pd.read_csv("../intermediate-steps/battingprediction_step1.csv")
schema["playerID"] = df_prediction["playerID"]
schema["age"] = df_prediction["age"]
df_prediction = schema

for player in df_prediction["playerID"]:
    df_prediction.loc[df_prediction.playerID == player, player] = 1

df_prediction.fillna(0, inplace=True)
df_prediction.drop(["playerID", "points"], 1, inplace=True)

df_prediction.to_csv("../intermediate-steps/battingprediction_step2.csv", index=False)

# -----------------------------------------------------------------------------------------
# Ahora pitching
df2 = pd.read_csv("../intermediate-steps/pitching_step2.csv")

df_hot2 = pd.concat([
    df2, pd.DataFrame(columns=df2["playerID"].drop_duplicates())
], axis=1)

schema2 = df_hot2.drop(df_hot2.index)

# Poner un 1 en la columna que corresponde.
for player in df_hot2["playerID"]:
    df_hot2.loc[df_hot2.playerID == player, player] = 1

df_hot2.fillna(0, inplace=True)
df_hot2.drop(["playerID"], 1, inplace=True)
df_hot2.to_csv("../intermediate-steps/pitching_step3.csv", index=False)

# Ahora los datos a predecir:
df_prediction2 = pd.read_csv("../intermediate-steps/pitchingprediction_step1.csv")
schema2["playerID"] = df_prediction2["playerID"]
schema2["age"] = df_prediction2["age"]
df_prediction2 = schema2

for player in df_prediction2["playerID"]:
    df_prediction2.loc[df_prediction2.playerID == player, player] = 1

df_prediction2.fillna(0, inplace=True)
df_prediction2.drop(["playerID", "points"], 1, inplace=True)

df_prediction2.to_csv("../intermediate-steps/pitchingprediction_step2.csv", index=False)
sys.exit()