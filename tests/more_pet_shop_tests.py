import unittest
from src.pet_shop import *
from tests.pet_shop_test import TestPetShop

class MorePetShopTests(unittest.TestCase):
    def setUp(self):
        # borrow the test data
        tps = TestPetShop()
        tps.setUp()
        self.customers = tps.customers
        self.new_pet = tps.new_pet
        self.cc_pet_shop = tps.cc_pet_shop

    def test_process_cash_tender(self):
        process_cash_tender(self.cc_pet_shop, self.customers[0], 100)
        shop_cash = get_total_cash(self.cc_pet_shop)
        customer_cash = get_customer_cash(self.customers[0])
        self.assertEqual(1100, shop_cash)
        self.assertEqual(900, customer_cash)

    def test_remove_pet(self):
        pet = find_pet_by_name(self.cc_pet_shop, "Tristan")
        remove_pet(self.cc_pet_shop, pet)
        self.assertEqual(5, get_stock_count(self.cc_pet_shop))