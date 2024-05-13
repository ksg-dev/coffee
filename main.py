import menu


def report(balance):
    uom = ["ml", "ml", "g"]
    for resource, amount in menu.resources.items():
        print(f"{resource.title()}: {amount}")

    print(f"Money: ${balance:.2f}")


def order():
    pass


def check_resources(drink):
    need_water = menu.MENU[drink]["ingredients"]["water"]
    need_coffee = menu.MENU[drink]["ingredients"]["coffee"]
    need_milk = menu.MENU[drink]["ingredients"]["milk"]
    have_water = menu.resources["water"]
    have_milk = menu.resources["milk"]
    have_coffee = menu.resources["coffee"]
    ingredients = list(menu.MENU[drink]["ingredients"])
    for i, r in








    # try:
    #     water = menu.MENU[drink]["ingredients"]["water"]
    #     coffee = menu.MENU[drink]["ingredients"]["coffee"]
    #     milk = menu.MENU[drink]["ingredients"]["milk"]
    # except KeyError:
    print(ingredients)
    print(resources)
    # print(f"Resources needed:\nWater: {water}\nMilk: {milk}\nCoffee: {coffee}")


def money():
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    q_total = 0.25 * q
    d_total = 0.10 * d
    n_total = 0.05 * n
    p_total = 0.01 * p
    total = sum([q_total, d_total, n_total, p_total])
    return float(total)


# operations = {
#     "report": report(),
#     "order": order(),
# }


def main():
    maker_on = True
    entered = 0
    while maker_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        if choice == "report":
            report(entered)
        elif choice == "off":
            maker_on = False
            print("Have a nice day!")
        # Test money function, return report
        elif choice == "money":
            entered += money()
            report(entered)
        elif choice == "espresso" or "latte" or "cappuccino":
            check_resources(choice)




main()
