from abc import ABC, abstractmethod

class FoodType:
    french = 1
    american = 2

class Resaturant(ABC):
    @abstractmethod
    def make_food(self):
        pass

    @abstractmethod
    def make_drink(self):
        pass

class FrenchResaturant(Resaturant):
    def make_food(self):
        print("Cordon Bleu")

    def make_drink(self):
        print("Merlot")

class AmericanRestaurant(Resaturant):
    def make_food(self):
        print("Hamburger")

    def make_drink(self):
        print("Coca cola")

class RestaurantFactory:
    @staticmethod
    def suggest_restaurant(r_type: FoodType):
        if r_type == FoodType.french:
            return FrenchResaturant()
        else:
            return AmericanRestaurant()

def dine_at(restaurant: Resaturant):
    print(" for dinner we are having:")
    restaurant.make_food()
    restaurant.make_drink()

if __name__ == '__main__':
    suggestion1 = RestaurantFactory.suggest_restaurant(FoodType.french)
    suggestion2 = RestaurantFactory.suggest_restaurant(FoodType.american)

    dine_at(suggestion1)
    dine_at(suggestion2)