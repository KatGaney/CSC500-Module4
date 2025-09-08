# This class defines a single item for a shopping cart.
class ItemToPurchase:
    """
    Represents an item to be purchased with a name, price, and quantity.
    """
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        """
        Initializes the item with a name, price, and quantity.
        The default constructor sets the values to "none", 0.0, and 0.
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        """
        Calculates and prints the cost of the item.
        """
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

# Main program section to handle user input and calculations.
if __name__ == "__main__":
    
    # --- Item 1 ---
    print("Item 1")
    print("Enter the item name:")
    item1_name = input()
    print("Enter the item price:")
    item1_price = float(input())
    print("Enter the item quantity:")
    item1_quantity = int(input())
    
    # Create the first ItemToPurchase object.
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    # --- Item 2 ---
    print("\nItem 2")
    print("Enter the item name:")
    item2_name = input()
    print("Enter the item price:")
    item2_price = float(input())
    print("Enter the item quantity:")
    item2_quantity = int(input())

    # Create the second ItemToPurchase object.
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)
    
    # --- Total Cost Calculation and Output ---
    print("\nTOTAL COST")
    
    # Print the cost of each item.
    item1.print_item_cost()
    item2.print_item_cost()
    
    # Calculate and print the total cost.
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"Total: ${total_cost:.2f}")