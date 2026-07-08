# STEP 1: IMPORT LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:/Users/swati singh/Downloads/student_performance_dataset.csv")
print(df.head())

# STEP 3: SPLIT FEATURES & TARGET
X = df.drop("final_result", axis=1)
y = df["final_result"]

# STEP 4: TRAIN-TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# STEP 5: FEATURE SCALING
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

### PLOT
plt.figure(figsize=(6,4))
df["final_result"].value_counts().plot(kind="bar")
plt.title("Pass vs Fail Distribution")
plt.xlabel("Final Result")
plt.ylabel("Count")
plt.show()

# STEP 6: BUILD ANN MODEL
model = Sequential()

model.add(Dense(16, activation='relu', input_dim=7))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # binary classification

# STEP 7: COMPILE MODEL
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# STEP 8: TRAIN MODEL
model.fit(X_train, y_train, epochs=100, batch_size=2)

# STEP 9: EVALUATE MODEL
loss, accuracy = model.evaluate(X_test, y_test)
print("\nAccuracy:", accuracy)

# STEP 10: PREDICT
new_student = np.array([[5, 80, 6, 60, 3, 7, 1]])
new_student = scaler.transform(new_student)

prediction = model.predict(new_student)

print("\nPrediction (0=Fail, 1=Pass):", prediction)

# Convert probability to class
if prediction > 0.5:
    print("Result: PASS ✅")
else:
    print("Result: FAIL ❌")
