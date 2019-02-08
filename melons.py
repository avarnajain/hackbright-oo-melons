"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class"""
    def __init__(self, species, qty):
        self.species= species
        self.qty = qty
        self.tax = 0
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "Christmas melons":
            base_price = 5 * 1.5
        else:
            base_price = 5
        total = (1 + self.tax) * self.qty * base_price

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


