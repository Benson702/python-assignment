def calculate_discount(price, discount_percent):
    """Calculates the final price after applying discount.
    The fun should take the original price and the discount percentage as parameters.
    If the discount is 20% or higher apply discount otherwise return the original price.
    """
    if discount_percent >= 20:
        discount_amount=price * discount_percent/100
        final_price=price - discount_amount
        return final_price
    else:
        return price
print(calculate_discount(200, 25))  
print(calculate_discount(200, 10))  