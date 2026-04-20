from random import randint
from datetime import datetime, timedelta
from quicksort import quickSort
from listcompareaccuracy import listCompareAccuracy

# Range for length of data
itemnumlower = 5
itemnumhigher = 10
# Range for size of items
itemrangelower = 1
itemrangehigher = 99


# Main

data = []
for i in range(randint(itemnumlower, itemnumhigher)):
    data.append(randint(itemrangelower, itemrangehigher))
sorteddata = quickSort(data)

print(data)
print()
print("Sorted List:")

startime = datetime.now()

humandata = []
for i in range(len(data)):
    while True:
        try:
            newitem = int(input(f"Item {i+1}/{len(data)}:\n"))
            humandata.append(newitem)
            break
        except:
            print("Invalid input")

endtime = datetime.now()
timetaken = endtime - startime
timeperitem = timetaken / len(data)

accuracyresult = listCompareAccuracy(sorteddata, humandata)
accuracy = accuracyresult[0]
incorrect = accuracyresult[1]

print()
print(f"Original data:\n{data}\n")
print(f"Hopefully sorted data:\n{humandata}\n")

print(f"Time taken: {timetaken}")
print(f"Time taken per item: {timeperitem}")
print(f"Accuracy: {accuracy*100}%")


# Ranks based on time and incorrect answers
# Times (sec per item): 1.5, 2, 3, 4, 5, 6, 6+
# -1 Rank per incorrect answer
ranks = ['SS', 'S', 'A', 'B', 'C', 'D', 'F']

if timeperitem < timedelta(milliseconds=1500):
    rankindex = 0
elif timeperitem < timedelta(milliseconds=2000):
    rankindex = 1
elif timeperitem < timedelta(milliseconds=3000):
    rankindex = 2
elif timeperitem < timedelta(milliseconds=4000):
    rankindex = 3
elif timeperitem < timedelta(milliseconds=5000):
    rankindex = 4
elif timeperitem < timedelta(milliseconds=6000):
    rankindex = 5
else:
    rankindex = 6

for i in range(incorrect):
    if rankindex < 6: # Can't go past F rank
        rankindex += 1

print()
print(f"Rank: {ranks[rankindex]}")