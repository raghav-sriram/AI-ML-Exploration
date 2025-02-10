# Raghav Sriram
# Period 6 ML Gabor
# Chapter 7

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import classification_report


f = "Cleaned_Housing_Association_Properties.csv"
dH = pd.read_csv(f)# Load


useless_columns = ["OBJECTID", "POSTCODE", "ADDRESS", "CONSTITUENCY", "WARD", "LSOA", "LSOA_CODE", "ROW_NUMBER",  "LATITUDE", "LONGITUDE", "EASTING", "NORTHING"]
data = dH.drop(columns=useless_columns) # Preprocessing

x_Hou = data.drop("FractionHAProperties", axis=1)
y_Hou = data["FractionHAProperties"] # Defining the target variable and features

X_train_housing, X_test_housing, y_train_housing, y_test_housing = train_test_split(x_Hou, y_Hou, test_size=0.3, random_state=42) # Split for test/train

classifiers_housing = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "Extra Trees": ExtraTreesClassifier(random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

m = {"Classifier": [], "Accuracy": [], "Precision": [], "Recall": [], "F1-Score": []}           #96

res = dict()

for name, clf in classifiers_housing.items():
    clf.fit(X_train_housing, y_train_housing)
    yH = clf.predict(X_test_housing)
    accuracy = accuracy_score(y_test_housing, yH)
    report = classification_report(y_test_housing, yH)
    res[name] = {"accuracy": accuracy, "report": report}
    precision, recall, f1, _ = precision_recall_fscore_support(y_test_housing, yH, average="weighted")
    m["Classifier"].append(name)
    m["Accuracy"].append(accuracy)
    m["Precision"].append(precision)
    m["Recall"].append(recall)
    m["F1-Score"].append(f1)
    
# Display
print()
for i, j in res.items():
    print(f"{i} Classifier:")
    print(f"Accuracy: {j['accuracy']}\n")

# Plotting the results
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("Performance Comparison of Classifiers")

axes[0, 0].bar(m["Classifier"], m["Accuracy"], color="skyblue")
axes[0, 0].set_title("Accuracy")
axes[0, 0].set_ylim([min(m["Accuracy"]) - 0.05, 1])

axes[0, 1].bar(m["Classifier"], m["Precision"], color="lightgreen")
axes[0, 1].set_title("Precision")
axes[0, 1].set_ylim([min(m["Precision"]) - 0.05, 1])

axes[1, 0].bar(m["Classifier"], m["Recall"], color="lightcoral")
axes[1, 0].set_title("Recall")
axes[1, 0].set_ylim([min(m["Recall"]) - 0.05, 1])

axes[1, 1].bar(m["Classifier"], m["F1-Score"], color="orchid")
axes[1, 1].set_title("F1-Score")
axes[1, 1].set_ylim([min(m["F1-Score"]) - 0.05, 1])

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()