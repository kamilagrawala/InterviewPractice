import pprint
from tokenize import String

global_inv = {}
cart = {}

def print_formatted(data):
    """Pretty prints the given data."""
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)

def main():
    """Main entry point."""
    print_formatted("Welcome to ECommereceCartManager!")
    restock("apple",100)
    restock("banana", 200)
    restock("apple", 400)
    print_formatted(global_inv)

    print_formatted(check("apple"))
    print_formatted(check("banana"))

    add("usr1", "apple", 100)
    add("usr2", "banana", 100)
    add("usr1", "banana", 100)
    add("usr1", "apple", 200)
    print_formatted(global_inv)
    print_formatted(cart)
    remove("usr1", "apple", 100)

    print_formatted(global_inv)
    print_formatted(cart)

    CART("usr1")

def restock(item_id, quantity):
        current_quantity = global_inv.get(item_id, 0)
        global_inv[item_id] = current_quantity + quantity

def check(item_id):
    return global_inv.get(item_id, 0)

def add(user_id, item_id, quantity):
    current_quantity = global_inv.get(item_id, 0)
    if current_quantity != 0 and quantity <= current_quantity:
        global_inv[item_id] -= quantity
        if user_id not in cart:
            cart[user_id] = {}
            cart[user_id][item_id] = quantity
        else:
            if item_id not in cart[user_id]:
                cart[user_id][item_id] = quantity
            else:
                cart[user_id][item_id] += quantity
        print_formatted("Added")
    else:
        print_formatted("Insufficient inventory")

def remove(user_id, item_id, quantity):
    cart_quantity = cart.get(user_id, {}).get(item_id, 0)
    if user_id in cart:
        if item_id in cart[user_id]:
            cart[user_id][item_id] -= min(quantity, cart_quantity)
            global_inv[item_id] +=  min(quantity, cart_quantity)
            print_formatted(f"Removed {min(quantity, cart_quantity)}")

def CART(user_id):
    user_cart = sorted(cart.get(user_id, {}))

    if not user_cart:
        print_formatted("Cart empty")
        return

    user_cart_str = ""

    for item in user_cart:
        if cart.get(user_id).get(item, 0) != 0:
            if user_cart_str == "":
                user_cart_str += f"{item}: {cart.get(user_id).get(item, 0)}"
            else:
                user_cart_str += f" ,{item}: {cart.get(user_id).get(item, 0)}"

    if user_cart_str == "":
        print_formatted("Cart Empty")
    else:
        print_formatted(user_cart_str)

if __name__ == "__main__":
    main()
