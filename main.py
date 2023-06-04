from os import system
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def clear():
    system('pause ')
    system('cls')


my_menu = Menu()
coffee_machine = CoffeeMaker()
money_keeper = MoneyMachine()

shutDown = False
while not shutDown:
    clear()
    selection = input(f"What would you like? ({my_menu.get_items()[0:-1]}): ")

    if selection == 'off':
        print('The coffee machine system is shutting down now.\nBye!')
        shutDown = True

    elif selection == 'report':
        coffee_machine.report()
        money_keeper.report()

    else:
        drink = my_menu.find_drink(selection)
        if not drink:
            continue

        if not coffee_machine.is_resource_sufficient(drink):
            continue

        if not money_keeper.make_payment(drink.cost):
            continue

        coffee_machine.make_coffee(drink)