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
}


def coffee_machine():
    machine = True
    coffee_cost = 0
    machine_profit = 0
    while machine:

        def cost(qcoin, dcoin, nick, pen):
            choice_cost = (qcoin * 0.25) + (dcoin * 0.10) + (nick * 0.05) + (pen * 0.01)
            return choice_cost

        def check(coffee):
            """Checks if customer money is enough to buy selected beverage"""
            if coffee >= prefer_cost:
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")

        # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        choice = input("What would you like? (espresso/latte/capuccino): ")

        # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
        if choice == "off":
            machine = False
        # TODO 3. Print report

        if choice == "report":
            water = resources["water"]
            milk = resources["milk"]
            coffee = resources["coffee"]
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Water:{water}ml")
            print(f"money:{machine_profit}$")

        # TODO 4. Check resources sufficient?
        resource_check = False

        def check_resource(choice_drink):
            """Checks if remaining resources is enough to make customer request"""
            if choice != "report" and choice != "off":
                if MENU[choice_drink]["ingredients"]["water"] <= resources["water"]:
                    if MENU[choice_drink]["ingredients"]["coffee"] <= resources["coffee"]:
                        if choice_drink != "espresso":
                            if MENU[choice_drink]["ingredients"]["milk"] <= resources["milk"]:
                                return True
                            else:
                                print("Sorry there is not enough milk.")

                        else:
                            return True
                    else:
                        print("Sorry there is not enough coffee.")

                else:
                    print("Sorry there is not enough water.")

        # TODO 5. Process coins
        proceed_pay = True
        if check_resource(choice):
            print("Please insert coins")
            quarters = int(input("How many quarters?:"))
            dimes = int(input("How many dimes?:"))
            nickels = int(input("How many nickels?:"))
            pennies = int(input("How many pennies?:"))

            coffee_cost = (cost(quarters, dimes, nickels, pennies))
        else:
            proceed_pay = False

        # TODO 6. Check transaction successful
        prefer_cost = 0
        if proceed_pay:
            for prefer in MENU:
                if prefer == choice:
                    prefer_cost = MENU[choice]["cost"]
                    machine_profit += prefer_cost

        # TODO 7. Make coffee
        # deduct resources from order
        if choice != "report" and choice != "off":
            if check(coffee_cost):
                if proceed_pay:
                    resources["water"] -= MENU[choice]["ingredients"]["water"]
                    change = coffee_cost - MENU[choice]["cost"]
                    print(f"Here is {round(change, 2)}$ in change.")
                    print(f"Here is your {choice} ☕. Enjoy!")
                    if choice != "espresso":
                        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]


coffee_machine()
