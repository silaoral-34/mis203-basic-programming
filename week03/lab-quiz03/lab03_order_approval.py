order_amount = float(input("Enter the order amount (TRY): "))
available_stock = int(input("Enter the available stock: "))
requested_quantity = int(input("Enter the requested quantity: "))

membership_input = input("Is the customer a member? (yes/no): ").strip().lower()
is_member = (membership_input == "yes")

if requested_quantity <= 0 or requested_quantity > available_stock:
    print("Order rejected: Invalid quantity or insufficient stock.")
else:
    
    final_price = order_amount
    
   
    if order_amount >= 500 and is_member:
        final_price = order_amount * 0.90
        print("Order approved: Reason - Valid stock and 10% member discount applied.")
    else:
        print("Order approved: Reason - Valid stock (no discount applied).")
        
    
    print(f"Final Price: {final_price:.2f} TRY")





