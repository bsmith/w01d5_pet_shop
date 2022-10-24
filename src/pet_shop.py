"""The Pet Shop"""

# mypy docs: https://mypy.readthedocs.io/

from typing_extensions import reveal_type
from typing import Iterable, Any

Pet = dict[str, str | int]
Customer = dict[str, str | int | list[Pet]]
PetShop = dict[str, str | dict[str, int] | list[Pet]]

def get_pet_shop_name(pet_shop: PetShop) -> str:
    assert isinstance(pet_shop["name"], str)
    return pet_shop["name"]

def get_total_cash(pet_shop: PetShop) -> int:
    assert isinstance(pet_shop["admin"], dict)
    # assert isinstance(pet_shop["admin"]["total_cash"], int)
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop: PetShop, amount: int) -> None:
    assert isinstance(pet_shop["admin"], dict)
    # assert isinstance(pet_shop["admin"]["total_cash"], int)
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop: PetShop) -> int:
    assert isinstance(pet_shop["admin"], dict)
    # assert isinstance(pet_shop["admin"]["pets_sold"], int)
    return pet_shop["admin"]["pets_sold"]

# But we're not actually selling any pets?
def increase_pets_sold(pet_shop: PetShop, number: int) -> None:
    assert isinstance(pet_shop["admin"], dict)
    # assert isinstance(pet_shop["admin"]["pets_sold"], int)
    pet_shop["admin"]["pets_sold"] += number

def get_stock_count(pet_shop: PetShop) -> int:
    return len(pet_shop["pets"])

# def get_pets_by_breed(pet_shop: PetShop, breed_name: str) -> list[dict[str, str | int]]:
def get_pets_by_breed(pet_shop: PetShop, breed_name: str) -> Any:
    assert isinstance(pet_shop["pets"], list)
    return [pet for pet in pet_shop["pets"] if pet["breed"] == breed_name]

#def first(list):
#    return list[0] if list else None

# The Trick: the for loop only runs once
def first(iterable: Iterable[Any]) -> Any:
    """Return the first item in an iterable, otherwise None"""
    for item in iterable:
        return item
    return None

# reveal_type(first)

def find_pet_by_name(pet_shop: PetShop, pet_name: str) -> Pet | None:
    assert isinstance(pet_shop["pets"], list)
    pet = first(pet for pet in pet_shop["pets"] if pet["name"] == pet_name)
    assert pet is None or isinstance(pet, dict)
    return pet

def remove_pet(pet_shop: PetShop, pet: Pet) -> None:
    assert isinstance(pet_shop["pets"], list)
    pet_shop["pets"].remove(pet)

def remove_pet_by_name(pet_shop: PetShop, pet_name: str) -> None:
    pet = find_pet_by_name(pet_shop, pet_name)
    if pet is not None:
        remove_pet(pet_shop, pet)

def add_pet_to_stock(pet_shop: PetShop, pet: Pet) -> None:
    assert isinstance(pet_shop["pets"], list)
    pet_shop["pets"].append(pet)

def get_customer_cash(customer: Customer) -> int:
    assert isinstance(customer["cash"], int)
    return customer["cash"]

def remove_customer_cash(customer: Customer, amount: int) -> None:
    assert isinstance(customer["cash"], int)
    customer["cash"] -= amount

def get_customer_pet_count(customer: Customer) -> int:
    assert isinstance(customer["pets"], list)
    return len(customer["pets"])

def add_pet_to_customer(customer: Customer, pet: Pet) -> None:
    assert isinstance(customer["pets"], list)
    customer["pets"].append(pet)

def customer_can_afford_pet(customer: Customer, pet: Pet) -> bool:
    assert isinstance(customer["cash"], int)
    assert isinstance(pet["price"], int)
    return customer["cash"] >= pet["price"]

def process_cash_tender(pet_shop: PetShop, customer: Customer, amount: int) -> None:
    remove_customer_cash(customer, amount)
    add_or_remove_cash(pet_shop, amount)

def sell_pet_to_customer(pet_shop: PetShop, pet: Pet, customer: Customer) -> None:
    # Check that the pet hasn't escaped
    if pet == None:
        return # raise ValueError("Pet must be not-None")
    # Check that the customer has enough money
    if not customer_can_afford_pet(customer, pet):
        return # raise ValueError("Customer is too poor")
    # Take money from customer; Add money to shop
    assert isinstance(pet["price"], int)
    process_cash_tender(pet_shop, customer, pet["price"])
    # Remove the pet from the shop
    remove_pet(pet_shop, pet)
    # And update how many have been sold
    increase_pets_sold(pet_shop, 1)
    # Add the pet to the customer
    add_pet_to_customer(customer, pet)
