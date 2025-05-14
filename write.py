"""
write.py - Module for handling all write operations in the cosmetics shop system
Includes functions for saving products and generating invoices
"""

import datetime

def save_products(products, filename="products.txt"):
    """
    Saves product data to a text file
    
    Args:
        products (list): List of product dictionaries
        filename (str): Name of file to save to (default: products.txt)
    """
    try:
        with open(filename, "w") as f:
            for p in products:
                line = f"{p['name']},{p['brand']},{p['qty']},{p['cost']},{p['country']}\n"
                f.write(line)
    except Exception as e:
        print(f"Error saving products: {e}")

def generate_sale_invoice(customer_name, invoice_lines, total_amount):
    """
    Generates a sales invoice file
    
    Args:
        customer_name (str): Name of customer
        invoice_lines (list): List of purchased items
        total_amount (float): Total sale amount
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"invoice_sale_{customer_name}_{timestamp}.txt"
        
        with open(filename, "w") as f:
            # Header section
            f.write("="*50 + "\n")
            f.write("WE CARE COSMETICS\n".center(50) + "\n")
            f.write("DURBARMARG, KATHMANDU\n".center(50))
            f.write("Phone: 9842322211\n".center(50))
            f.write("="*50 + "\n\n")
            
            # Customer info
            f.write(f"Customer: {customer_name}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-"*50 + "\n")
            
            # Items header
            f.write("ITEM".ljust(20))
            f.write("BRAND".ljust(15))
            f.write("QTY".center(8))
            f.write("PRICE".rjust(10))
            f.write("TOTAL".rjust(12) + "\n")
            f.write("-"*50 + "\n")
            
            # Items list
            for line in invoice_lines:
                parts = line.split("\t")
                if len(parts) >= 4:
                    f.write(parts[0].ljust(20))  # Product name
                    f.write(parts[1].ljust(15))  # Brand
                    f.write(parts[2].center(8))  # Quantity
                    f.write(parts[3].split()[0].rjust(10))  # Price
                    if len(parts) > 3:
                        total = parts[3].split()[-1].replace("Rs.","").strip()
                        f.write(total.rjust(12) + "\n")  # Total
            
            # Footer
            f.write("-"*50 + "\n")
            f.write("TOTAL AMOUNT:".rjust(40))
            f.write(f"Rs. {total_amount:.2f}".rjust(10) + "\n")
            f.write("="*50 + "\n")
            
        print(f"\nInvoice successfully saved as: {filename}")
        return True
    except Exception as e:
        print(f"Error generating invoice: {e}")
        return False

def generate_restock_invoice(vendor_name, invoice_lines, total_amount):
    """
    Generates a restock invoice file
    
    Args:
        vendor_name (str): Name of supplier/vendor
        invoice_lines (list): List of restocked items
        total_amount (float): Total restock amount
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"invoice_restock_{vendor_name}_{timestamp}.txt"
        
        with open(filename, "w") as f:
            f.write("="*50 + "\n")
            f.write("WE CARE COSMETICS - RESTOCK\n".center(50))
            f.write("="*50 + "\n\n")
            f.write(f"Supplier: {vendor_name}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-"*50 + "\n")
            f.write("ITEM".ljust(25))
            f.write("QTY".ljust(10))
            f.write("UNIT PRICE".ljust(15))
            f.write("TOTAL".rjust(10) + "\n")
            f.write("-"*50 + "\n")
            
            for line in invoice_lines:
                parts = line.split("\t")
                if len(parts) >= 3:
                    f.write(parts[0].ljust(25))
                    f.write(parts[2].split()[0].ljust(10))
                    f.write(parts[3].split(":")[1].strip().ljust(15))
                    f.write(parts[3].split("Subtotal:")[1].strip().rjust(10) + "\n")
            
            f.write("-"*50 + "\n")
            f.write("TOTAL RESTOCK COST:".rjust(40))
            f.write(f"Rs. {total_amount:.2f}".rjust(10) + "\n")
            f.write("="*50 + "\n")
            
        print(f"\nRestock invoice saved as: {filename}")
        return True
    except Exception as e:
        print(f"Error generating restock invoice: {e}")
        return False
