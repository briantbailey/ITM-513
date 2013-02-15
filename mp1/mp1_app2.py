# MP1 Application 2
# Brian T. Bailey

import random
import math

# Create 3 Lists of 100 Random Coordinates for x, y, z
# I have limited the range of coordinate values from -250 to 250
xL = [random.randint(-250, 250) for i in range(0, 100)]
yL = [random.randint(-250, 250) for i in range(0, 100)]
zL = [random.randint(-250, 250) for i in range(0, 100)]

# Create List of (x, y, z) coordinate tuples
threeSpace = zip(xL, yL, zL)

# Create Lists of tuples sorted in ascending order for x, y, z
xSortedSpace = sorted(threeSpace, key=lambda coordinate: coordinate[0])
ySortedSpace = sorted(threeSpace, key=lambda coordinate: coordinate[1])
zSortedSpace = sorted(threeSpace, key=lambda coordinate: coordinate[2])

# Store sorted list in a dictionary
sortedDict = {"xSorted": xSortedSpace, "ySorted": ySortedSpace, "zSorted": zSortedSpace}

# sort threeSpace list in ascending order by distance from origin
def distanceFromOrigin(point):
  d = math.sqrt((point[0] ** 2) + (point[1] ** 2) + (point[2] ** 2))
  return d

threeSpace.sort(key=distanceFromOrigin)
minCoord = threeSpace[0]
maxCoord = threeSpace[len(threeSpace) - 1]

# Print results to display
print "\nMP1 Application 2"
print "Brian T. Bailey\n"
print "Coordinates sorted by x ascending order:"
print "----------------------------------------------------------"
print sortedDict['xSorted'], "\n"
print "Coordinates sorted by y ascending order:"
print "----------------------------------------------------------"
print sortedDict['ySorted'], "\n"
print "Coordinates sorted by z in ascending order:"
print "----------------------------------------------------------"
print sortedDict['zSorted'], "\n"
print "Closest and Farthest Coordinates from the Origin:"
print "----------------------------------------------------------"
print "Coordinate closest to the origin:", minCoord
print "Coordinate farthest from the origin:", maxCoord, "\n"