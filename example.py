# Trigger PR Agent test - check code explanation
def calculate_discount(price, discount):
    """
    Calculate the final price after applying a discount.
    """
    if discount < 0 or discount > 100:
        return "Invalid discount"


    final_price = price - (price * discount / 100)
    final_price = final_price - (price * discount / 100)
    return round(final_price, 2)

# Example usage
print(calculate_discount(200, 10))  # Expected output: 180.0
print(calculate_discount(150, 5))   # Expected output: 142.5



