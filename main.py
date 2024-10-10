import math
menu = {
    "expresso":{
        "ingredients":{
            "water": 50,
            "coffee":10
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5, 
    },
    "cappuccinno":{
       "ingredients":{
         "water": 250,
         "milk": 100,
         "coffee": 24
       },
       "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

is_on = True
balance_checker = True
available_water = resources["water"]
available_milk = resources["milk"]
available_coffee = resources["water"]
available_money = resources["money"]
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25

def choice_ing():
    global choice_water
    choice_water = menu[choice]["ingredients"]["water"]
    global choice_coffee
    choice_coffee = menu[choice]["ingredients"]["coffee"]
    global choice_milk
    choice_milk = menu[choice]["ingredients"]["milk"]
    if choice == "expresso":
        choice_milk = 0
def report():
    print(f"Water: {available_water}ml\nMilk: {available_milk}ml\nCoffee: {available_coffee}g\nMoney: ${available_money}")

def resource_balancer():
   global available_water
   available_water -= choice_water
   global available_milk
   available_milk -= choice_milk
   global available_coffee
   available_coffee -= choice_coffee

def resource_checker():
    if available_water < choice_water:
        print("Insufficient water, please top-up")
    elif available_coffee < choice_coffee:
        print("Insufficient coffe, please top-up")
    elif available_milk < choice_milk:
        print("Insufficient milk, please top-up")
    else:
        print("Resources enough for selected option")



def cal():
    
    penny_choice = int(input("How many pennies?:"))
    nickel_choice = int(input("How many nicks?:"))
    dime_choice = int(input("How many dimes?:"))
    quarter_choice = int(input("How many quarter?:"))
    price = menu[choice]["cost"]
    global available_money
    available_money += price 
    total = (penny_choice * penny) + (nickel_choice * nickel) + (dime_choice * dime) + (quarter_choice * quarter)
    if total < price:
        balance_checker = False
        print("Insufficient balance, please add more coins")
        
        while not balance_checker:
            if total == price or total > price:
                balance_checker = True
                
            penny_choice = int(input("How many pennies?:"))
            nickel_choice = int(input("How many nicks?:"))
            dime_choice = int(input("How many dimes?:"))
            quarter_choice = int(input("How many quarter?:"))
            if total == price or total > price:
                balance_checker = True
            balance_checker = True
            print("k")
    elif total > price:
        excess = total - price
        print(f"Your change is {excess}")
    print(total)

while is_on:
    
    choice = input("What would you like(Expresso/Latte/Cappuccinno)?:\n").lower()
    if choice == "off":
       break
    elif choice == "report":
        report()
        break
    choice_ing()
    resource_checker()
    resource_balancer()
    cal()
    





  

