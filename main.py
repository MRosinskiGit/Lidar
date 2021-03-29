import simulate_cloud
import csv
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from scipy.stats import norm



with open('LidarData.xyz', 'w', newline='\n') as csvfile:

    csvwriter = csv.writer(csvfile)

    cloud_points = simulate_cloud.generate_points_cylindrical(radius=10, height=10, move=[-5,-5,-5], num_points=100)
    for p in cloud_points:
        csvwriter.writerow(p)
    cloud_points = simulate_cloud.generate_points_vertical(width=10, height=10,move=[5,5,5],num_points=100)
    for p in cloud_points:
        csvwriter.writerow(p)
    cloud_points = simulate_cloud.generate_points_horizontal(length=10, depth=10,move=[0,0,-0],num_points=100)
    for p in cloud_points:
        csvwriter.writerow(p)

x_read, y_read, z_read, clusters = [], [], [], []

with open('LidarData.xyz', newline='') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for x2,y2,z2 in csvReader:
        x_read.append(float(x2))
        y_read.append(float(y2))
        z_read.append(float(z2))

x=tuple(x_read)
y=tuple(y_read)
z=tuple(z_read)
coord=list(zip(x,y,z))

clusterer=KMeans(n_clusters=3)
X_array = np.array(coord)

print(type(clusters))
clusterer.fit(X_array)
y_pred = clusterer.predict(X_array)
print("y_pred:")
print(y_pred)
print("X_array:")
print(X_array)
red = y_pred == 0
blue = y_pred == 1
cyan = y_pred == 2

ax = plt.axes(projection='3d')
ax.scatter(X_array[red, 0], X_array[red, 1], X_array[red, 2], c="r")
ax.scatter(X_array[blue, 0], X_array[blue, 1], X_array[blue, 2],c="b")
ax.scatter(X_array[cyan, 0], X_array[cyan, 1], X_array[cyan, 2],c="c")


# fig = plt.figure()

# ax.scatter(x, y, z, linewidth=0.5, );
#
# # plt.scatter(x, y)
#
# # # plt.plot(x_read2)
plt.show()
# #
# #



