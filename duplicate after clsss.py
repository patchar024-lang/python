# Test dictionary
test_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

# Value to check
value_to_check = 10

# Count frequency
frequency = list(test_dict.values()).count(value_to_check)

print(f"The value {value_to_check} appears {frequency} times.")