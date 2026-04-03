from sklearn import datasets  # load the Iris dataset (built-in to scikit-learn)
import matplotlib.pyplot as plt  # plotting library for creating charts

# Load Iris dataset as dict-like object
iris = datasets.load_iris()

# x: feature matrix (150 samples × 4 features)
# y: target labels (0=setosa, 1=versicolor, 2=virginica)
# species: readable names for target labels
x = iris.data
y = iris.target
species = iris.target_names

# SCATTER PLOT
# Plot petal length (x-axis) vs petal width (y-axis), colored by species
plt.figure(figsize=(8, 6))
for i in range(len(species)):
    plt.scatter(x[y == i, 2], x[y == i, 3], label=species[i])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Iris Dataset')
plt.legend()
plt.show()

# BAR PLOT
# Compute average petal length for each iris species and display in a bar chart
import numpy as np  # numerical computations
plt.figure(figsize=(8, 6))
avg_petal_length = [np.mean(x[y == i, 2]) for i in range(len(species))]
plt.bar(species, avg_petal_length)
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.title('Average Petal Length of Each Iris Species')
plt.show()

# HISTOGRAM
# Show distribution of petal width for each species using overlapping histograms
plt.figure(figsize=(8, 6))
for i in range(len(species)):
    plt.hist(x[y == i, 3], alpha=0.5, label=species[i])
plt.xlabel('Petal Width')
plt.ylabel('Frequency')
plt.title('Distribution of Petal Width for Each Iris Species')
plt.legend()
plt.show()

# Analysis comments:
# - Setosa is clearly separated from Versicolor and Virginica in petal features.
# - Virginica has the largest average petal length, then Versicolor, then Setosa.
# - Setosa has smaller petal width distribution; research can use these features for classification.

#SCATTER PLOT (Petal Length vs Sepal Length)
plt.figure(figsize=(8, 6))
for i in range(len(species)):
    plt.scatter(x[y == i, 2], x[y == i, 0], label=species[i])
plt.xlabel('Petal Length')
plt.ylabel('Sepal Length')
plt.title('Iris Dataset: Petal Length vs Sepal Length')
plt.legend()
plt.show()

# Analysis:
# - Setosa has shorter petal length and sepal length compared to Versicolor and Virginica.
# - Versicolor and Virginica have overlapping petal length and sepal length, making them harder to distinguish based on these features alone.