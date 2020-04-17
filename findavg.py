from Lib import statistics


costs = [28175, 28855, 28027, 29539, 27586, 28027, 28849, 27586, 28575, 28027]

avgcost = 0
for cost in costs:
    avgcost += cost
avgcost = avgcost / 10
print(avgcost)

differences = []
for cost in costs:
    diff = (cost - avgcost)**2
    differences.append(diff)

totaldiff = 0
for difference in differences:
    totaldiff += difference

stdev = totaldiff/10
stdev = (stdev)**(1/2)
print(stdev)

x = statistics.mean(costs) 
  
# Printing the mean 
print("Mean is :", x)

print("Standard Deviation of sample is %s " % (statistics.stdev(costs)))




