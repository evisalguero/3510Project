import random
import math
import sys
import time
import timeit

# takes in file name from command line
#f = open("mat-test.txt")
def parseInputFile(filename):
    f = open(filename)
    #print(f.read())
    lines = f.readlines()
    listOfPoints = []
    for line in lines:
        lis = line.split()
        xVal = float(lis[1])
        yVal = float(lis[2])
        tupl = (xVal, yVal)
        listOfPoints.append(tupl)
        #print(xVal, yVal)
    f.close()
    return listOfPoints

listOfPoints = parseInputFile(sys.argv[1])    


#TODO: time comp calc distance vs store dist
#TODO: swap function 
#TODO: path generating function

# generate path
# given: list of points
# returns: path of points, path is of type list
def generatePath(listOfCities):
    #init steps
    currNode = listOfCities[0] # start node, just picked 1st one
    currX, currY = currNode
    totalCost = 0 
    listOfIndices = list(range(1, len(listOfCities))) 
    path = [currNode]
    for i in range(len(listOfCities)-1):
        randomNumber = random.choice(listOfIndices) # picking random node 
        listOfIndices.remove(randomNumber)
        connectingNode = listOfCities[randomNumber] 
        x, y = connectingNode
        distance = math.sqrt((x - currX)**2 + (y - currY)**2) # calculating distance 
        totalCost += distance
        path.append(connectingNode)
        currNode = connectingNode
    #now connect end point to start point
    firstX, firstY = path[0]
    lastX, lastY = path[len(listOfCities)-1]
    distance = math.sqrt((firstX - lastX)**2 + (firstY - lastY)**2) # calculating distance 
    totalCost += distance
    path.append(path[0])
    print(path)
    return(path)
    
samplePath = generatePath(listOfPoints)


pathDict = { "Edge1":2,
            "Edge2":3,
            "Edge3":4}



print("Length of path: " + (str) (len(listOfPoints)))

x1, y1 = listOfPoints[2]
x2, y2 = listOfPoints[1]

#distReal = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
#print(distReal)

start = time.time()
for x in range(5000):
    distReal = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
print("Time to calculate an value 5000 times: " + (str) (time.time() - start))

start = time.time()
for x in range(5000):
    pulledValue = pathDict.get("Edge1")
print("Time to retrieve an value 5000 times: " + (str) (time.time() - start))

start = time.time()
for x in range(5000):
    pathDict["Edge4"] = 5
print("Time to store an value 5000 times: " + (str) (time.time() - start))












