def calculate_discount(price, discount):
    """
    Calculate the final price after applying the discount.
    Supports duck typing for numeric types.
    """
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("Both price and discount must be numeric types.")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    return price * (1 - discount / 100)

