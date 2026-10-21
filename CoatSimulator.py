temperature = eval(input("Give me a temperature in F: "))
isRaining = eval(input("Is it raining out? (type True or False): "))

#isCold = True
#isRaining = True
#isCold = True
#isRaining = True

if temperature <= 55:
    print("Bring a coat!")

else:
    print("Don't bring a coat!")

# if temperature > 55:
#     print("Don't bring a coat!")

if isRaining:
    print("Bring an umbrella!")

else:
    print("Don't bring an umbrella!")

