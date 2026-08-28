def calculate_due_amount(total_due, bill_payments):
    print(f"Initial Total Due: ${total_due:.2f}\n")
    
    for payment in bill_payments:
        # Scenario 1: Using 'pass'
        # If the payment is 0, we acknowledge it but do nothing and move on
        if payment == 0:
            print("Processing: $0 payment detected.")
            pass 
            print("   (Pass executed: No changes made to the balance)")
            
        # Scenario 2: Using 'continue'
        # If a payment is negative, it's invalid. We skip it and move to the next item
        elif payment < 0:
            print(f"Warning: Invalid negative payment ${payment} skipped.")
            continue
            
        # Scenario 3: Regular processing
        else:
            total_due -= payment
            print(f"Processed: Paid ${payment:.2f}. Remaining Due: ${total_due:.2f}")
            
        # Scenario 4: Using 'break'
        # If the due amount is completely paid off or overpaid, we stop processing completely
        if total_due <= 0:
            if total_due < 0:
                overpayment = abs(total_due)
                print(f"\nAccount overpaid! Refund customer: ${overpayment:.2f}")
                total_due = 0  # Reset due amount to 0
            else:
                print("\nAccount fully paid!")
            break

    print(f"\nFinal Customer Due Amount: ${total_due:.2f}")

# --- Test Data ---
# Starting balance the customer owes
starting_balance = 500.00  

# A list of transactions to process
# - 150.00: Normal payment
# - 0.00: Triggers 'pass'
# - -50.00: Triggers 'continue' (skipped)
# - 350.00: Pays off the remaining balance, triggers 'break'
# - 100.00: Will never be reached because 'break' stops the loop
transactions = [150.00, 0.00, -50.00, 350.00, 100.00]

# Run the program
calculate_due_amount(starting_balance, transactions)