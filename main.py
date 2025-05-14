"""
main.py - Main entry point for the We Care Cosmetics shop system
Handles the main menu and program flow
"""

from operation import display_products, sell_products, restock_products
from read import load_products

def show_welcome():
    """Displays the welcome banner and shop information"""
    print("\n" + "*" * 50)
    print("\t\tWE CARE COSMETICS".center(50))
    print("*" * 50)
    print("\tDURBARMARG, KATHMANDU | Phone: 9842322211".center(50))
    print("~" * 50)
    print("\tA VERY DELIGHTFUL GREETINGS!".center(50))
    print("\tCrafted for the queen in you".center(50))
    print("~" * 50)
    print("Discover our Signature Collection".center(50) + "\n")

def main():
    """Main program loop"""
    show_welcome()
    products = load_products()
    
    while True:
        print("\n==== Main Menu ====")
        print("1. View Products")
        print("2. Sell Products")
        print("3. Restock Products")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            display_products(products)
        elif choice == "2":
            products = sell_products(products)
        elif choice == "3":
            products = restock_products(products)
        elif choice == "4":
            print("\nThank you for using We Care Cosmetics system!")
            print("Have a wonderful day!\n")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
