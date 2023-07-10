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


#Printar relatório
def report(resources: dict):
    print("REPORT OF THE MACHINE'S RESOURCES")
    print(f"The machine has {resources['water']} ml of water")
    print(f"The machine has {resources['milk']} ml of milk")
    print(f"The machine has {resources['coffee']} g of cooffee")
    print(f"The machine has {resources['money']}$")

# Check Resources
# Process coins
def process_coins():
    print("Insert the amount of coins")
    total = int(input("how many quarters (0.25$)?: ")) * 0.25
    total += int(input("how many dimes (0.01$)?: ")) * 0.1
    total += int(input("how many nickles (?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
# Check transaction sucessful?
def check_enough_money(order, payment):
    if payment >= order['cost']:
        print("payment successful!")
        if payment >= order['cost']:
            print(f"Dispensing change of {payment-order['cost']}")
        return True
    else:
        print("You haven't inserted enought money! Money inserted returned")
        return False

# Make cofee
def make_coffee(order, resources):
    for ingredient, value in order['ingredients'].values:
        resources[ingredient] -= value
    print("Your order is done!")


while True:
    option = input("Insert your order [espresso/latte/cappuccino]")
    if option == 'off':
        break
    elif option == 'report':
        report(resources)
    else:
        try:
            order = menu['order']
        except:
            print("This option does not exist! Try another one")
        else:
            money = process_coins()
            if check_enough_money(order, money):
                make_coffee(order, resources)