# 🎓 Student Performance Prediction using Artificial Neural Networks (ANN)

## 📌 Project Overview

This project predicts whether a student will pass or fail using an Artificial Neural Network (ANN). The model is built using TensorFlow and Keras, and it learns from student-related features such as study hours, attendance, assignments, exam scores, and extra classes.

---

## 🎯 Objectives

* Predict student performance using deep learning.
* Learn how Artificial Neural Networks solve classification problems.
* Understand data preprocessing, feature scaling, model training, and prediction.

---

## 📂 Dataset

* **Dataset Name:** `student_performance_dataset.csv`
* **Target Variable:** `final_result`
* **Problem Type:** Binary Classification (Pass / Fail)

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* TensorFlow
* Keras

---

## 📊 Project Workflow

### 1. Data Loading

* Loaded the student performance dataset using Pandas.

### 2. Data Preparation

* Split the dataset into input features and target variable.
* Divided the data into training and testing sets.
* Applied feature scaling using StandardScaler.

### 3. Model Building

* Built an Artificial Neural Network with:

  * Input Layer
  * Two Hidden Layers (ReLU Activation)
  * Output Layer (Sigmoid Activation)

### 4. Model Training

* Compiled the model using the Adam optimizer and Binary Crossentropy loss function.
* Trained the model for 100 epochs.

### 5. Model Evaluation

* Evaluated the model using classification accuracy.
* Predicted whether a new student would pass or fail.

### 6. Visualization

* Pass vs Fail Distribution
* Training Accuracy over Epochs

---

## 📈 Results

The ANN model successfully learned the relationship between student features and final results. It can predict whether a student is likely to pass or fail based on the input values.

---

## 📸 Project Visualizations

### Pass vs Fail Distribution

*(Add the screenshot from the `images` folder.)*

### Training Accuracy

*(Add the training accuracy graph here.)*

---

## 📁 Project Structure

```text
Student-Performance-Prediction-ANN/
│── data/
│── images/
│── ANN_Model.py
│── README.md
│── requirements.txt
│── .gitignore
└── LICENSE
```

---

## 🚀 Future Improvements

* Train the model on a larger real-world dataset.
* Compare ANN with Logistic Regression and Random Forest.
* Tune hyperparameters for better performance.
* Deploy the model as a web application using Streamlit.

---

## 👩‍💻 Author

**Swati Singh**

Aspiring Data Analyst | Python | SQL | Excel | Power BI | Machine Learning
