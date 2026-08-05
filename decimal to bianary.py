def decimal_to_binary(decimal_num):
    # Handle the edge case for 0
    if decimal_num == 0:
        return "0"
        
    binary_str = ""
    
    # Loop until the decimal number becomes 0
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2
        
    return binary_str

# Test the function
number = 13
result = decimal_to_binary(number)
print(f"The binary string for {number} is: {result}")