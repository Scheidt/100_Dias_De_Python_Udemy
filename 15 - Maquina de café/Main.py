menu = {
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
    "money": 0.0,
}


# Check Resources
def report(resources: dict):
    print("REPORT OF THE MACHINE'S RESOURCES")
    print(f"The machine has {resources['water']} ml of water")
    print(f"The machine has {resources['milk']} ml of milk")
    print(f"The machine has {resources['coffee']} g of cooffee")
    print(f"The machine has {resources['money']}$")

# Process coins
def process_coins():
    print("Insert the amount of coins")
    while True:
        try:
            total = int(input("Insert the amount of quarters (0.25$)?: ")) * 0.25
            total += int(input("Insert the amount of dimes (0.1$)?: ")) * 0.1
            total += int(input("Insert the amount of nickles (0.05): ")) * 0.05
            total += int(input("Insert the amount of pennies? (0.01): ")) * 0.01
            return total
        except:
            print("Você inseriu um valor não numérico. Por favor, tente novamente.")

# Check transaction sucessful?
def check_enough_money(order, payment):
    if payment >= order['cost']:
        print("payment successful!")
        if payment >= order['cost']:
            print(f"Dispensing change of {payment-order['cost']}$")
        return True
    else:
        print(f"You haven't inserted enought money! The {payment:.2fes}$ you inserted will be returned.")
        return False

# Make cofee
def make_coffee(order):
    # Verify if machine has enough ingredients
    for ingredient, value in order['ingredients'].items():
       if resources[ingredient] - value < 0:
           print(f"The machine doesn't have enough {ingredient} to make your order. Money returned")
           return
    for ingredient, value in order['ingredients'].items():
        resources[ingredient] -= value
    resources['money'] += order['cost']
    print("Your order is done!")


while True:
    option = input("Insert your order [espresso/latte/cappuccino]: ")
    if option == 'off':
        break
    elif option == 'report':
        report(resources)
    else:
        try:
            order = menu[option]
        except:
            print("This option does not exist! Try another one")
        else:
            money = process_coins()
            if check_enough_money(order, money):
                make_coffee(order)