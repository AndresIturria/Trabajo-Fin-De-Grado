import sys
import time
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

start = time.time()
df = pd.read_csv("../intermediate-steps/pitching_step3.csv")
df2 = pd.read_csv("../intermediate-steps/pitchingprediction_step2.csv")

labels = df.pop("points")
features = tf.convert_to_tensor(df)

# Number of features in the training set + 1 for the input layer
# Hidden layer: Training Data Samples/Factor * (Input Neurons + Output Neurons)
factor = 1
inputlayer = len(df.columns) + 1
hiddenLayer = len(df) / (factor * (inputlayer + 1))
print(inputlayer)
print(hiddenLayer)

l0 = tf.keras.layers.Dense(units=inputlayer, activation='relu')
l1 = tf.keras.layers.Dense(units=hiddenLayer, activation='relu')
l2 = tf.keras.layers.Dense(units=1)

model = tf.keras.Sequential([l0, l1, l2])
model.compile(
    loss='mse',
    optimizer='adam',
    metrics=['mse']
)
print("Started training the model")
history = model.fit(features, labels, epochs=500, verbose=False)
print("Finished training the model")

x = model.predict(df2)
y = pd.DataFrame(x)


df3 = pd.read_csv("../intermediate-steps/pitchingprediction_step1.csv")
df3["points"] = y[0]
df3.sort_values(by=["points"], ascending=False, inplace=True)
df3.to_csv("../finished-data/training_pitch.csv", index=False)

end = time.time()
print(end - start)
sys.exit()
