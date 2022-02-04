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
            else:
                print("Sorry, not enough water!")
                print(" ")
        elif buy_number == '2' and CoffeeMachine.cups != 0:
            if water_can_latte >= 1:
                if coffee_can_latte >= 1:
                    if milk_can_cappuccino >= 1:
                        CoffeeMachine.water -= 350
                        CoffeeMachine.milk -= 75
                        CoffeeMachine.coffee -= 20
                        CoffeeMachine.cups -= 1
                        CoffeeMachine.money += 7
                        print("I have enough resources, making you a coffee!")
                        print(" ")
                    else:
                        print("Sorry, not enough coffee milk!")
                        print(" ")
                else:
                    print("Sorry, not enough coffee beans!")
                    print(" ")
            else:
                print("Sorry, not enough water!")
                print(" ")
        elif buy_number == '3' and CoffeeMachine.cups != 0:
            if water_can_cappuccino >= 1:
                if coffee_can_cappuccino >= 1:
                    if milk_can_latte >= 1:
                        CoffeeMachine.water -= 200
                        CoffeeMachine.milk -= 100
                        CoffeeMachine.coffee -= 12
                        CoffeeMachine.cups -= 1
                        CoffeeMachine.money += 6
                        print("I have enough resources, making you a coffee!")
                        print(" ")
                    else:
                        print("Sorry, not enough coffee milk!")
                        print(" ")
                else:
                    print("Sorry, not enough coffee beans!")
                    print(" ")
            else:
                print("Sorry, not enough water!")
                print(" ")
        elif cups_of_with == "fill":
            water_add = int(input("Write how many ml of water do you want to add:"))
            CoffeeMachine.water = CoffeeMachine.water + water_add
            milk_add = int(input("Write how many ml of milk do you want to add:"))
            CoffeeMachine.milk = CoffeeMachine.milk + milk_add
            coffee_add = int(input("Write how many grams of coffee beans do you want to add:"))
            CoffeeMachine.coffee = CoffeeMachine.coffee + coffee_add
            cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
            CoffeeMachine.cups = CoffeeMachine.cups + cups_add
        elif cups_of_with == "take":
            print(" ")
            print(f"I gave you ${CoffeeMachine.money}")
            CoffeeMachine.money = 0