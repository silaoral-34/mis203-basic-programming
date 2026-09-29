item1_name = input("Enter item 1 name: ")
item1_qty = int(input("Enter item 1 quantity: "))
item1_price = float(input("Enter item 1 unit price (TRY): "))

item2_name = input("Enter item 2 name: ")
item2_qty = int(input("Enter item 2 quantity: "))
item2_price = float(input("Enter item 2 unit price (TRY): "))

delivery_fee = float(input("Enter delivery fee (TRY): "))
tax_percentage = float(input("Enter tax percentage (%): "))

line1_total = item1_qty * item1_price
line2_total = item2_qty * item2_price
subtotal = line1_total + line2_total
tax_amount = subtotal * (tax_percentage / 100)
final_total = subtotal + tax_amount + delivery_fee

print("\n--- PURCHASE QUOTE ---")
print(f"{item1_name} ({item1_qty} x {item1_price:.2f} TRY): {line1_total:.2f} TRY")
print(f"{item2_name} ({item2_qty} x {item2_price:.2f} TRY): {line2_total:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax ({tax_percentage:.0f}%): {tax_amount:.2f} TRY")
print(f"Delivery Fee: {delivery_fee:.2f} TRY")
print(f"Final Total: {final_total:.2f} TRY")
