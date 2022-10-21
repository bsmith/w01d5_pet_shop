# PDA Reference: I.T 6

people = [
    { "name": "Alice", "budget": 500, "desired_pet": "dog" },
    { "name": "Bob", "budget": 1000, "desired_pet": "cat" },
    { "name": "Chris", "budget": 450, "desired_pet": "goldfish" },
]

# ***
pet_prices = {
    "dog": 900,
    "goldfish": 5,
    "cat": 500,
}

# ***
def can_person_afford_pet(person, pet):
    return person["budget"] >= pet_prices[pet]

for person in people:
    # ***
    affordable = can_person_afford_pet(person, person["desired_pet"])
    print(f"{person['name']} wants a {person['desired_pet']}")
    print("They can " + ("not " if not affordable else "") + "afford it")
    if can_person_afford_pet(person, "goldfish"):
        print("Have they considered a goldfish?")

