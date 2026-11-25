def sum(i1, i2):
    result = 0
    for i in range(i1, i2+1):
        result += i
    return result

def main():
    print("Sum from 1 to 10 is", sum(1,10))
    print("Sum from 20 to 37 is", sum(20,37))
    print("Sum from 35 to 49 is", sum(35,49))
    z = sum(0,100)
    z = z + 10
    y = z + sum(30,40)
    print(y)

main()

# sum = 0
# for i in range(1,11):
#     sum += i
# print("Sum from 1 to 10 is ", sum)
#
# sum = 0
# for i in range(20,38):
#     sum += i
# print("Sum from 20 to 37 is", sum)
#
# sum = 0
# for i in range(35, 50):
#     sum += i
# print("Sum from 35 to 49 is", sum)