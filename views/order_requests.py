ORDERS = [
        {
        "id": 1,
        "stylesId": 1,
        "sizesId": 1,
        "metalsId": 1
        },
        {
        "stylesId": 1,
        "sizesId": 1,
        "metalsId": 1,
        "id": 2
        },
        {
        "stylesId": 1,
        "sizesId": 1,
        "metalsId": 1,
        "id": 3
        },
        {
        "stylesId": 3,
        "sizesId": 1,
        "metalsId": 5,
        "id": 4
        },
        {
        "stylesId": 1,
        "sizesId": 4,
        "metalsId": 1,
        "id": 5
        },
        {
        "stylesId": 1,
        "sizesId": 3,
        "metalsId": 2,
        "id": 6
        },
        {
        "stylesId": 1,
        "sizesId": 2,
        "metalsId": 3,
        "id": 7
        },
        {
        "stylesId": 1,
        "sizesId": 2,
        "metalsId": 1,
        "id": 8
        }
    ]


def get_all_orders(): 
    return ORDERS

def get_single_order(id):
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order


def create_order(order):
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def delete_order(id):
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break