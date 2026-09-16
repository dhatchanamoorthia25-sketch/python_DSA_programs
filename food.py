class FoodItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food_item(self, food_item):
        self.menu.append(food_item)

    def show_menu(self):
        print(f"\n==== {self.name} Menu ====")
        for food in self.menu:
            print(f"{food.item_id}. {food.name} - ₹{food.price}")


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, food, quantity):
        self.items.append((food, quantity))
        print(f"{food.name} added to cart.")

    def calculate_total(self):
        total = 0
        for food, quantity in self.items:
            total += food.price * quantity
        return total


class Order:
    def __init__(self, cart):
        self.cart = cart
        self.status = "Placed"


# Create food items
food1 = FoodItem(1, "Pizza", 200)
food2 = FoodItem(2, "Burger", 120)
food3 = FoodItem(3, "French Fries", 80)

# Create restaurant
restaurant = Restaurant("My Restaurant")

# Add food items to menu
restaurant.add_food_item(food1)
restaurant.add_food_item(food2)
restaurant.add_food_item(food3)

# Display menu
restaurant.show_menu()

# Create cart
cart = Cart()

# Add items to cart
cart.add_item(food1, 2)
cart.add_item(food2, 1)

# Calculate total
print("\nTotal Bill: ₹", cart.calculate_total())

# Create order
order = Order(cart)
print("Order Status:", order.status)