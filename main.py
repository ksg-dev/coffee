import menu


def report():
    for resource, amount in menu.resources.items():
        print(f"{resource.title()}: {amount}")


def order():
    pass


def check_resources():
    pass


def money():
    print("Please insert coins.")
    q = int(input("How many quarters?: "))


# operations = {
#     "report": report(),
#     "order": order(),
# }


def main():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if choice == "report":
        report()


main()
