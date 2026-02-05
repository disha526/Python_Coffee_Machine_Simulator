from data import MENU , resource
profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    total = int(input("quarters? ")) * 0.25
    total += int(input("dimes? ")) * 0.10
    total += int(input("nickles? ")) * 0.05
    total += int(input("pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ")

is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        is_on = False

    elif user_choice == "report":
        print(resources)
        print(f"Money: ${profit}")

    elif user_choice in MENU:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select espresso,latte,cappuccino.")


