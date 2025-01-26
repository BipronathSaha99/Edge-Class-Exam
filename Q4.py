print(
    " ==================== Task 1: Load Sepal Length and Sepal Width columns using NumPy =============="
)
import numpy as np

# Load the Iris dataset (make sure the dataset is available)
data = np.genfromtxt(
    "iris.csv", delimiter=",", skip_header=1
)  # Assuming the first row is header

# Extract sepal length and sepal width (assuming they are the first two columns)
sepal_length = data[:, 0]
sepal_width = data[:, 1]

print(sepal_length, sepal_width)
# task 2
print(" ==================== Task 2: Pandas Operations ==============")

import pandas as pd

# Load the Iris dataset using pandas (ensure the file path is correct)
try:
    df = pd.read_csv("iris.csv")
except FileNotFoundError:
    print("Error: The file 'iris.csv' was not found. Please check the file path.")
    exit()

# Check the first few rows to inspect the data
print("First few rows of the dataset:")
print(df.head())

# Check the data types to ensure columns are properly formatted
print("\nData types of the columns:")
print(df.dtypes)

# Check if the 'species' column contains valid species names
# and ensure no concatenated values are present
if (
    df["species"].str.contains("SetosaSetosa").any()
):  # A quick check for concatenated values
    print("\nFound concatenated 'species' values. Cleaning up the data...")
    # Split the concatenated string back to individual species
    species = df["species"].str.extract(r"(Setosa|Versicolor|Virginica)")
    df["species"] = species[0]

# Task 1: Calculate mean, median, and standard deviation for each feature
# First, check for any non-numeric columns or unexpected values
print("\nChecking for any non-numeric columns in the dataset:")
print(df.select_dtypes(exclude=["number"]).columns)

# Ensure numeric columns are handled correctly
mean_values = df.mean(
    numeric_only=True
)  # Specify numeric_only to only consider numeric columns
median_values = df.median(numeric_only=True)
std_dev_values = df.std(numeric_only=True)

print("\nMean values for numeric features:\n", mean_values)
print("\nMedian values for numeric features:\n", median_values)
print("\nStandard Deviation values for numeric features:\n", std_dev_values)

# Task 2: Group by species and calculate average sepal length and petal length
grouped = df.groupby("species")[["sepal_length", "petal_length"]].mean()
print("\nGrouped by species (average sepal and petal lengths):\n", grouped)

# Task 3: Filter rows where sepal length is greater than 5.0 cm
filtered_df = df[df["sepal_length"] > 5.0]
print("\nFiltered rows where sepal length > 5.0 cm:\n", filtered_df)
