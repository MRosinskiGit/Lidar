import simulate_cloud
from csv import writer, reader
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':
    with open('LidarData.csv', 'w', encoding='utf-8', newline='\n') as csvfile:

        csvwriter = writer(csvfile)

        cloud_points = simulate_cloud.generate_points_cylindrical(radius=10, height=10, move=[-5,-5,-5], num_points=100)
        for p in cloud_points:
            csvwriter.writerow(p)
        cloud_points = simulate_cloud.generate_points_vertical(width=10, height=10,move=[5,5,5],num_points=100)
        for p in cloud_points:
            csvwriter.writerow(p)
        cloud_points = simulate_cloud.generate_points_horizontal(length=10, depth=10,move=[0,0,-0],num_points=100)
        for p in cloud_points:
            csvwriter.writerow(p)


data =reader(open('LidarData.csv', 'r'), delimiter=",", quotechar='|')
x_read, y_read, z_read = [], [], []
clusters = []

for row in data:
    x_read.extend([row[0]])
    y_read.extend([row[1]])
    z_read.extend([row[2]])




#cluster = zip(x_read, y_read)
#clusters.extend(cluster)

#x, y = zip(*clusters)

#plt.figure()
#plt.scatter(x_read, z_read, 'bo')
# x_read2=np.array(x_read)
# x_read2=abs(x_read2)
# plt.plot(x_read2)
# plt.show()





