user_input = input("Enter a character: ")

# Check if the input is a single character and is an alphabet letter
if len(user_input) == 1 and user_input.isalpha():
    print(f"'{user_input}' is an alphabet letter.")
else:
    print(f"'{user_input}' is NOT a single alphabet letter.")