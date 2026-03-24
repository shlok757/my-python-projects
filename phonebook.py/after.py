number = int(input("Enter a number: "))
number = abs(number)

count = 0
if number == 0:
    count = 1
else:
    while number > 0:
        count += 1
        number //= 10   

print("Total number of digits:", count)







