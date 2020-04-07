# should print hello world 
#print("Hello world")

f = open("mat-test.txt")
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

copyOfList = listOfPoints

f.close()

