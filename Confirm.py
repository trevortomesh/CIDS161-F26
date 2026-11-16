continueLoop = 'Y'
bananas = 0

while continueLoop == 'Y':
    bananas += 1
    print("Here's a banana! You have", bananas, "bananas.")
    continueLoop = input("Would you like another banana? Y/N: ")

print("No more bananas for you!")
