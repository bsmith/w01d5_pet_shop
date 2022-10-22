# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# But we're not actually selling any pets?
def increase_pets_sold(pet_shop, number):
    pet_shop["admin"]["pets_sold"] += number

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_name):
    return [pet for pet in pet_shop["pets"] if pet["breed"] == breed_name]

#def first(list):
#    return list[0] if list else None

# The Trick: the for loop only runs once
def first(iterable):
    """Return the first item in an iterable, otherwise None"""
    for item in iterable:
        return item
    return None

def find_pet_by_name(pet_shop, pet_name):
    return first(pet for pet in pet_shop["pets"] if pet["name"] == pet_name)

def remove_pet(pet_shop, pet):
    pet_shop["pets"].remove(pet)

def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name(pet_shop, pet_name)
    remove_pet(pet_shop, pet)

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

def process_cash_tender(pet_shop, customer, amount):
    remove_customer_cash(customer, amount)
    add_or_remove_cash(pet_shop, amount)

def sell_pet_to_customer(pet_shop, pet, customer):
    # Check that the pet hasn't escaped
    if pet == None:
        return # raise ValueError("Pet must be not-None")
    # Check that the customer has enough money
    if not customer_can_afford_pet(customer, pet):
        return # raise ValueError("Customer is too poor")
    # Take money from customer; Add money to shop
    process_cash_tender(pet_shop, customer, pet["price"])
    # Remove the pet from the shop
    remove_pet(pet_shop, pet)
    # And update how many have been sold
    increase_pets_sold(pet_shop, 1)
    # Add the pet to the customer
    add_pet_to_customer(customer, pet)
