required libaray:

- Numpy
- Panda
- Scipy-learn
- Shapely
- geopy

1. Basic idea is loop all yards geo information to find the mini distance from given input(latitude, longitude)
2. Idea of optimize the solution is use DBSCAN clustering find the clusters, then compare with the given input(latitude, longitude)
with centroid of each cluster, find closet cluster,then find the most two closet location in that specific cluster