import random
import math
import sys
import time
import timeit

totalSwaps = 0
totalNonSwaps = 0
totalEdgeCases = 0
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

start = time.time()
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
    #print(len(listOfIndices))
    path = [currNode]
    for i in range(len(listOfCities)-1):
        randomNumber = random.choice(listOfIndices) # picking random node 
        listOfIndices.remove(randomNumber)
        connectingNode = listOfCities[randomNumber] 
        currX, currY = currNode
        x, y = connectingNode
        distance = int(math.sqrt((x - currX)**2 + (y - currY)**2)) # calculating distance 
        totalCost += distance
        path.append(connectingNode)
        currNode = connectingNode
    #now connect end point to start point
    firstX, firstY = path[0]
    lastX, lastY = path[len(listOfCities)-1]
    distance = int(math.sqrt((firstX - lastX)**2 + (firstY - lastY)**2)) # calculating distance 
    totalCost += distance
    path.append(path[0])
    print(path)
    print(len(path))
    return path, totalCost
    
samplePath,pathCost = generatePath(listOfPoints)
print("Initial path cost: " + (str) (pathCost))

#Swaps two random nodes in a list
#Given: a path/list of points, totalCost of that path/list of points
#Return: the new path (or old path if the new path was less efficient), the total cost of the path
def swapNodes(listOfCities, totalCost):
    #print("length of listOfCities: " + (str) (len(listOfCities)))
    randomIndex = random.randrange(len(listOfCities) - 1)
    randomIndex2 = random.randrange(len(listOfCities)- 1)
    
    while randomIndex2 == randomIndex:
        randomIndex2 = random.randrange(len(listOfCities)- 1)
    
    # picking random node
    global totalSwaps
    global totalNonSwaps
    #################################################################################################### 
    #Attempting to swap nodes B and E in list [A, B, C, ... D, E, F]
    #so that it becomes [A, E, C, ... D, B, F]
    if (randomIndex == 0):
        previousNode1 = listOfCities[len(listOfCities) - 2]
        xA, yA = previousNode1
    else:
        previousNode1 = listOfCities[randomIndex - 1]
        xA, yA = previousNode1
    
    swapNode = listOfCities[randomIndex]
    xB, yB = swapNode

    nextNode1 = listOfCities[randomIndex + 1]
    xC, yC = nextNode1
    
    if (randomIndex2 == 0):
        previousNode2 = listOfCities[len(listOfCities) - 2]
        xD, yD = previousNode2
    else:
        previousNode2 = listOfCities[randomIndex2 - 1]
        xD, yD = previousNode2
    
    swapNode2 = listOfCities[randomIndex2]
    xE, yE = swapNode2
    
    nextNode2 = listOfCities[randomIndex2 + 1]
    xF, yF = nextNode2
    
    
    #Calculate new and old edge costs
    newEdge1 = int(math.sqrt((xE - xA)**2 + (yE - yA)**2))
    newEdge2 = int(math.sqrt((xC - xE)**2 + (yC - yE)**2))
    newEdge3 = int(math.sqrt((xB - xD)**2 + (yB - yD)**2))
    newEdge4 = int(math.sqrt((xF - xB)**2 + (yF - yB)**2))
    
    oldEdge1 = int(math.sqrt((xB - xA)**2 + (yB - yA)**2))
    oldEdge2 = int(math.sqrt((xC - xB)**2 + (yC - yB)**2))
    oldEdge3 = int(math.sqrt((xE - xD)**2 + (yE - yD)**2))
    oldEdge4 = int(math.sqrt((xF - xE)**2 + (yF - yE)**2))
    
    #Compare total cost of new edges to old edges
    newTotal = newEdge1 + newEdge2 + newEdge3 + newEdge4
    oldTotal = oldEdge1 + oldEdge2 + oldEdge3 + oldEdge4
    if (newTotal) < (oldTotal):
        #if the new edges have a lower cost than the old ones, swap the nodes
        if (randomIndex == 0):
            listOfCities[randomIndex] = swapNode2
            listOfCities[len(listOfCities) - 1] = swapNode2
            listOfCities[randomIndex2] = swapNode
        elif (randomIndex2 == 0):
            listOfCities[randomIndex2] = swapNode
            listOfCities[len(listOfCities) - 1] = swapNode
            listOfCities[randomIndex] = swapNode2
        else:
            listOfCities[randomIndex] = swapNode2
            listOfCities[randomIndex2] = swapNode
        newTotalCost = totalCost - oldTotal + newTotal
        print("Node at index %s was swapped with node at index %s" % (randomIndex, randomIndex2))
        print("Old total cost: %s" % (totalCost))
        print("New total cost: %s" % (newTotalCost))
        totalSwaps = totalSwaps + 1
        return listOfCities, newTotalCost
        
    else:
        #print("Node at index %s was not swapped with node at index %s, cost stayed at %s" % (randomIndex, randomIndex + 1, totalCost))
        totalNonSwaps = totalNonSwaps + 1
        return listOfCities, totalCost
    
    


for x in range(200):
    samplePath, pathCost = swapNodes(samplePath, pathCost)
    print(samplePath)




print("Time to run the algorithm 2,000 times: " + (str) (time.time() - start) + " seconds")
print("Final path cost: " + (str) (pathCost))
print("Total # of swaps: " + (str) (totalSwaps))
print("Total # of nonswaps: " + (str) (totalNonSwaps))


# calculate temperature function, supposed to simulate cooling
def calcTemp(iteration, maxTemp):
    tempChange = 3.5
    temp = maxTemp - (iteration*tempChange)
    return temp


# Simulated annealing function
# Given: list of points(a path), number of iterations, temperature
# Returns: best path within number of iterations 
def simulatedAnnealing(listOfCities, maxIterations, maxTemp):
    print("running sim")
    currList, currCost = generatePath(listOfCities) # initial random path 
    bestList, bestCost = currList, currCost
    for i in range(1, maxIterations):
        #print(currCost)
        ithList, ithCost = swapNodes(currList, currCost) # uses swap function
        currTemp = calcTemp(i, maxTemp) # uses temperature function
        #print(currTemp)
        #print(math.exp((currCost-ithCost)/currTemp))
        if (ithCost <= currCost):
            currList, currCost = ithList, ithCost
            if (ithCost < bestCost):
                bestList, bestCost = ithList, ithCost
        elif ((math.exp((currCost-ithCost)/currTemp)) > random.random()): #acceptance probability, random.random gives probabilites 
            print(math.exp((currCost-ithCost)/currTemp))
            currList, currCost = ithList, ithCost
            print("randomly selected intermediate worse path")
            #print("iteration: ", i)
            #print("currtemp: ", currTemp)
            #print("cost", currCost, "icost", ithCost)
        else:
            #print("else block")
            continue

    return bestList, bestCost



#bestResult, bestResultCost = simulatedAnnealing(listOfPoints, 2000, 10000)    
#print("Time to run the algorithm 2000 times: " + (str) (time.time() - start) + " seconds")
#print(bestResult, bestResultCost)
#print("Total # of swaps: " + (str) (totalSwaps))
#print("Total # of nonswaps: " + (str) (totalNonSwaps))

      
      
      
      
      
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










