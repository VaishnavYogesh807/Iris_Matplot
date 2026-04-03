# Iris_Matplot

## Purpose

The goal of this project is to look at the Iris dataset and compare the physical traits of different iris species side by side. The project shows how data visualization can help tell the difference between species by showing how measurements of petals and sepals can do this.

## Design & Implementation

The program follows a simple design:

* Load the dataset using `sklearn`
* Store feature data in `x` and species labels in `y`
* Use loops to separate data by species
* Generate visualizations using `matplotlib`

## Variables

* `x`: A 2D array containing measurements (sepal length, sepal width, petal length, petal width)
* `y`: A 1D array containing species labels (0, 1, 2)
* `species`: A list of species names corresponding to the labels

## Methods Used

* `plt.scatter()`: Creates a scatter plot to compare two features
* `plt.bar()`: Displays average values across species
* `plt.hist()`: Shows the distribution of a feature
* `np.mean()`: Calculates average values

## Limitations
* The dataset is small and already clean, so there was no need to clean it up first.
* Only basic charts and graphs were used; there was no advanced styling or interactivity.
* No user input or dynamic analysis; the results are always the same for the dataset

## Conclusion

This project primarily focuses on petal lengths across three different species, and also that petal measurements are superior to sepal measurements for differentiating iris species, highlighting the significance of feature selection in data analysis.
