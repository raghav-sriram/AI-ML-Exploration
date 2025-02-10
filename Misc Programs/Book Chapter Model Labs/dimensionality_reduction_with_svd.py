
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline

# Load the dataset
file_path = 'jobs_in_data.csv'  # Replace with the path to your dataset
data = pd.read_csv(file_path)

# Selecting numerical and categorical columns
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = data.select_dtypes(include=['object']).columns

# Creating a column transformer for preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
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
# pd.DataFrame(svd_data).to_csv('transformed_data.csv', index=False)

import matplotlib.pyplot as plt

# After applying TruncatedSVD...
svd_data = svd_pipeline.fit_transform(data)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(svd_data[:, 0], svd_data[:, 1])
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.title('2D representation of the Data using TruncatedSVD')
plt.show()
