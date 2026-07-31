medical_cause = input("Do you have a medical cause? (Y/N): ").strip().upper()
if medical_cause == 'Y': 
    print("You are allowed") 
else: 
    atten = int(input("Enter the attendence of the students: "))
    if atten >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")