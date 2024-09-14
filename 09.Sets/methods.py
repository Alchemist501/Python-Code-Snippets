collection = {True, 1, 2.98, "Python", ("Drogon", "Caraxes", "Vermithor", "Cannibel")}
print(collection)
collection.add("Coding")
print(collection)
collection.remove("Coding")
print(collection)
collection.clear()
print(collection)
collection = {True, 1, 2.98, "Python", ("Drogon", "Caraxes", "Vermithor", "Cannibel")}
print(collection.pop())
print(collection)
coll = {1, 2, 3}
print("Union :", collection.union(coll))
print("Intersection : ", collection.intersection(coll))
# 1 will not be there as 1 is itself considered as true and neglected
