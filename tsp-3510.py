import random
import math
import sys
import time
import timeit
import copy

totalSwaps = 0
totalNonSwaps = 0
totalEdgeCases = 0
timeLimit = int(sys.argv[3])
# takes in file name from command line
#f = open("mat-test.txt")
def parseInputFile(filename):
    f = open(filename)
    #print(f.read())
    lines = f.readlines()
    listOfPoints = []
    node_IDs = {}
    for line in lines:
        lis = line.split()
        xVal = float(lis[1])
        yVal = float(lis[2])
        tupl = (xVal, yVal)
        listOfPoints.append(tupl)
        node_IDs[tupl] = lis[0] # key=city, value=id number
        #print(xVal, yVal)
    f.close()
    return listOfPoints, node_IDs



start = time.time()
listOfPoints, node_IDs = parseInputFile(sys.argv[1])    



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
        x, y = connectingNode
        distance = int(math.sqrt((x - currX)**2 + (y - currY)**2)) # calculating distance 
        totalCost += distance
        path.append(connectingNode)
        currNode = connectingNode
        currX, currY = currNode
    #now connect end point to start point
    firstX, firstY = path[0]
    lastX, lastY = path[len(listOfCities)-1]
    distance = int(math.sqrt((firstX - lastX)**2 + (firstY - lastY)**2)) # calculating distance 
    totalCost += distance
    path.append(path[0])
    #print(path)
    #print(len(path))
    return path, totalCost
    

def calcCost(path):
    totalCost = 0
    #print(len(path))
    for i in range(0, len(path)-1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        addedCost = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
        totalCost = totalCost + addedCost
    return totalCost


#Swaps two random nodes in a list
#Given: a path/list of points, totalCost of that path/list of points
#Return: the new path (or old path if the new path was less efficient), the total cost of the path
def swapNodes(listOfCities, totalCost):
    listOfCities = listOfCities[:-1]
    #print("length of listOfCities: " + (str) (len(listOfCities)))
    randomIndex = random.randrange(0, len(listOfCities))
    randomIndex2 = random.randrange(0, len(listOfCities))
    
    while randomIndex2 == randomIndex:
        randomIndex2 = random.randrange(0, len(listOfCities))
    
    if randomIndex > randomIndex2:
        temp = randomIndex2
        randomIndex2 = randomIndex
        randomIndex = temp
    # print(randomIndex, randomIndex2, randomIndex2-randomIndex)
    # picking random node
    global totalSwaps
    global totalNonSwaps
    global totalEdgeCases

    def nodeDist(node1, node2):
        x1, y1 = node1
        x2, y2 = node2
        dist = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
        return dist
    numCities = len(listOfCities)
    #################################################################################################### 
    #Attempting to swap nodes B and C in list [A, B, C, D, ... E, F]
    #so that it becomes [A, C, B, D, ... E, F]
    if ((randomIndex2 - randomIndex) == 1 or (randomIndex == 0 and randomIndex2 == numCities-1)):
        if randomIndex2 == numCities-1:
            temp = randomIndex2
            randomIndex2 = randomIndex
            randomIndex = randomIndex2
        previousNode = listOfCities[randomIndex - 1]
        swapNode = listOfCities[randomIndex]
        swapNode2 = listOfCities[randomIndex2]
        nextNode = listOfCities[randomIndex2 + 1]
        
        #old: previousNode, swapNode, swapNode2, nextNode
        #new: previousNode, swapNode2, swapNode, nextNode
        oldEdge1 = nodeDist(previousNode, swapNode)
        oldEdge2 = nodeDist(swapNode2, nextNode)        
        newEdge1 = nodeDist(previousNode, swapNode2)
        newEdge2 = nodeDist(swapNode, nextNode)

        
        newTotal = newEdge1 + newEdge2
        oldTotal = oldEdge1 + oldEdge2
        
        # if (newTotal) < (oldTotal):
        listOfCities[randomIndex] = swapNode2
        listOfCities[randomIndex2] = swapNode
            
        newTotalCost = totalCost - oldTotal + newTotal
        

    elif ((randomIndex2 - randomIndex) == 2 or (randomIndex == 1 and randomIndex2 == numCities-1) or (randomIndex == 0 and randomIndex2 == numCities-2)):
        if randomIndex2 == numCities-1 or randomIndex2 == numCities-2:
            temp = randomIndex2
            randomIndex2 = randomIndex
            randomIndex = randomIndex2
        #Attempting to swap nodes B and D in list [A, B, C, D, E, F, ...]
        #so that it becomes [A, D, C, B, E, F, ...]
        previousNode1 = listOfCities[randomIndex - 1]
        swapNode = listOfCities[randomIndex]
        swapNode2 = listOfCities[randomIndex2]
        nextNode2 = listOfCities[randomIndex2 + 1]
        

        
        #old: previousNode1, swapNode, middleNode, swapNode2, nextNode2
        #new: previousNode1, swapNode2, middleNode, swapNode, nextNode2
        #Calculate new and old edge costs
        oldEdge1 = nodeDist(previousNode1, swapNode)
        oldEdge2 = nodeDist(swapNode2, nextNode2)
        newEdge1 = nodeDist(previousNode1, swapNode2)
        newEdge2 = nodeDist(swapNode, nextNode2)
        

        
        #Compare total cost of new edges to old edges
        newTotal = newEdge1 + newEdge2
        oldTotal = oldEdge1 + oldEdge2
        # print("NewEdge1 (AE): " + (str) (newEdge1))
        # print("NewEdge2 (EC): " + (str) (newEdge2))
        # print("NewEdge3 (DB): " + (str) (newEdge3))
        # print("NewEdge4 (BF): " + (str) (newEdge4))
        # print("OldEdge1 (AB): " + (str) (oldEdge1))
        # print("OldEdge2 (BC): " + (str) (oldEdge2))
        # print("OldEdge3 (DE): " + (str) (oldEdge3))
        # print("OldEdge4 (EF): " + (str) (oldEdge4))
        
        # print("New total edge cost: %s" % (newTotal))
        # print("Old total edge cost: %s" % (oldTotal))
        # if (newTotal) < (oldTotal):
    
        listOfCities[randomIndex] = swapNode2
        listOfCities[randomIndex2] = swapNode
            
        newTotalCost = totalCost - oldTotal + newTotal
        # print("Node at index %s was swapped with node at index %s" % (randomIndex, randomIndex2))
            
        # print("Old total cost: %s" % (totalCost))
        # print("New total cost: %s" % (newTotalCost))
            
        
          
    else:
        #Attempting to swap nodes B and E in list [A, B, C, ... D, E, F]
        #so that it becomes [A, E, C, ... D, B, F]
        previousNode1 = listOfCities[randomIndex - 1]
        swapNode = listOfCities[randomIndex]
        nextNode1 = listOfCities[randomIndex + 1]
    
        previousNode2 = listOfCities[randomIndex2 - 1]
        swapNode2 = listOfCities[randomIndex2]
        try:
            nextNode2 = listOfCities[randomIndex2 + 1]
        except IndexError:
            nextNode2 = listOfCities[0]
        

        
        #old: previousNode1, swapNode, nextNode1, ..., previousNode2, swapNode2, nextNode2
        #new: previousNode1, swapNode2, nextNode1, ..., previousNode2, swapNode, nextNode2
        #Calculate new and old edge costs
        newEdge1 = nodeDist(previousNode1, swapNode2)
        newEdge2 = nodeDist(swapNode2, nextNode1)
        newEdge3 = nodeDist(previousNode2, swapNode,)
        newEdge4 = nodeDist(swapNode, nextNode2)
        
        oldEdge1 = nodeDist(previousNode1, swapNode)
        oldEdge2 = nodeDist(swapNode, nextNode1)
        oldEdge3 = nodeDist(previousNode2, swapNode2)
        oldEdge4 = nodeDist(swapNode2, nextNode2)
        
        #Compare total cost of new edges to old edges
        newTotal = newEdge1 + newEdge2 + newEdge3 + newEdge4
        oldTotal = oldEdge1 + oldEdge2 + oldEdge3 + oldEdge4
        # print("NewEdge1 (AE): " + (str) (newEdge1))
        # print("NewEdge2 (EC): " + (str) (newEdge2))
        # print("NewEdge3 (DB): " + (str) (newEdge3))
        # print("NewEdge4 (BF): " + (str) (newEdge4))
        # print("OldEdge1 (AB): " + (str) (oldEdge1))
        # print("OldEdge2 (BC): " + (str) (oldEdge2))
        # print("OldEdge3 (DE): " + (str) (oldEdge3))
        # print("OldEdge4 (EF): " + (str) (oldEdge4))
        
        # print("New total edge cost: %s" % (newTotal))
        # print("Old total edge cost: %s" % (oldTotal))
        # if (newTotal) < (oldTotal):
    
        listOfCities[randomIndex] = swapNode2
        listOfCities[randomIndex2] = swapNode
            
        newTotalCost = totalCost - oldTotal + newTotal
        # print("Node at index %s was swapped with node at index %s" % (randomIndex, randomIndex2))
            
        # print("Old total cost: %s" % (totalCost))
        # print("New total cost: %s" % (newTotalCost))
            
        
    listOfCities.append(listOfCities[0])
    totalSwaps = totalSwaps + 1

    
    return listOfCities, newTotalCost

    




# Simulated annealing function
# Given: list of points(a path), number of iterations, temperature
# Returns: best path within number of iterations 
listOfCities = generatePath(listOfPoints)
def simulatedAnnealing(listOfCities, maxIterations, maxTemp):
    #print("running sim")
    #currList, currCost = generatePath(listOfCities) # initial random path 
    currList, currCost = listOfCities
    #print("Initial cost: ", currCost)
    bestList, bestCost = currList, currCost
    currTemp = maxTemp
    #count = 0
    for i in range(1, maxIterations):
        ithList, ithCost = swapNodes(currList, currCost) # uses swap function
        currTemp = currTemp * .97 # cooling
        if (currTemp <= 0):
            currTemp = 1000
        if (ithCost <= currCost):
            #currList, currCost = ithList, ithCost
            currList = ithList
            currCost = ithCost
            if (ithCost <= bestCost):
                bestList, bestCost = ithList, ithCost
        elif ((math.exp((currCost-ithCost)/currTemp)) >= random.random()): #acceptance probability, random.random gives probabilites 
            
            #print("cost diff", currCost - ithCost)
            currList, currCost = ithList, ithCost
            #print("randomly selected intermediate worse path")
            


   
    return bestList, bestCost



#bestResult1, bestResultCost1 = simulatedAnnealing(listOfPoints, 2000, 1000)
for i in range (1, 1000):
    resultList, resultCost = simulatedAnnealing(listOfCities, 2000, 1000)
    listOfCities = resultList, resultCost
    if i % 10 == 0:
        print("on iteration ", i, "cost ", resultCost)
        

print("Time to run the algorithm 1000 times: " + (str) (time.time() - start) + " seconds")
timeUsed = time.time() - start
print(timeUsed)
timePerIteration = timeUsed/1000
print(timePerIteration)
timeRemaining = timeLimit - (time.time() - start)
print(timeRemaining)
iterationsRemaining = timeRemaining/timePerIteration
print(iterationsRemaining)
iterateRange = max(2, int(math.floor(iterationsRemaining)))
print(iterateRange)
iterationNumber = 1
flag = True
while iterationNumber < iterationsRemaining and flag:
    resultList, resultCost = simulatedAnnealing(listOfCities, 2000, 1000)
    listOfCities = resultList, resultCost
    if iterationNumber % 10 == 0:
        print("on iteration ", iterationNumber, "cost ", resultCost)
    if (timeLimit - (time.time() - start)) < 2:
        flag = False
    iterationNumber = iterationNumber + 1
    
print("Total time used: " + (str) (time.time() - start) + " seconds")
   
    

f = open(sys.argv[2], "w+")
f.write("Total cost: " +str(resultCost) + "\n")
for i in range(len(resultList)):
    city = resultList[i]
    id_num = node_IDs[city]
    if (i == len(resultList)-1):
        f.write(str(id_num))
    else:    
        f.write(str(id_num) + ", ")
f.close()    
    

