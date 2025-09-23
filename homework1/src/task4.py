# Function that calculates final price of a product after applying a given discount
def calculate_discount(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("must be numeric types.")
    if discount < 0 or discount > 100:
        raise ValueError("Enter a num between 0 and 100.")
    return price * (1 - discount / 100)

