import time
import logo
import os

MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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
    },
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}



def coin_cal():
    penny = int(input("Pay in penny:- "))
    nickle = int(input("Pay in nickle:- "))
    dime = int(input("Pay in dime:- "))
    quatar = int(input("Pay in quatar:- "))
    result = (0.01 * penny) + (0.05 * nickle) + (0.1 * dime) + (0.5 * quatar)
    return result

end = True
money = 0

def coffee_maker(coffee):
        coffee_name = MENU[coffee]
        is_coffee_made = coffee_name["ingredients"]
        if is_coffee_made["water"] > resources["water"]:
            print("Sorry, Water is insufficient to make the coffee")
            return False
        elif is_coffee_made["milk"] > resources["milk"]:
            print("Sorry, milk is insufficient to make the coffee")
            return False

        elif is_coffee_made["coffee"] > resources["coffee"]:
            print("Sorry, Coffee is insufficient to make the coffee")
            return False
        else:
            money_received = coin_cal()
            if money_received >= coffee_name["cost"]:
                if money_received > coffee_name["cost"]:
                    change = money_received - coffee_name["cost"]
                    print(f"Your change  is {change}")

                print(f"Enjoy your {coffee}")
                resources["coffee"] -= coffee_name["ingredients"]['coffee']
                resources["milk"] -= coffee_name["ingredients"]['milk']
                resources["water"] -= coffee_name["ingredients"]['water']
                return coffee_name["cost"]
            else:
                print("Your have paid insufficient money.")
                return False

print(f"""
          {logo.cup}
          """)

while end:
    
    # os.system('cls')

    coffee = input("What coffee do you want? (espresso/cappuccino/latte)-> ")
    if coffee != "report":
        ans = coffee_maker(coffee)
        if  ans == False:
            end = False
        else:
            money += ans
    else:
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}")
    # time.sleep(5)