from Coffee import coffee

class BeverageFactory:
    def create_beverage(self, beverage_type):
        if beverage_type == "Coffee":
            return coffee()
