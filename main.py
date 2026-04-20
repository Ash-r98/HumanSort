from random import randint
from datetime import datetime, timedelta

# Range for length of data
itemnumlower = 5
itemnumhigher = 10
# Range for size of items
itemrangelower = 1
itemrangehigher = 99

data = []
for i in range(randint(itemnumlower, itemnumhigher)):
    data.append(randint(itemrangelower, itemrangehigher))

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

print()
print(f"Original data:\n{data}\n")
print(f"Hopefully sorted data:\n{humandata}\n")

print(f"Time taken: {timetaken}")