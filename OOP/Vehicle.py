from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


        Attributes:
            wheels: An integer representing the number of wheels the vehicle has.
            miles: The integral number of miles driven on the vehicle.
            make: The make of the vehicle as a string.
            model: The model of the vehicle as a string.
            year: The integral year the vehicle was built.
            sold_on: The date the vehicle was sold.
        """
    _metaclass_ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
            return 0.0 #already sold
        return 5000 * self.wheels

    def purchase_price(self):
        if self.sold_on is None:
            return 0.0 # Not yet sold
        return  self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        pass



class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return 'car'


class Motorcycle(Vehicle):
    base_sale_price = 1500
    wheels = 2

    def vehicle_type(self):
        return 'motorcycle'

BeatFi = Motorcycle(0,"Honda", "Beat Fi", 2016, 10000)

print(BeatFi.sale_price())
print(BeatFi.purchase_price())