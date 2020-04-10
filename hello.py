import random
import math
import sys

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
    
generatePath(listOfPoints)
