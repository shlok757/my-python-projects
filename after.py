number = int(input("Enter the number: "))
power = int(input("Enter the power: "))

result = 1
i = 1
while i <= power:
    result = result * number
    i += 1

print(f"{number} raised to the power {power} is {result}")