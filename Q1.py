# Q1: task 1


def total_sales(store_data):
    product_sales = {}  # This will store the total sales for each product
    for store, products in store_data.items():
        for product, quantity in products.items():
            if product in product_sales:
                product_sales[
                    product
                ] += quantity  # Add the quantity to the existing value
            else:
                product_sales[product] = (
                    quantity  # Initialize the product with its quantity
                )
    return product_sales


print("======================== Q1 task 1 starts here ===========================")
# Test Data
store_data = {
    "Store A": {"apple": 50, "banana": 30, "orange": 20},
    "Store B": {"apple": 70, "banana": 10, "grape": 40},
    "Store C": {"apple": 60, "orange": 50, "banana": 20},
}

# Test the function
result = total_sales(store_data)
print(result)

print("======================== Q1 task 2 starts here ===========================")


# Q1 : task 2
def store_with_max_sales(store_data):
    max_sales = 0
    store_with_max = ""

    for store, products in store_data.items():
        store_total = sum(products.values())

        if store_total > max_sales:
            max_sales = store_total
            store_with_max = store

    if store_with_max == "":
        return None

    return store_with_max


# Test Data
store_data = {
    "Store A": {"apple": 50, "banana": 30, "orange": 20},
    "Store B": {"apple": 70, "banana": 10, "grape": 40},
    "Store C": {"apple": 60, "orange": 50, "banana": 20},
}

# Test the function
result = store_with_max_sales(store_data)
print(result)
