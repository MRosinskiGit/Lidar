import simulate_cloud
import csv
from scipy.stats import norm
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':
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



x_read, y_read, z_read = [], [], []
clusters = []
with open('LidarData.xyz', newline='') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    for x2,y2,z2 in csvReader:
        # x_read.append(float(row[0]))
        # y_read.append(float(row[1]))
        # z_read.append(float(row[2]))
        #print(float(x2),float(y2),float(z2))
        x_read.append(float(x2))
        y_read.append(float(y2))
        z_read.append(float(z2))



print(x_read)
print(y_read)
print(z_read)
# x=list(x_read)
# y=list(y_read)
x=tuple(x_read)
y=tuple(y_read)
z=tuple(z_read)
print(x)
print(y)
print(z)
# print(type(x))
#print(y)
 #cluster = zip(x_read, y_read)
# #clusters.extend(cluster)
#
# #x, y = zip(*clusters)
#
clusters=zip(x,y)

clusterer=KMeans(n_clusters=3)

X_array = np.array(clusters)

print(type(clusters))
#clusterer.fit(X_array)
#y_pred = clusterer.predict(X_array)

#print(y_pred)




# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter(x, y, z, linewidth=0.5, );
#
# # plt.scatter(x, y)
#
# # # plt.plot(x_read2)
# plt.show()
# #
# #



