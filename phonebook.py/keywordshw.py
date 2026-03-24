bill_amount = float(input("Enter total bill amount: "))
paid_amount = float(input("Enter amount paid by customer: "))

due_amount = bill_amount - paid_amount

if due_amount > 0:
    print(f"Customer due amount is: {due_amount:.2f}")
elif due_amount == 0:
    print("No due amount. Bill is fully paid.")
else:
    print(f"No due. Customer should receive change: {-due_amount:.2f}")