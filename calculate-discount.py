def calculate_discount(price, discount_percent):
    """Calculates the final price after applying discount.
    The fun should take the original price and the discount percentage as parameters.
    If the discount is 20% or higher apply discount otherwise return the original price.
    """
    if price < 0 or discount_percent >= 20:
        discount_amount=price * discount_percent/100
        final_price=price - discount_amount
        return final_price
    else:
        return price
original_price = float(input("Enter the original_price"))
discount_percent = float(input("Enter the discountt_percent"))

final_price = calculate_discount(original_price, discount_percent)
if discount_percent >= 20:
    print(f"Final price applying a {discount_percent}% discount: ${final_price}")
else:
    print(f"No discount applied. original price: ${original_price:.2f}")
