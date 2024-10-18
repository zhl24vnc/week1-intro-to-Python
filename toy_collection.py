toy_collection = {
    "Teddy Bear": {
        "age_suitability": 3,
        "is_electronic": False
    },
    "Remote Control Car": {
        "age_suitability": 6,
        "is_electronic": True
    }
}

toy_collection["Lego Set"] = {
    "age_suitability": 5,
    "is_electronic": False
}
toy_collection["Drone"] = {
    "age_suitability": 10,
    "is_electronic": True
}

def add_toy(toy_name, age_suitability, is_electronic):
    if toy_name in toy_collection:
        return f"Toy '{toy_name}' already exists in the collection."
    toy_collection[toy_name] = {
        "age_suitability": age_suitability,
        "is_electronic": is_electronic
    }
    return f"Toy '{toy_name}' has been added to the collection."

def find_toy(toy_name):
    if toy_name in toy_collection:
        return toy_collection[toy_name]
    else:
        return f"Toy '{toy_name}' is not in the collection."
def remove_toy(toy_name):
    if toy_name in toy_collection:
        del toy_collection[toy_name]
        return f"Toy '{toy_name}' has been removed from the collection."
    else:
        return f"Toy '{toy_name}' does not exist in the collection."
def list_toys():
    if toy_collection:
        return list(toy_collection.keys())
    else:
        return "The toy collection is empty."
    
print(find_toy("Teddy Bear"))
print(find_toy("Robot"))     
print(add_toy("Robot", 7, True)) 
print(add_toy("Teddy Bear", 3, False))
print(remove_toy("Drone"))
print(remove_toy("Drone"))
print(list_toys())