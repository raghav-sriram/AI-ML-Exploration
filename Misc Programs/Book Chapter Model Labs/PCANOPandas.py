
import csv
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Function to load data from a CSV file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data_reader = csv.reader(file)
        data = list(data_reader)
        headers = data[0]
        rows = data[1:]
    return headers, np.array(rows)

# Function to identify numerical and categorical columns
def identify_column_types(headers, data):
    numerical_cols = []
    categorical_cols = []
    for i, header in enumerate(headers):
        try:
            data[:, i].astype(float)
            numerical_cols.append(i)
        except ValueError:
            categorical_cols.append(i)
    return numerical_cols, categorical_cols

# Load the dataset
file_path = 'jobs_in_data.csv'  # Replace with the path to your dataset
headers, data = load_data(file_path)

# Identifying numerical and categorical columns
numerical_cols, categorical_cols = identify_column_types(headers, data)

# Creating a column transformer for preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[('imputer', SimpleImputer(strategy='mean')), ('scaler', StandardScaler())]), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

# TruncatedSVD with an arbitrary number of components, e.g., 2 for visualization purposes
svd = TruncatedSVD(n_components=2)

# Creating a pipeline with preprocessing and TruncatedSVD
svd_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('svd', svd)])

# Fitting the pipeline to the data
svd_data = svd_pipeline.fit_transform(data)

# Optionally, you can save the transformed data to a new file
# np.savetxt('transformed_data.csv', svd_data, delimiter=',')
