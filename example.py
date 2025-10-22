def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        return "Invalid discount"
    final_price = price - (price * discount / 100)
    return round(final_price, 2)

print(calculate_discount(200, 10))
print(calculate_discount(150, 5))
print("code review test")


