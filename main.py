
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def is_resource_sufficient(order_ingredients):
    """ Return True when the order can be made and return False when the resource is insufficient """

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry there is not enough water.")
            return False

    return True

def process_coin():
    """ Calculate Total value of the coin inserted by the customer"""

    total = int(input("how many quarters? : "))*0.25
    total += int(input("how many dimes ? : "))*0.1
    total += int(input("how many nickeles? : "))*0.05
    total += int(input("how many penny ? :"))*0.01

    return total

def is_transaction_succesful(money_received,drink_cost):
    """ Return True when the payment is accepted and Flase when the money is insufficent""" 

    if money_received >=drink_cost:
        change = round((money_received - drink_cost),2)
        print(f"here is your change : {change}")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money and refunding your money back")
        return False

def make_coffee(drink_name , order_ingredients):
    """ Deduct the order from the reources """

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your drink  ☕️ : {drink_name} ")    


while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino):")
    if choice == "off":
        is_on =False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]    
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):

            payment=process_coin() 
            if is_transaction_succesful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])



        