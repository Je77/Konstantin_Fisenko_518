class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550


def print_has():
    print(" ")
    print("The coffee machine has:")
    print(f"{CoffeeMachine.water} of water")
    print(f"{CoffeeMachine.milk} of milk")
    print(f"{CoffeeMachine.coffee} of coffee beans")
    print(f"{CoffeeMachine.cups} of disposable cups")
    print(f"${CoffeeMachine.money} of money")


while True:
    print(" ")
    water_can_espresso = CoffeeMachine.water // 250
    coffee_can_espresso = CoffeeMachine.coffee // 16

    water_can_latte = CoffeeMachine.water // 350
    coffee_can_latte = CoffeeMachine.coffee // 20
    milk_can_latte = CoffeeMachine.milk // 75

    water_can_cappuccino = CoffeeMachine.water // 200
    coffee_can_cappuccino = CoffeeMachine.coffee // 12
    milk_can_cappuccino = CoffeeMachine.milk // 100


