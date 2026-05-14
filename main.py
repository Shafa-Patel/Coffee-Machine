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


on_off=True
def report():
    print(resources)

def sufficient_resources(choice):

    for item in resources:
        if resources[item] < MENU[choice]["ingredients"][item]:
              print(f"Sorry, we don't have enough {item} to make {choice}")
              return False

    return True


def process_coins(choice):
    price = MENU[choice]["cost"]
    quarters=float(input("Please Enter the no.of Quarters:"))
    dimes=float(input("Please Enter the no.of Dimes:"))
    nickles =float(input("Please Enter the no.of Nickles :"))
    pennies =float(input("Please Enter the no.of Pennies :"))
    received_money=(quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    if price>received_money:
        print(f"PRICE OF {choice} is {price}  ")
        print(f"you didnt provided sufficient money")
        print("TRANSACTION CANCELED")
        return False
    elif price<received_money:
        print(f"PRICE OF {choice} is {price}  ")
        print(f"Please take the remaining amount{received_money-price}")
        print(f"Here's your {choice}! ENJOY")
        return True
    return True

def update_resources(choice):
    for item in MENU[choice]["ingredients"]:
         resources[item] -= MENU[choice]["ingredients"][item]

while on_off:
    user_coffee = input("What would you like? (espresso/latte/cappuccino):")
    if user_coffee == "off":
        on_off = False
    elif user_coffee == "report":
        report()
    else:
        if sufficient_resources(user_coffee):
           if process_coins(user_coffee):
               update_resources(user_coffee)

