"""
operation.py - Module containing core business logic operations
Includes functions for product display, sales, and restocking
"""

from write import save_products, generate_sale_invoice, generate_restock_invoice
from read import load_products
import datetime

def display_products(products):
    """
    Displays available products in a formatted table
    
    Args:
        products (list): List of product dictionaries
    """
    print("\nAvailable Products:")
    print("-" * 80)
    print(
        'Product'.ljust(20) +
        'Brand'.ljust(15) +
        'Price (Rs)'.ljust(12) +
        'In Stock'.ljust(12) +
        'Country'.ljust(15)
    )
    print("-" * 80)
    
    for p in products:
        selling_price = p['cost'] * 2
        print(
            p['name'].ljust(20) +
            p['brand'].ljust(15) +
            str(round(selling_price, 2)).ljust(12) +
            str(p['qty']).ljust(12) +
            p['country'].ljust(15)
        )
    print("-" * 80)

def sell_products(products):
    """
    Handles the product selling process including invoice generation
    
    Args:
        products (list): List of product dictionaries
    
    Returns:
        list: Updated list of products
    """
    customer_name = input("Enter customer name: ").strip()
    total_amount = 0
    invoice_lines = []
    
    while True:
        display_products(products)
        choice = input("\nEnter product number to buy (or '0' to finish): ")
        
        if not choice.isdigit() or int(choice) < 0 or int(choice) > len(products):
            print("Invalid input. Please try again.")
            continue
            
        choice = int(choice)
        if choice == 0:
            break
            
        selected = products[choice-1]
        if selected['qty'] <= 0:
            print(f"Sorry, {selected['name']} is out of stock.")
            continue
            
        try:
            sell_qty = int(input(f"Enter quantity to buy (Available: {selected['qty']}): "))
            if sell_qty <= 0:
                print("Quantity must be positive.")
                continue
                
            free_items = sell_qty // 3
            total_items = sell_qty + free_items
            
            if total_items > selected['qty']:
                print(f"Not enough stock! You requested {sell_qty} (+{free_items} free) = {total_items}, but only {selected['qty']} available.")
                continue
                
            selected['qty'] -= total_items
            subtotal = (selected['cost'] * 2) * sell_qty
            total_amount += subtotal
            
            line = f"{selected['name']}\t{selected['brand']}\t{sell_qty} +{free_items} free\tRs. {subtotal:.2f} (Buy 3 Get 1 Free)"
            invoice_lines.append(line)
            print(f"Added {sell_qty} {selected['name']} (+{free_items} free) to invoice.")
            
        except ValueError:
            print("Invalid quantity entered.")
            continue
            
    if total_amount > 0:
        if generate_sale_invoice(customer_name, invoice_lines, total_amount):
            save_products(products)
            
    return products

def restock_products(products):
    """
    Handles product restocking including new product addition
    
    Args:
        products (list): List of product dictionaries
    
    Returns:
        list: Updated list of products
    """
    vendor_name = input("Enter supplier/vendor name: ").strip()
    total_amount = 0
    invoice_lines = []
    
    while True:
        print("\nRestock Options:")
        print("1. Restock existing product")
        print("2. Add new product")
        print("3. Finish restocking")
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            display_products(products)
            try:
                product_id = int(input("Enter product ID to restock (0 to cancel): "))
                if product_id == 0:
                    continue
                if 1 <= product_id <= len(products):
                    selected = products[product_id-1]
                    add_qty = int(input(f"Enter quantity to add to {selected['name']}: "))
                    if add_qty > 0:
                        selected['qty'] += add_qty
                        subtotal = selected['cost'] * add_qty
                        total_amount += subtotal
                        line = f"{selected['name']}\t{selected['brand']}\t{add_qty}\tRate: Rs. {selected['cost']}  Subtotal: Rs. {subtotal:.2f}"
                        invoice_lines.append(line)
                        print(f"Added {add_qty} {selected['name']} to inventory.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                
        elif choice == '2':
            print("\nAdd New Product:")
            name = input("Product name: ").strip()
            brand = input("Brand: ").strip()
            try:
                cost = float(input("Cost price: "))
                qty = int(input("Initial quantity: "))
                country = input("Country of origin: ").strip()
                
                new_product = {
                    'name': name,
                    'brand': brand,
                    'qty': qty,
                    'cost': cost,
                    'country': country
                }
                products.append(new_product)
                subtotal = cost * qty
                total_amount += subtotal
                line = f"{name}\t{brand}\t{qty}\tRate: Rs. {cost}  Subtotal: Rs. {subtotal:.2f}"
                invoice_lines.append(line)
                print(f"Added new product: {name}")
            except ValueError:
                print("Invalid cost or quantity entered.")
                
        elif choice == '3':
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
    if total_amount > 0:
        if generate_restock_invoice(vendor_name, invoice_lines, total_amount):
            save_products(products)
            
    return products
