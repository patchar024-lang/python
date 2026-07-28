actual_cost = float(input("Enter the actual cost of the item:"))
sale_amount = float(input("Please Enter the sale Amount:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit")