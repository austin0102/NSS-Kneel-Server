import sqlite3

from models import Order, Metal, Style, Size

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
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.styles_id,
            o.sizes_id,
            o.metals_id,
            m.metal as metal,
            m.price as metal_price,
            s.style as style,
            s.price as style_price,
            sz.carets as carets,
            sz.price as size_price
        FROM `Orders` o
        JOIN Metals m ON m.id = o.metals_id
        JOIN Styles s ON s.id = o.styles_id
        JOIN Sizes sz ON sz.id = o.sizes_id
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['styles_id'], row['sizes_id'], row['metals_id'])
            metal = Metal(row['id'], row['metal'], row['metal_price'])
            style = Style(row['id'], row['style'], row['style_price'])
            size = Size(row['id'], row['carets'], row['size_price']) 
            order.metal = metal.__dict__
            order.style = style.__dict__
            order.size = size.__dict__
            orders.append(order.__dict__)

        return orders

def get_single_order(id):
    """function to find single order
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.styles_id,
            o.sizes_id,
            o.metals_id,
            m.metal as metal,
            m.price as metal_price,
            s.style as style,
            s.price as style_price,
            sz.carets as carets,
            sz.price as size_price
        FROM `Orders` o
        JOIN Metals m ON m.id = o.metals_id
        JOIN Styles s ON s.id = o.styles_id
        JOIN Sizes sz ON sz.id = o.sizes_id
        WHERE o.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        order = Order(data['id'], data['styles_id'], data['sizes_id'], data['metals_id'])
        metal = Metal(data['id'], data['metal'], data['metal_price'])
        style = Style(data['id'], data['style'], data['style_price'])
        size = Size(data['id'], data['carets'], data['size_price']) 
        order.metal = metal.__dict__
        order.style = style.__dict__
        order.size = size.__dict__

        return order.__dict__





def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( styles_id, sizes_id, metals_id )
        VALUES
            ( ?, ?, ? );
        """, (new_order['styles_id'], new_order['sizes_id'],
              new_order['metals_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id


    return new_order


def delete_order(id):
    """delete an order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
            SET
                styles_id = ?,
                sizes_id = ?,
                metals_id = ?,
        WHERE id = ?
        """, (new_order['styles_id'], new_order['sizes_id'],
              new_order['metals_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True