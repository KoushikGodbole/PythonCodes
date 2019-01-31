import operator
import math
def closestLocations(totalCrates, allLocations, truckCapacity):
    # WRITE YOUR CODE HERE
    temp = dict()
    sorted_temp = tuple()
    for i in range(totalCrates):
        x = allLocations[i]
        val = math.sqrt((x[0]*x[0]) + (x[1]*x[1]))
        temp[val] = x
        res = []
        for key in sorted(temp.keys()):
            res.append(temp[key])
    return res[:truckCapacity]



res = tuple()
res = closestLocations(3, [[1,2],[3,4],[1,-1]], 2)
print(res)