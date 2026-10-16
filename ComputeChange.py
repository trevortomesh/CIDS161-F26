# Receive the amount
amount = eval(input("Enter an amount (ex. 11.56): "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the nickels
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find number of pennies
numberOfPennies = remainingAmount

# Display results
print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickels, "nickels\n",
      "\t", numberOfPennies, "pennies")