Sure! Here’s a simple Python program that demonstrates all four list operations:

# 1. Create an empty list
empty_list = []
print("Empty list:", empty_list)

# 2. Create a list with elements
my_list = [10, 20, 30, 40, 50]
print("List with elements:", my_list)

# 3. Use * operator
repeated_list = my_list * 2
print("List after using * operator:", repeated_list)

# 4. Reverse a list
my_list.reverse()
print("Reversed list:", my_list)

Output
Empty list: []
List with elements: [10, 20, 30, 40, 50]
List after using * operator: [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
Reversed list: [50, 40, 30, 20, 10]