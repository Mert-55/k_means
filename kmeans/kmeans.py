import numpy as np
from numpy import array


class KMeans:
    def __init__(self):
        """
        Point Variations:
        CENTER = Have a unique designation and are changeable in position.
        REGULAR = Have no designation and are unchangeable in their position
                after they have been created
        """
        self._centers = None
        self._points = None
        self._k: int = 3

    @staticmethod
    def distance(point: array, centers: list[array]):
        """
        Calculate the euclidian distances of all centers to one point
        """
        return np.sqrt(np.sum((centers - point) ** 2, axis=1))

    def match(self, iteration_limit: int = 180):
        self._centers = np.random.uniform(
        np.amin(self._points, axis=0),
        np.amax(self._points, axis=0),
        size=(self._k, self._points.shape[1]),
        )

        y = []
        for _ in range(iteration_limit):
            # array of assignments of centers based on indices in place of points
            y = array(
                [
                    np.argmin(KMeans.distance(point, self._centers))
                    for point in self._points
                ]
            )

            # belonging_pts array in array with the length of k
            #cluster_indices = [choice for i in range(k) if (choice := np.argwhere(y == i))]
            cluster_indices = [choice for i in range(self._k) if (choice := np.argwhere(y == i)).size > 0]
            
            # if cluster amount > centers then some cluster dont have belonging data points
            cluster_centers = [
                center if len(indices) == 0 else np.mean(self._points[indices], axis=0)
                for i, indices in enumerate(cluster_indices)
                if (center := self._centers[i]) is not None
            ]

            cluster_centers = np.array(cluster_centers).squeeze()
            
            if np.max(self._centers - array(cluster_centers)) < 0.005:
                break

            self._centers = array(cluster_centers)

        return y

    def add_points(self, *pts) -> None:
        """
        add one or more points
        Condition:
            point must be either two or three dimensional
            the dimensions must be the same as all other points
        """
        for pt in pts:
            if self._points is None:
                self._points = array(pt)
                continue

            if pt.shape[1] != self._points[0].shape[1]:
                raise ValueError("dimension of point does not match rest")

            self._points.append(pt)


    @property
    def points(self):
        return np.concatenate((self._points, self._centers), axis=0)

    @property
    def regular_points(
        self,
    ):
        return self._points

    @property
    def centers(
        self,
    ):
        return self._centers
