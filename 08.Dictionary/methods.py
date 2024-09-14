Daemon = {
    "name": "Daemon Targeryan",
    "age": 40,
    "designation": {
        1: "Queen's husband",
        2: "Queen's uncle",
        3: "Queen's daughter-in-law's father",
    },
    "ratings": 9.4,
    "spouse": {1: "Rheanerya Targeryan", 2: "Laena Velaryon"},
}
print("Keys are : ", Daemon.keys())
print("List of keys are : ", list(Daemon.keys()))
print("Values are : ", Daemon.values())
print("List of values are : ", list(Daemon.values()))
print("Items are : ", Daemon.items())
print("List of items are : ", list(Daemon.items()))
print("Values of spouse: ", Daemon.get("spouse"))
print("List of values of spouse are : ", list((Daemon.get("spouse")).items()))
Daemon.update({"siblings": "Viserys Targeryan"})
print(Daemon)
