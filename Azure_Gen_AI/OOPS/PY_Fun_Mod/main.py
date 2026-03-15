# Python Program: Data Cleaner with Functional Programming 

def clean_and_discount_prices(prices): 
    # Step 1: Remove invalid prices (<= 0) 
    valid_prices = list(filter(lambda x: x > 0, prices))

    # Step 2: Apply 10% discount
    discounted_prices = list(map(lambda x: round(x * 0.9, 2), valid_prices)) 

    return discounted_prices

# Main program 
if __name__ == "__main__":
    # Sample mixed data with valid and invalid price values
    price_list = [250, -45, 0, 100, 499.99, -10, 30]

    print("Original Prices:", price_list)
    final_prices = clean_and_discount_prices(price_list) 
    print("Cleaned & Discounted Prices:", final_prices)

