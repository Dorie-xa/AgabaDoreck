#sets
beverages = set(("Tea", "Coffee", "Juice"))
beverages.add("Water")
beverages.add("Milk")
print(beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

mySet.remove("kettle")
print(mySet)

for item in mySet:
    print(item)

myset2 = {"pen","book","bag","shoe"}
mylist = ["phone","bottle"]
myset2.update(mylist)
print(myset2)

ages = {20,21}
names = {"Agaba","Doreck"}
print(ages.union(names))