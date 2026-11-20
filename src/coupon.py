def calculate_price(original_price, discount_rate=0.20):
    if original_price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_rate <= 1:
        raise ValueError("Invalid discount rate")
    return round(original_price * (1 - discount_rate), 2)


if __name__ == "__main__":
    print("Final price:", calculate_price(100))
