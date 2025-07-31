# iris_analysis.py
import pandas as pd; print(pd.__version__)

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Dataset with Error Handling
def load_iris_data():
    try:
        iris = load_iris(as_frame=True)
        df = iris.frame
        print("✅ Dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

# Main analysis and visualization function
def analyze_and_visualize():
    df = load_iris_data()
    if df is None:
        return

    # Explore the dataset
    print("\n🔍 First 5 rows of the dataset:")
    print(df.head())

    print("\n📋 Dataset Info:")
    print(df.info())

    print("\n🧼 Missing Values:")
    print(df.isnull().sum())

    print("\n📊 Descriptive Statistics:")
    print(df.describe())

    # Add species column
    df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    print("\n📊 Grouped Means by Species:")
    print(df.groupby('species').mean())

    # Set style
    sns.set(style="whitegrid")

    # Simulate time series
    df['index'] = range(len(df))

    # Line Chart
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='index', y='sepal length (cm)', hue='species')
    plt.title("Line Chart: Sepal Length over Index")
    plt.xlabel("Index (simulated time)")
    plt.ylabel("Sepal Length (cm)")
    plt.legend(title='Species')
    plt.show()

    # Bar Chart
    plt.figure(figsize=(7, 5))
    sns.barplot(data=df, x='species', y='petal length (cm)', ci=None)
    plt.title("Bar Chart: Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.show()

    # Histogram
    plt.figure(figsize=(7, 5))
    sns.histplot(df['sepal width (cm)'], bins=15, kde=True, color='skyblue')
    plt.title("Histogram: Sepal Width Distribution")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title='Species')
    plt.show()

# Run the analysis
if __name__ == "__main__":
    analyze_and_visualize()
