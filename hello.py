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


#TODO: time comp calc distance vs store dist Edit: Finished!
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
    return path, totalCost
    
samplePath,pathCost = generatePath(listOfPoints)


#Swaps two random nodes in a list
#Given: a path/list of points, totalCost of that path/list of points
#Return: the new path (or old path if the new path was less efficient), the total cost of the path
def swapNodes(listOfCities, totalCost):
    randomIndex = random.randrange(len(listOfCities))# picking random node
    if randomIndex == (len(listOfCities)-1) or randomIndex == (len(listOfCities)-2):
        print(randomIndex)
    else:
        #Note: in a subset of the list with nodes [A, B, C, D], we are
        #swapping nodes B and C so we are checking the cost of the new list [A, C, B, D]
        #Obtain coordinates
        previousNode = listOfCities[randomIndex - 1]
        xA, yA = previousNode
        swapNode = listOfCities[randomIndex]
        xB, yB = swapNode
        swapNode2 = listOfCities[randomIndex + 1]
        xC, yC = swapNode2
        nextNode = listOfCities[randomIndex + 2]
        xD, yD = nextNode
        #Calculate new and old edge costs
        newEdge1 = int(math.sqrt((xC - xA)**2 + (yC - yA)**2))
        newEdge2 = int(math.sqrt((xD - xB)**2 + (yD - yB)**2))
        oldEdge1 = int(math.sqrt((xB - xA)**2 + (yB - yA)**2))
        oldEdge2 = int(math.sqrt((xD - xC)**2 + (yD - yC)**2))
        #Compare total cost of new edges to old edges
        if (newEdge1 + newEdge2) < (oldEdge1 + oldEdge2):
            #if the new edges have a lower cost than the old ones, swap the nodes
            listOfCities[randomIndex] = swapNode2
            listOfCities[randomIndex] = swapNode
            newTotalCost = totalCost - oldEdge1 - oldEdge2 + newEdge1 + newEdge2
            print("Node at index %s was swapped with node at index %s" % (randomIndex, randomIndex + 1))
            print("Old total cost: %s" % (totalCost))
            print("New total cost: %s" % (newTotalCost))
            
        else:
            print("Node at index %s was not swapped with node at index %s, cost stayed at %s" % (randomIndex, randomIndex + 1, totalCost))
    newListOfCities = listOfCities
    
    
    return newListOfCities



swapNodes(samplePath, pathCost)




"""
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
"""










