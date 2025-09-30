import json

def get_products():
    while True:
        names = input("Enter product names (comma-separated): ")
        if names.strip():
            return [n.strip() for n in names.split(',')]
        print("Please enter at least one product name.")

def get_prices():
    while True:
        prices = input("Enter product prices (comma-separated): ")
        try:
            price_list = [float(p.strip()) for p in prices.split(',')]
            return price_list
        except ValueError:
            print("Invalid prices. Please enter valid numbers.")

def product_data_transformer():
    names = get_products()
    prices = get_prices()
    if len(names) != len(prices):
        print("Number of products and prices must match.")
        return
    pairs = list(zip(names, prices))
    filtered = list(filter(lambda x: x[1] > 0, pairs))
    result = list(map(lambda x: {"product": x[0], "price": x[1], "discounted": x[1]*0.9}, filtered))
    with open('products.json', 'w') as f:
        json.dump(result, f, indent=2)
    print("First 5 products:")
    print(json.dumps(result[:5], indent=2))
