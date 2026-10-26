def calculate_subtotal(price, quantity):
    return price * quantity


def get_discount_rate(subtotal):
    if subtotal >= 100:
        return 0.10  # 0. yerine 0.10 olarak düzeltildi
    return 0.0


def calculate_shipping(subtotal):
    if subtotal >= 100:
        return 0
    return 10


def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount = subtotal * discount_rate
    return subtotal - discount + shipping_fee


def print_quote(order_name, price, quantity):
    subtotal = calculate_subtotal(price, quantity)
    discount_rate = get_discount_rate(subtotal)
    shipping_fee = calculate_shipping(subtotal)
    final_total = calculate_final_total(
        subtotal, discount_rate, shipping_fee
    )

    print(f"\n{order_name}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount rate: {discount_rate:.0%}")
    print(f"Shipping fee: ${shipping_fee:.2f}")
    print(f"Final total: ${final_total:.2f}")


# Test checks
assert calculate_subtotal(20, 2) == 40
assert get_discount_rate(100) == 0.10  # Artık hata vermeyecek
assert calculate_shipping(100) == 0
assert calculate_final_total(100, 0.10, 0) == 90

# Sample orders
print_quote("Order 1", 20, 2)
print_quote("Order 2", 30, 4)

