from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# j=input("what u wanna drink espresso,latte,cappucino")
is_on=True
coffeemaker=CoffeeMaker()
coffeemaker.report()
menu=Menu()

money=MoneyMachine()
money.report()

while is_on:
  options =menu.get_items()
  order=input(f"which u wanna drink {options}")
  if order =="report":
    coffeemaker.report()
    money.report()
  elif order=="off":
    is_on=False
  else:
    t=menu.find_drink(order)
    if coffeemaker.is_resource_sufficient(t) and money.make_payment(t.cost):
     coffeemaker.make_coffee(t)
  
    

 
  
  