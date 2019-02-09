"""Classes for melon orders."""

from random import randint
from datetime import datetime

class AbstractMelonOrder():
    base_price = None
    order_hour = datetime.now().hour
    order_day = datetime.now().today().weekday()
 
    """An abstract base class"""
    def __init__(self, species, qty):
        self.species= species
        self.qty = qty
        self.tax = 0
        self.shipped = False


    def get_base_price(self):
        """use rand int between 5-9 as base price"""
        if self.base_price != None:
            return self.base_price

        self.base_price = randint(5,9)
        if self.order_day in range(0, 6) and self.order_hour in range(8,12):
                self.base_price = self.base_price + 4
        return self.base_price

    def get_total(self):
        """Calculate price, including tax."""
        if self.base_price == None:
            self.get_base_price()

        if self.species == "Christmas melons":
            total = (1 + self.tax) * self.qty * self.base_price * 1.5
        else:
            total = (1 + self.tax) * self.qty * self.base_price      
    
        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True   

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def shipping_status(self):
        print(self.shipped)
        return None

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty, country_code='USA', tax=0.08):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "domestic"
        self.tax = tax



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code, tax=0.17):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = tax

    def get_total(self):
        if self.qty < 10:
            return super().get_total() + 3
            print("flat fee added")
        else:
            return super().get_total()

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self,species,qty,country_code='USA', tax=0):
        super().__init__(species,qty)
        self.country_code = country_code
        self.order_type = "government"
        self.tax = tax
        self.passed_inspection = False

    def mark_inspection(self, passed_inspection):
        self.passed_inspection = passed_inspection

