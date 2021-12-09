#! python3

import pyinputplus as pyip

def itemCost(i):
    switcher = {
        'wheat': 3.00,
        'white': 2.00,
        'sourdough': 3.50,
        'chicken': 1.00,
        'turkey': 1.25,
        'ham': 0.75,
        'tofu': 2.00,
        'cheddar': 0.50,
        'Swiss': 0.75,
        'mozzarella': 0.60,
    }
    return switcher.get(i)


print("Select bread:")
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
breadCost = itemCost(bread)

print("Select protein:")
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
proteinCost = itemCost(protein)

cheese = pyip.inputYesNo("Do you want cheese (Y/N): ")
if cheese == 'yes':
    print("Select cheese:")
    cheeseChoice = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    cheeseCost = itemCost(cheese)
else:
    cheeseChoice = 'none'
    cheeseCost = 0.0

extras = pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato (Y/N): ")
if extras == 'yes':
    extrasCost = 1.00
else:
    extrasCost = 0.0


quantity = pyip.inputInt("How many? ")

total = (breadCost + proteinCost + cheeseCost + extrasCost) * float(quantity)

print(f'''
Order:
    Bread = {bread} (£{breadCost})
    Protein = {protein} (£{proteinCost})
    Cheese = {cheese}
        Cheese Option = {cheeseChoice} (£{cheeseCost})
    Extras = {extras} (£{extrasCost})
Total = £{total}
''')



