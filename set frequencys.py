data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

value = int(input("Enter value: "))

count = list(data.values()).count(value)

print("Frequency:", count)