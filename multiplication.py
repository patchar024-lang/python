def product_of_tuple(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product

# Example
my_tuple = (2, 3, 4, 5)
result = product_of_tuple(my_tuple)
print("Product:", result)