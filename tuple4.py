def tuple_product(t):
    product = 1
    for num in t:
        product *= num
    return product


# Example tuple
t = (2, 3, 4, 5)

result = tuple_product(t)
print("Product of tuple elements:", result)
