import math
def ClassifyPoint(points,p,k):
    distance = []
    for group in points:
        for features in points[group]:
            euclidean_distance = math.sqrt((features[0]-p[0])**2 +(features[1]-p[1])**2)
            distance.append((euclidean_distance,group))
    distance.sort(key= lambda x: x[0])
    distance = distance[0:k]
    freq1,freq2 = 0,0
    for d in distance:
        freq1 += int(d[1]==0)
        freq2 += int(d[1]==1)
    return int(freq1<freq2)

points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
              1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]}
p =(2.5,7)
k = 3
print ClassifyPoint(points,p,k)


