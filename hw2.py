n = int(input())

odd_list = [x for x in range(1, n) if x % 2 != 0]
even_list = [x for x in range(1, n) if x % 2 == 0]

print("Odd numbers:", odd_list)
print("Even numbers:", even_list)