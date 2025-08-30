print("Simple Calculator")
print("Operations: + , - , * , / , %")

# Taking inputs
num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

# Performing calculation
if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero.")
elif op == "%":
    if num2 != 0:
        print("Result =", num1 % num2)
    else:
        print("Error! Modulo by zero.")
else:
    print("Invalid operation!")
    