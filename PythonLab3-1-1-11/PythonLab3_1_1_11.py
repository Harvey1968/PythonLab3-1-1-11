#3.1.1.11 LAB: Essentials of the if-else statement

income = float(input("Enter your annual income: "))
#if the citizen's income is less than or equal to 85,528 thalers, then the tax will be equal to 18% of the income, 
#additionally a discount is applied to that total: minus 556 thalers and 2 cents (this was the so-called tax relief)
if income <= 85528:
	tax = (income * 0.18) - 556.02
	tax = round(tax, 0) #Use integer NOT a float

#if the income was greater than 85,528 thalers, the tax will be equal to 14,839 thalers and 2 cents,
#plus a fee 32% of the surplus (or remainder) of anything over the 85,528 thalers.
#((100000 - 85528) + 14839.02) * 0.32 = 9380.0 thalers
# 29,311.02 * 0.32 = 9,379.52
#((100000 - 85528) * 0.32) + 14839.02 = 19470.0 thalers
# 4,631.04 + 14839.02 = 19,470.06 
else:
	tax = ((income - 85528) * 0.32) + 14839.02

#If the citizen's tax is below 0 thalers the citizen will not be taxed, all praise the Queen and her generosity!!
if tax < 0:
	tax = 0.0
	print("You are below the tax bracket and will not be charged, therefore...")

tax = round(tax, 0) #Use integer NOT a float
print("Your tax is:", tax, "thalers")
