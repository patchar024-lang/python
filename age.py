try:
    # 1. Ask the user to enter their age
    user_input = input("Please enter your age: ")
    
    # 2. Convert the input into an integer
    age = int(user_input)
    
    # 3. Check for logical errors in the age value
    if age < 0:
        print("❌ Error: Age cannot be negative.")
    elif age > 120:
        print("❌ Error: Please enter a realistic age (120 or below).")
    else:
        print(f"✅ Valid age entered: {age}")
        
        # 4. Check if the age is even or odd
        if age % 2 == 0:
            print("🔢 Your age is an EVEN number.")
        else:
            print("🔢 Your age is an ODD number.")
            