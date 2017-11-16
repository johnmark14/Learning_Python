class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
       following properties:

       Attributes:
           name: A string representing the customer's name.
           balance: A float tracking the current balance of the customer's account.
       """

    def __init__(self, name, balance=0.0):
        # Return a Customer object whose name is *name*.
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        # Return the  balance remaining after withdrawing *amount*
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        # Return the balance remaining after depositing *amount*
        self.balance += amount
        return self.balance


c001 = Customer("John Mark D. Gabrentina")

print(c001.get_name())

print(c001.deposit(100))

print(c001.withdraw(50))

