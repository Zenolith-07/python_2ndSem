"""
read.py - Module for handling all read operations in the cosmetics shop system
Includes functions for loading product data
"""

def load_products(filename="products.txt"):
    """
    Loads product data from a text file
    
    Args:
        filename (str): Name of file to read from (default: products.txt)
    
    Returns:
        list: List of product dictionaries
    """
    products = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 5:
                        product = {
                            'name': parts[0],
                            'brand': parts[1],
                            'qty': int(parts[2]),
                            'cost': float(parts[3]),
                            'country': parts[4]
                        }
                        products.append(product)
        return products
    except FileNotFoundError:
        print("Products file not found. Starting with empty inventory.")
        return []
    except Exception as e:
        print(f"Error loading products: {e}")
        return []
