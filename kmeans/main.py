import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import adjusted_rand_score

from kmeans.kmeans import KMeans

def main():
    kmeans = KMeans()

    # points = np.random.randint(0,100,(100,2))
    data = make_blobs(n_samples=100, n_features=2, centers=3)
    points = data[0]

    kmeans.add_points(points)

    labels = kmeans.match()

    ari = adjusted_rand_score(data[1], labels)
    plt.scatter(points[:, 0], points[:, 1], c=labels)
    plt.scatter(kmeans.centers[:, 0], kmeans.centers[:, 1], c=range(len(kmeans.centers)), marker="+", s=200)

    plt.show()


if __name__ == "__main__":
    main()
