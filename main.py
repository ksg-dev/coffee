import menu


def report(resources, balance):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${balance:.2f}")


def make_coffee(drink, ingredients):
    """Subtract used resources from resources"""
    resources = menu.resources

    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")


def check_resources(order_ingr):
    """Returns True when order can be made, False if ingredients are insufficient."""
    resources = menu.resources
    for item in order_ingr:
        if order_ingr[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def money():
    """Takes coins as input, returns balance entered to main function"""
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


def check_money(entered_money, drink_cost):
    """Returns True if enough money was entered, change if over, False if not enough entered"""
    if entered_money < drink_cost:
        print(f"Not enough money entered.\nWe've refunded your ${entered_money}.")
        return False
    elif entered_money > drink_cost:
        change = entered_money - drink_cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        return True


def main():
    maker_on = True
    entered = 0
    while maker_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        if choice == "off":
            maker_on = False
            print("Have a nice day!")
        elif choice == "report":
            report(menu.resources, entered)
        elif choice == "espresso" or "latte" or "cappuccino":
            drink = menu.MENU[choice]
            if check_resources(drink["ingredients"]):
                payment = money()
                if check_money(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])


main()
