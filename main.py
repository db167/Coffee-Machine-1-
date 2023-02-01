from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine() 
machineOn = True
while machineOn:
	options = menu.get_items()
	coffeeChoice = input(f"What would you like? {options}:")
	if coffeeChoice == "off":
		machineOn = False
	elif coffeeChoice == "report":
		coffeeMaker.report()
		moneyMachine.report()
	else:
		coffee = menu.find_drink(coffeeChoice)
		if coffeeMaker.is_resource_sufficient(coffee) and moneyMachine.make_payment(coffee.cost):
			coffeeMaker.make_coffee(coffee)