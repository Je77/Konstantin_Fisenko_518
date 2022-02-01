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

    cups_of_with = input("Write action (buy, fill, take, remaining, exit):")
    if cups_of_with == 'remaining':
        print_has()
    if cups_of_with == 'exit':
        break
    if cups_of_with == 'buy':
        print(" ")
        buy_number = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if buy_number == 'back':
            continue
        if buy_number == '1' and CoffeeMachine.cups != 0:
            if water_can_espresso >= 1:
                if coffee_can_espresso >= 1:
                    CoffeeMachine.water -= 250
                    CoffeeMachine.coffee -= 16
                    CoffeeMachine.cups -= 1
                    CoffeeMachine.money += 4
                    print("I have enough resources, making you a coffee!")
                    print(" ")
                else:
                    print("Sorry, not enough coffee beans!")
                    print(" ")
