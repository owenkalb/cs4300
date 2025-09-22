# Function that calculates final price of a product after applying a a given discount
#percentage inside of a function named calculate_discount
def calculate_discount(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("Both price and discount must be numeric types.")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    return price * (1 - discount / 100)

