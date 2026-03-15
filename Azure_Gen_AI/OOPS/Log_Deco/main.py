# Logging Decorator Lab - Python Program

import logging 
from functools import wraps 
from datetime import datetime

# Step 1: Configure logging 
logging.basicConfig(filename='function_calls.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Step 2: Define the decorator
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Called function: {func.__name__} with args: {args} and kwargs: {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Function {func.__name__} returned: {result}')
        return result
    return wrapper

# Step 3: Apply decorator to functions 
@log_function_call 
def add(a, b):     
    return a + b  

@log_function_call 
def multiply(x, y):     
    return x * y 
 
# Step 4: Main program 
if __name__ == "__main__":
    sum_result = add(5, 3) 
    product_result = multiply(4, 7) 
    print(f'Sum: {sum_result}, Product: {product_result}')
    print("Check 'function_calls.log' for logged output.") 

