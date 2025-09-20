# Task 1: Load and Explore the Dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame  # convert to DataFrame directly
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Dataset file not found!")
except OSError as e:
    print(f"OS error: {e}")

# Display first few rows
print("First 5 rows of dataset:")
print(df.head(), "\n")

# Explore structure
print("Data types and non-null counts:")
print(df.info(), "\n")

print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# Clean dataset (Iris has no missing values, but let's handle just in case)
df = df.dropna()

# Task 2: Basic Data Analysis
print("Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Grouping by species and computing mean of numerical features
group_means = df.groupby("target").mean()
print("Mean values per species:")
print(group_means, "\n")

# Add species names instead of numeric codes
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))

# Task 3: Data Visualization

# 1. Line chart (fake time series: index as time)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length over Index (as Time)")
plt.xlabel("Index (as time)")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Bar Chart: Avg Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
