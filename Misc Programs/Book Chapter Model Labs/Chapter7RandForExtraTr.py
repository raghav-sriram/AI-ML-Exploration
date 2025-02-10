import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
file_path = 'jobs_in_data.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Creating a binary classification target based on the median salary
median_salary = data['salary_in_usd'].median()
data['high_salary'] = (data['salary_in_usd'] >= median_salary).astype(int)

# Selecting features for the model and encoding categorical variables
features = data.drop(columns=['work_year', 'salary_currency', 'salary', 'salary_in_usd', 'high_salary'])
label_encoder = LabelEncoder()
for column in features.select_dtypes(include=['object']).columns:
    features[column] = label_encoder.fit_transform(features[column])

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, data['high_salary'], test_size=0.3, random_state=42)

# Training the Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Training the Extra Trees Classifier
et_model = ExtraTreesClassifier(random_state=42)
et_model.fit(X_train, y_train)

# Predicting and evaluating the Random Forest Classifier
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
rf_report = classification_report(y_test, rf_predictions)

# Predicting and evaluating the Extra Trees Classifier
et_predictions = et_model.predict(X_test)
et_accuracy = accuracy_score(y_test, et_predictions)
et_report = classification_report(y_test, et_predictions)

# Display the results
print("Random Forest Classifier Accuracy:", rf_accuracy)
print("Random Forest Classification Report:\n", rf_report)
print("Extra Trees Classifier Accuracy:", et_accuracy)
print("Extra Trees Classification Report:\n", et_report)
