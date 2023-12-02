from beverage_factory import BeverageFactory

class CoffeeMachineMain:
    def add_beverage(self, beverage_type):
        beverage = BeverageFactory().create_beverage(beverage_type)
        beverage.make()
            



if __name__ == "__main__": 
    cm=CoffeeMachineMain()
    cm.add_beverage("Coffee")

