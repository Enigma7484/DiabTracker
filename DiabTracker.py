# importing dependencies

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('diabetes.csv')

pd.read_csv
# printing the first 5 rows of the dataset
print(diabetes_dataset.head())
# printing the number of rows and columns in this dataset
print(diabetes_dataset.shape)

# getting the statistical measures of the data
print(diabetes_dataset.describe())
print(diabetes_dataset['Outcome'].value_counts())

# 0 -> Non-Diabetic 1 -> Diabetic
print(diabetes_dataset.groupby('Outcome').mean())

# separating the data and labels
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

# Data Standardization
scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)
print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

# Train Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

# Training the Model
classifier = svm.SVC(kernel='linear')
# Training the Support Vector Machine Classifer
classifier.fit(X_train, Y_train)

# Model Evaluation
# AccuracyScore
# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
