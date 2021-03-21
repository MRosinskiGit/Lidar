import simulate_cloud
from csv import writer

if __name__ == '__main__':
    cloud_points = simulate_cloud.generate_points_cylindrical(radius=50, height=200, concentration=1, num_points=10000)
    with open('LidarData.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:

        csvwriter = writer(csvfile)
        for p in cloud_points:
            csvwriter.writerow(p)
            #print(p)


