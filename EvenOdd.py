# get integer from user
number = eval(input("Enter an integer: "))

# check if divisible by two, if not it's odd.
if number % 2 == 0:
    print(number, "is even")

else:
    print(number, "is odd")