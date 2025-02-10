import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def apply_pca(file_path, n_components=None):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Separate features and target if necessary (optional)
    # If the dataset has a target column, replace 'target_column' with its name
    # y = data['target_column']
    # X = data.drop('target_column', axis=1)

    # For this dataset, consider all columns as features
    X = data

    # Identify numerical and categorical columns
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    # Create a preprocessing pipeline
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  # Impute missing values
        ('scaler', StandardScaler())                 # Standardize numeric features
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),  # Impute missing values
        ('encoder', LabelEncoder())  # Encode categorical features
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Preprocessing the data
    X_preprocessed = preprocessor.fit_transform(X)

    # Apply PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(X_preprocessed)

    # Display results
    print("Original shape:", X.shape)
    print("Transformed shape:", principal_components.shape)
    print("Explained variance ratio:", pca.explained_variance_ratio_)

    return principal_components, pca.explained_variance_ratio_

# Example usage
file_path = 'jobs_in_data.csv'  # Change to your dataset path
n_components = 2  # Change the number of components as needed
transformed_data, variance_ratio = apply_pca(file_path, n_components)
