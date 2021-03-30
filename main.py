import simulate_cloud
import csv
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from scipy.stats import norm


with open('LidarData.xyz', 'w', newline='\n') as csvfile:                   #otwórz plik i wygeneruj do niego dane

    csvwriter = csv.writer(csvfile)

    cloud_points = simulate_cloud.generate_points_cylindrical(radius=100, height=100, move=[-90,-90,-90], num_points=1000)
    for p in cloud_points:
        csvwriter.writerow(p)
    cloud_points = simulate_cloud.generate_points_vertical(width=100, height=100,move=[0,0,0],num_points=1000)
    for p in cloud_points:
        csvwriter.writerow(p)
    cloud_points = simulate_cloud.generate_points_horizontal(length=100, depth=100,move=[90,90,90],num_points=1000)
    for p in cloud_points:
        csvwriter.writerow(p)

x_read, y_read, z_read, clusters = [], [], [], []

with open('LidarData.xyz', newline='') as csvDataFile:                  #odczytaj dane z pliku
    csvReader = csv.reader(csvDataFile)
    for x2,y2,z2 in csvReader:
        #print(x2,y2,z2)
        x_read.append(float(x2))                                        #przerzutuj odczytane stringi na flaot
        y_read.append(float(y2))
        z_read.append(float(z2))

x=tuple(x_read)                                                     #konwersja z list do tuple
y=tuple(y_read)
z=tuple(z_read)
coord=list(zip(x,y,z))                                               #stworz zip z koordynatów x,y,z

clusterer=KMeans(n_clusters=3)                                          #klasteryzacja punktów
X_array = np.array(coord)

clusterer.fit(X_array)
y_pred = clusterer.predict(X_array)

red = y_pred == 0
blue = y_pred == 1
cyan = y_pred == 2

ax = plt.axes(projection='3d')                                              #wizualizacja punktów w 3D
ax.scatter(X_array[red, 0], X_array[red, 1], X_array[red, 2], c="r")
ax.scatter(X_array[blue, 0], X_array[blue, 1], X_array[blue, 2],c="b")
ax.scatter(X_array[cyan, 0], X_array[cyan, 1], X_array[cyan, 2],c="c")
plt.show()

cluster1_x,cluster1_y,cluster1_z = [], [], []
licznik=0

for val in range(len(y_pred)):                                              #podział klastrów na zmienne x,y,z (klaster 1)
    if y_pred[val] == 0:
        # print(val)
        cluster1_x.append(coord[val][0])
        cluster1_y.append(coord[val][1])
        cluster1_z.append(coord[val][2])
        licznik += 1

cluster2_x,cluster2_y,cluster2_z = [], [], []
licznik=0

for val in range(len(y_pred)):                                              #podział klastrów na zmienne x,y,z (klaster 2)
    if y_pred[val] == 0:
        # print(val)
        cluster2_x.append(coord[val][0])
        cluster2_y.append(coord[val][1])
        cluster2_z.append(coord[val][2])
        licznik += 1

cluster3_x,cluster3_y,cluster3_z = [], [], []
licznik=0

for val in range(len(y_pred)):                                             #podział klastrów na zmienne x,y,z (klaster 3)
    if y_pred[val] == 0:
        # print(val)
        cluster3_x.append(coord[val][0])
        cluster3_y.append(coord[val][1])
        cluster3_z.append(coord[val][2])
        licznik += 1


# ax.scatter(cluster1_x, cluster1_y, cluster1_z, c="r")
# ax.scatter(cluster1_x, cluster1_y, cluster1_z, c="r")
# ax.scatter(cluster1_x, cluster1_y, cluster1_z, c="r")

# plt.show()

losulosu = random.randint(0,len(cluster1_x))
losowy_punkt_klaster1_1 = [cluster1_x[losulosu], cluster1_y[losulosu], cluster1_z[losulosu]]        #losowanie 3 punktów z klastra

losulosu = random.randint(0,len(cluster1_x))
losowy_punkt_klaster1_2 = [cluster1_x[losulosu], cluster1_y[losulosu], cluster1_z[losulosu]]

losulosu = random.randint(0,len(cluster1_x))
losowy_punkt_klaster1_3 = [cluster1_x[losulosu], cluster1_y[losulosu], cluster1_z[losulosu]]

VectA = np.subtract(losowy_punkt_klaster1_1,losowy_punkt_klaster1_3)                            #odejmowanie wetkrów
VectB = np.subtract(losowy_punkt_klaster1_2,losowy_punkt_klaster1_3)

VectUa = VectA/np.linalg.norm(VectA)                                                            #obliczanie W
VectUb = VectB/np.linalg.norm(VectB)
W = np.cross(VectUa,VectUb)

D=np.sum(np.multiply(W, losowy_punkt_klaster1_3))                                                 #obliczenie D
np.subtract(losowy_punkt_klaster1_1,losowy_punkt_klaster1_3)
W=list(W)
for temp in range(len(cluster1_x)-1):                                                  #stworzenie listy W do obliczania dystaunsu
    W.append(W)


distance = (np.add((np.multiply(coord,W)),D)) #
print(distance)
