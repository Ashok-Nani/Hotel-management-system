import datetime

# Use a dictionary for a cleaner, scalable menu and price mapping.
# All keys are converted to lowercase for consistent lookups.
MENU = {
    "biryani": 100,
    "chapathi": 50,
    "parota": 50,
    "ragimudda": 30,
    "whiterice": 60
}

DISCOUNT_THRESHOLD = 999
DISCOUNT_AMOUNT = 200

def display_menu():
    """Displays the menu items and their prices."""
    print("\n--- Welcome to Our Hotel ---")
    print("Available Menu Items:")
    # Calculate max length of item names for neat formatting
    max_len = max(len(item) for item in MENU.keys())
    for item, price in MENU.items():
        # Capitalize for display, but keep lowercase in the dictionary for lookup
        print(f"  {item.capitalize():<{max_len}} : Rs. {price}")
    print("----------------------------")

def get_order_details():
    """Handles user input for the order item and quantity."""
    
    # 1. Get the order item
    while True:
        user_order = input("Enter your order item: ").lower().strip()
        if user_order in MENU:
            print(f"'{user_order.capitalize()}' order is received successfully.")
            break
        else:
            print(f"Sorry, '{user_order.capitalize()}' is not available. Please choose from the menu.")
    
    # 2. Get the quantity
    while True:
        try:
            # We use the valid user_order from the previous step
            how_many = int(input(f"How many '{user_order.capitalize()}' you want?: "))
            if how_many > 0:
                return user_order, how_many
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Sorry, please enter a valid positive number for the quantity.")

def calculate_bill(order_item, quantity):
    """Calculates the total bill and applies the discount."""
    price_per_item = MENU[order_item]
    initial_total = price_per_item * quantity
    
    final_bill = initial_total
    discount_applied = 0
    
    print(f"\nSubtotal for {quantity} x {order_item.capitalize()}: Rs. {initial_total}")
    
    if initial_total > DISCOUNT_THRESHOLD:
        final_bill = initial_total - DISCOUNT_AMOUNT
        discount_applied = DISCOUNT_AMOUNT
        print(f"--- Special Offer Applied ---")
        print(f"Reducing Rs. {DISCOUNT_AMOUNT} for bills above Rs. {DISCOUNT_THRESHOLD}.")
        print(f"Final payable bill: Rs. {final_bill}")
    
    return initial_total, final_bill, discount_applied

def generate_bill_file(initial_total, final_bill, discount_applied, order_item, quantity):
    """Writes the bill details to a file."""
    
    bill_response = input("Do you want to generate a bill receipt? (yes/no): ").lower().strip()
    
    if bill_response == "yes":
        try:
            date_time = datetime.datetime.now()
            
            with open("bill.txt", "w") as f:
                f.write("---------------- HOTEL RECEIPT ----------------\n")
                f.write(f"Date/Time: {date_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("-----------------------------------------------\n")
                f.write(f"Item Ordered: {order_item.capitalize()}\n")
                f.write(f"Quantity: {quantity}\n")
                f.write(f"Price per Unit: Rs. {MENU[order_item]}\n")
                f.write("-----------------------------------------------\n")
                f.write(f"Initial Total: Rs. {initial_total}\n")
                f.write(f"Discount Applied: - Rs. {discount_applied}\n")
                f.write(f"FINAL PAYABLE AMOUNT: Rs. {final_bill}\n")
                f.write("---------------- Thank You! -------------------\n")
                
            print("\nReceipt generated successfully in 'bill.txt'!.")
        except IOError:
            print("Error: Could not write the bill to 'bill.txt'.")
    else:
        print("\nThanks for visiting!!")

def main():
    """Main function to run the hotel billing program."""
    display_menu()
    
    # Get validated order and quantity
    order_item, quantity = get_order_details()
    
    # Calculate totals
    initial_total, final_bill, discount_applied = calculate_bill(order_item, quantity)
    
    # Generate receipt
    generate_bill_file(initial_total, final_bill, discount_applied, order_item, quantity)

if __name__ == "__main__":
    main()