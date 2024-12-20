from typing import Any, get_args, get_origin, NewType, Union
import random
from math import sqrt

OK = NewType("OK", bool)

def elect_table(
    points, random_election=False
) -> None | dict[str, list[str] | list[float]]:
    cluster_designations = [cluster_point[0] for cluster_point in points.cluster_points]

    x = []
    y = []
    [(x.append(pt[0]), y.append(pt[1])) for pt in points.regular_points]

    if len(cluster_designations) > len(x):
        return None

    cluster_assignment = []
    for designation in cluster_designations:
        cluster_assignment.append(designation)

    remaining_assignments = [
        random.choice(cluster_designations)
        for _ in range(len(points.regular_points) - len(cluster_designations))
    ]

    cluster_assignment.extend(remaining_assignments)
    random.shuffle(cluster_assignment)

    return {"x": x, "y": y, "cluster_election": cluster_assignment}