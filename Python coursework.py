#defining a function
def main():
    #prints a line of star just for design
    print("***********************************") 
    print("\t\tWE CARE COSMETICS")                               #to print centered title 
    print("***********************************")
    print("\t\tDURBARMARG, KATHMANDU | Phone no: 9842322211")        #\t used for proper spacing 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t A VERY DELIGHTFUL GREETINGS! Crafted for the queen in you")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Discover our Signature Collection")

#new function that reads product data from a file
def load_products():
    #opens the file named products.txt f is just a variable name for the file
    with open("products.txt", "r") as f:

         # reads all lines from the file and stores them in list called lines.
        lines = f.readlines()                    
    products = []   #creats an empty list to store each product info

     #is a loop and goes through each line in file one by one
    for line in lines:                           
        name, brand, qty, cost, country = line.replace(" ", "").split(",") #splits each line by comma into five parts,       
        product = {
            "name": name,
            "brand": brand,
            "qty": int(qty),
            "cost": float(cost),
            "country": country
        }
        products.append(product)
        
    return products #sends the full list of products back to whereever the fun was called

#starts a new function to show the list of product on the screen
def display_products(products): 
    print("\nAvailable Products:") #prints a header line 
    print("-" * 80) #prints a line of 80 dashes for neat formatting 
    print(                                         #prints a row with column title 
    'Product' + ' ' * (20 - len('Product')) +
    'Brand' + ' ' * (15 - len('Brand')) +
    'Price (Rs)' + ' ' * (10 - len('Price (Rs)')) +
    'In Stock' + ' ' * (10 - len('In Stock')) +
    'Country' + ' ' * (15 - len('Country')) 
) 
    print("-" * 80)
    for p in products: #Loops through each product in the list and displays its info.
        selling_price = p['cost'] * 2 #Calculates the selling price by doubling the cost.
        print(
    name + ' ' * (20 - len(name)) +  
    brand + ' ' * (15 - len(brand)) +  
    str(selling_price) + ' ' * (10 - len(str(selling_price))) +  
    str(qty) + ' ' * (10 - len(str(qty))) +  
    country + ' ' * (10 - len(country))  
)
 
    print("-" * 80)


import datetime

# Function to load products from the file into a list
def load_products():
    products = []
    with open("products.txt", "r") as f:
        for line in f:
            if line.endswith("\n"):            # manually remove newline
                line = line[:-1]
            parts = line.split(",")            # don't touch internal spaces
            if len(parts) == 5:                # only process valid lines
                name = parts[0]
                brand = parts[1]
                qty = int(parts[2])
                cost = float(parts[3])
                country = parts[4]
                products.append({
                    'name': name,
                    'brand': brand,
                    'qty': qty,
                    'cost': cost,
                    'country': country
                })
    return products

# Function to save updated product data to file
def save_products(products):
    """Saves products to file using only basic string operations"""
    with open("products.txt", "w") as f:
        for p in products:
            # Build line using only concatenation
            line = p['name'] + "," + p['brand'] + "," 
            line += str(p['qty']) + "," + str(p['cost']) + "," 
            line += p['country'] + "\n"
            f.write(line)

# Function to display current products
def display_products(products):
    print("\nAvailable Products:")
    print("Product\t\t\t Brand\t\tPrice (Rs)\tStock\t Country")
    for p in products:
        selling_price = p['cost'] * 2
        print(p['name'] + "\t\t" + p['brand'] + "\t\t" + str(selling_price) + "\t\t" + str(p['qty']) + "\t" + p['country'])
    print()

# Function to sell products and generate invoice
def sell_products(products):
    customer_name = input("Enter customer name: ")
    total_amount = 0
    invoice_lines = []

    while True:
        print("\nAvailable Products:")
        print("-" * 80)
        no = "No."
        product = "Product"
        brand = "Brand"
        price = "Price (Rs)"
        in_stock = "In Stock"
        country = "Country"

# Print the header with manual spacing
        print(
            no + " " * (5 - len(no)) +
            product + " " * (20 - len(product)) +
            brand + " " * (15 - len(brand)) +
            price + " " * (10 - len(price)) +
            in_stock + " " * (10 - len(in_stock)) +
            country  # Last column doesn’t need extra padding
        )
        print("-" * 80)
        i = 0
        while i < len(products):
            p = products[i]
        
            no = str(i + 1)
            name = p['name']
            brand = p['brand']
            price = str(p['cost'] * 2)
            qty = str(p['qty'])
            country = p['country']

            # Set column widths
            no_width = 5
            name_width = 20
            brand_width = 15
            price_width = 10
            qty_width = 10
            country_width = 10  # last column doesn’t need padding, but included for clarity

            # Manual alignment using spaces
            line = (
                no + " " * (no_width - len(no)) +
                name + " " * (name_width - len(name)) +
                brand + " " * (brand_width - len(brand)) +
                price + " " * (price_width - len(price)) +
                qty + " " * (qty_width - len(qty)) +
                country
            )

            print(line)
            i += 1

        print("-" * 80)

        choice = input("Enter product number to buy (or '0' to finish): ")
        if not choice.isdigit() or int(choice) < 0 or int(choice) > len(products):
            print("Invalid input. Try again.")
            continue

        choice = int(choice)
        if choice == 0:
            break

        selected_product = products[choice - 1]
        if selected_product['qty'] == 0:
            print("Sorry, this product is out of stock.")
            continue

        try:
            sell_qty = int(input("Enter quantity to sell for " + selected_product['name'] + " (Available: " + str(selected_product['qty']) + "): "))
        except ValueError:
            print("Invalid quantity.")
            continue

        if sell_qty <= 0:
            print("Quantity must be greater than zero.")
            continue

        free_items = sell_qty // 3
        total_items = sell_qty + free_items

        if total_items > selected_product['qty']:
            print("Not enough stock available! You requested " + str(sell_qty) + " (+" + str(free_items) + " free) = " + str(total_items) + ", but only " + str(selected_product['qty']) + " in stock.")
            continue

        selected_product['qty'] -= total_items
        cost_price = selected_product['cost'] * 2
        subtotal = cost_price * sell_qty
        total_amount += subtotal

        line = line = selected_product['name'] + "\t" + selected_product['brand'] + "\t" + str(sell_qty) + " +" + str(free_items) + " free\t Rs. %.2f (Buy 3 Get 1 Free Applied)" % round(subtotal, 2)
        invoice_lines.append(line)
        print("Product added to invoice.")

    #After customer finishes buying
        if total_amount > 0:
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = "invoice_sale_" + customer_name + "_" + timestamp + ".txt"

            try:
                with open(filename, "w") as f:
                    f.write("Customer: " + customer_name + "\n")
                    f.write("Date: " + timestamp + "\n\n")
                    f.write("Sold Items:\n")
                    for line in invoice_lines:
                        f.write(line + "\n")
                    f.write("\nTotal Amount (excluding free items): Rs. " + str(round(total_amount, 2)) + "\n")
                print("Invoice saved to " + filename)
            except Exception as e:
                print("Error saving invoice:", e)

                save_products(products)

# Function to restock and generate invoice
def restock_products(products):
    vendor_name = input("Enter supplier/vendor name: ")
    total_amount = 0
    invoice_lines = []

    while True:
        print("\nRestock Options:")
        print("1. Restock existing products")
        print("2. Add new product")
        print("3. Finish restocking")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Display products with manual formatting
            print("\nAvailable Products:")
            print("-" * 80)
            header = "ID" + " "*(5-2) + "Product" + " "*(20-7) 
            header += "Brand" + " "*(15-5) + "Price" + " "*(10-5) + "Stock"
            print(header)
            print("-" * 80)
            
            # Display each product with manual spacing
            counter = 1
            for p in products:
                id_part = str(counter) + " "*(5-len(str(counter)))
                name_part = p['name'] + " "*(20-len(p['name']))
                brand_part = p['brand'] + " "*(15-len(p['brand']))
                price_part = str(p['cost']) + " "*(10-len(str(p['cost'])))
                stock_part = str(p['qty'])
                
                print(id_part + name_part + brand_part + price_part + stock_part)
                counter += 1
            print("-" * 80)

            # Restock logic
            try:
                product_id = int(input("Enter product ID to restock (0 to cancel): "))
                if product_id == 0:
                    continue
                if product_id >= 1 and product_id <= len(products):
                    selected = products[product_id-1]
                    print("\nSelected: " + selected['name'] + " (" + selected['brand'] + ") - Current stock: " + str(selected['qty']))
                    add_qty = int(input("Enter quantity to add: "))
                    if add_qty > 0:
                        selected['qty'] += add_qty
                        save_products(products)  # Save immediately
                        subtotal = selected['cost'] * add_qty
                        total_amount += subtotal
                        line = selected['name'] + "\t" + selected['brand'] + "\t" 
                        line += str(add_qty) + "\t Rate: Rs. " + str(selected['cost']) 
                        line += "  Subtotal: Rs. " + str(int(subtotal*100)/100)  # Manual rounding
                        invoice_lines.append(line)
                        print("Product restocked successfully!")
                else:
                    print("Invalid product ID!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == '2':
            print("\nAdd New Product:")
            name = input("Enter product name: ")
            brand = input("Enter brand: ")
            try:
                cost = float(input("Enter cost price: "))
                qty = int(input("Enter initial quantity: "))
                country = input("Enter country of origin: ")
                
                new_product = {
                    'name': name,
                    'brand': brand,
                    'qty': qty,
                    'cost': cost,
                    'country': country
                }
                products.append(new_product)
                save_products(products)  # Save immediately
                
                subtotal = cost * qty
                total_amount += subtotal
                line = name + "\t" + brand + "\t" + str(qty) + "\t Rate: Rs. " 
                line += str(cost) + "  Subtotal: Rs. " + str(int(subtotal*100)/100)
                invoice_lines.append(line)
                print("New product added successfully!")
            except ValueError:
                print("Invalid input for cost or quantity!")

        elif choice == '3':
            break

        else:
            print("Invalid choice!")

    if total_amount > 0:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "invoice_restock_" + vendor_name + "_" + timestamp + ".txt"
        with open(filename, "w") as f:
            f.write("Supplier: " + vendor_name + "\n")
            f.write("Date: " + str(datetime.datetime.now()) + "\n\n")
            f.write("Restocked Items:\n")
            for line in invoice_lines:
                f.write(line + "\n")
            f.write("\nTotal Restock Cost: Rs. " + str(int(total_amount*100)/100) + "\n")
        print("Restock invoice saved to " + filename)

# Main menu
def main():
    products = load_products()
    while True:
        print("\n==== Welcome to We Care Cosmetics ====")
        print("1. View Products")
        print("2. Buy Products")
        print("3. Restock Products")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_products(products)
        elif choice == "2":
            sell_products(products)
        elif choice == "3":
            restock_products(products)
        elif choice == "4":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


    
main()
products = load_products()
display_products(products)


          
