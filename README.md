# K-Means Clustering from Scratch

## Overview

This project implements the K-Means clustering algorithm from scratch using NumPy and Matplotlib. It demonstrates the ability to cluster randomly generated data points without relying on built-in clustering methods from scikit-learn.

The program generates synthetic data using scikit-learn's `make_blobs`, applies a custom K-Means algorithm to form clusters, and visualizes the results with Matplotlib.

## Features

- Implements K-Means clustering without external ML libraries
- Uses scikit-learn to generate sample data
- Visualizes clustering results using Matplotlib
- Step-by-step iterative updates to centroids

## How It Works

1. **Data Generation**: Scikit-learn's `make_blobs` is used to create synthetic datasets with a specified number of clusters.
2. **Initialization**: Randomly selects `k` data points as initial centroids.
3. **Assignment Step**: Each data point is assigned to the closest centroid.
4. **Update Step**: Centroids are recalculated as the mean of assigned points.
5. **Convergence Check**: Steps 3 and 4 repeat until centroids no longer change significantly.
6. **Visualization**: The final clusters and their centroids are plotted using Matplotlib.


## Setup
1. Install Python ^3.10, Poetry and poethepoet.
2. Clone this repository and cd into it.
3. Run poe setup to install the dependencies.
4. Finally run poe start.

## Alternatively

To run this project in a **Local** Python environment, follow these steps:

1. Install dependencies (if not already installed):
   ```bash
   pip install numpy matplotlib scikit-learn
   ```
2. Run the Python script:
   ```bash
   python k_means.py
   ```

## Example Output

The script produces a scatter plot of clustered data points, each color representing a separate cluster, with centroids marked for clarity.

## References

- [K-Means Clustering Explained](https://en.wikipedia.org/wiki/K-means_clustering)
- [Scikit-learn's ](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html)[`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html)
- [Understanding the K-Means Algorithm](https://towardsdatascience.com/k-means-clustering-explained-4528df86a120)

## Future Improvements

- Allow dynamic selection of `k` using the Elbow Method
- Optimize convergence using vectorized NumPy operations
- Compare performance with scikit-learn's `KMeans`

---

Enjoy clustering! 🚀

