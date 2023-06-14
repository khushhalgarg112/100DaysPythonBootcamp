bill = float(input("Enter your total bill amount ?\n"))
people = int(input("In how many person bill is splitting ?\n"))
amount = bill / people
tip = float(
    input("How much tip you want to give to the waiter ? Ex 10,12 or 15 percent\n")
)
amount += amount * tip / 100
# Here + sign not work because that concatenate str with str not str with float
print("Each have to pay ", round(amount, 2))

# if we convert flaot to int then .9 after 15 terms became the next number
# Ex:-  int(13.99999999999999999999) gives value 14 rather then 13
