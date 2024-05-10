import menu


def report(balance):
    uom = ["ml", "ml", "g"]
    for resource, amount in menu.resources.items():
        print(f"{resource.title()}: {amount}")

    print(f"Money: ${balance:.2f}")


def order():
    pass


def check_resources():
    pass


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
    entered = 0
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if choice == "report":
        report(entered)
    # Test money function, return report
    elif choice == "money":
        entered += money()
        report(entered)


main()
