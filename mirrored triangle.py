rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)