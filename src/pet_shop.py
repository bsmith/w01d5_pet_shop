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

def remove_pet_by_name(pet_shop, pet_name):
    pass

def add_pet_to_stock(pet_shop, pet):
    pass

def get_customer_cash(customer):
    pass

def remove_customer_cash(customer, amount):
    pass

def get_customer_pet_count(customer):
    pass

def add_pet_to_customer(customer, pet):
    pass

def customer_can_afford_pet(customer, pet):
    pass

def sell_pet_to_customer(pet_shop, customer):
    pass
