BurgerNum = int(input())
SideNum = int(input())
DrinkNum = int(input())
DessertNum = int(input())

if BurgerNum == 1 : 
	BurgerCal = 461
elif BurgerNum == 2 : 
	BurgerCal = 431
elif BurgerNum == 3 : 
	BurgerCal = 420
elif BurgerNum == 4 : 
	BurgerCal = 0

if DrinkNum == 1 : 
	DrinkCal = 130
elif DrinkNum == 2 : 
	DrinkCal = 160
elif DrinkNum == 3 : 
	DrinkCal = 118
elif DrinkNum == 4 : 
	DrinkCal = 0

if SideNum == 1 : 
	SideCal = 100
elif SideNum == 2 : 
	SideCal = 57
elif SideNum == 3 : 
	SideCal = 70
elif SideNum == 4 : 
	SideCal = 0

if DessertNum == 1 : 
	DessertCal = 167
elif DessertNum == 2 : 
	DessertCal = 266
elif DessertNum == 3 : 
	DessertCal = 75
elif DessertNum == 4 : 
	DessertCal = 0

Cal = BurgerCal + DrinkCal + SideCal + DessertCal
Answer = 'Your total Calorie count is ' + str(Cal) + "."

print(Answer)
