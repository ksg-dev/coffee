from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
atm = MoneyMachine()



def main():
    maker_on = True
    while maker_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            maker_on = False
            print("Have a nice day!")
        elif choice == "report":
            coffeemaker.report()
            atm.report()
        elif choice == "espresso" or "latte" or "cappuccino":
            drink = Menu().find_drink(choice)
            if coffeemaker.is_resource_sufficient(drink):
                if atm.make_payment(drink.cost):
                    coffeemaker.make_coffee(drink)
            


main()