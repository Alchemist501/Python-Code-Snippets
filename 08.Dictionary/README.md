# DICTIONARY

    Used to store data values in key:value pairs
    They are unordered mutable and don't allow duplicate keys
    dict = {
        "name":"Rheanerya Targareyan",
        "age":33,
        "Title":"Queen"
        "Spouse":"Daemon Targareyan"
    }
    dict["name"] => dict["key"] returns value

# Nested Dictionary

    dict = {
        'name': 'Daemon Targeryan',
        'age': 40,
        'designation': {
            1: "Queen's husband",
            2: "Queen's uncle",
            3: "Queen's daughter-in-law's father"
        },
        'ratings': 9.4,
        'spouse': {
            1: 'Rheanerya Targeryan',
            2: 'Laena Velaryon'
        }
    }
    dict['designation'][1] => Queen's husband

# Dictionary Methods

    dict.keys()    => Returns all keys
    dict.values()  => Returns all values
    dict.items()   => Returns all key-value pairs as tuples
    dict.get("key")=> Returns the key according to the value
    dict.update(newdict) =>Inserts the newdict to dict
