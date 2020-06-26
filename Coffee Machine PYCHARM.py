class CoffeeMachine:
    espresso = [250, 0, 16, 4]  # Water, Milk, Coffee Beans, Price
    latte = [350, 75, 20, 7]
    cappuccino = [200, 100, 12, 6]

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print('\nThe coffee machine has:\
        \n{} of water.\
        \n{} of milk.\
        \n{} of coffee beans.\
        \n{} of disposable cups.\
        \n${} of money.\n'.format(self.water, self.milk, self.beans, self.cups, self.money))

    def buy(self):
        election = input(f'\nWhat do you want to buy?:\n1 - espresso\n2 - latte\n3 - cappuccino\nback - to main menu'
                         f'\n> ')
        if election == '1':
            election = CoffeeMachine.espresso
        elif election == '2':
            election = CoffeeMachine.latte
        elif election == '3':
            election = CoffeeMachine.cappuccino
        else:
            return print('')

        while True:
            if self.water < election[0]:
                status = "water"
                break
            if self.milk < election[1]:
                status = "milk"
                break
            if self.beans < election[2]:
                status = "beans"
                break
            if self.cups < 1:
                status = "cups"
                break
            else:
                status = "possible"
                break
        if status == "possible":
            self.water -= election[0]
            self.milk -= election[1]
            self.beans -= election[2]
            self.money += election[3]
            self.cups -= 1
            print(f'\nI have enough resources.\n'
                  f'\nStarting to make a coffee'
                  f'\nGrinding coffee beans'
                  f'\nBoiling water'
                  f'\nMixing boiled water with crushed coffee beans'
                  f'\nPouring coffee into the cup'
                  f'\nPouring some milk into the cup'
                  f'\nCoffee is ready!\n')
        else:
            print(f"\nSorry, not enough {status}!\n")

    def fill(self):
        self.water += int(input("\nWrite how many ml of water do you want to add:\n> "))
        self.milk += int(input("Write how many ml of milk do you want to add:\n> "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
        print(f'\nOperation carried out successfully.\n')


V1 = CoffeeMachine(400, 540, 120, 9, 550)
print(f'Welcome!')
while True:
    option = input(f'Write action (buy, fill, take, remaining, exit).\n> ')
    if option == "buy":
        V1.buy()
    elif option == "fill":
        V1.fill()
    elif option == "take":
        print(f'\nI gave you ${V1.money}\n')
        V1.money -= V1.money
    elif option == "remaining":
        V1.remaining()
    elif option == "exit":
        break
    else:
        print(f'\nError: undefined action'
              f'\nPlease, select an available action.\n')
