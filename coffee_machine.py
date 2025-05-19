MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0  # in PLN
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_pln_coins():
    print("Insert coins (PLN):")
    pln5 = int(input("How many 5 PLN coins?: "))
    pln2 = int(input("How many 2 PLN coins?: "))
    pln1 = int(input("How many 1 PLN coins?: "))
    gr50 = int(input("How many 50 gr coins?: "))
    total = round(pln5 * 5 + pln2 * 2 + pln1 * 1 + gr50 * 0.5, 2)
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is {change} PLN in change.")
        resources["money"] += drink_cost
        return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: {resources["money"]} PLN')

# --- Main loop ---
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
        print("Shutting down the coffee machine...")
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_pln_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Unknown command.")
