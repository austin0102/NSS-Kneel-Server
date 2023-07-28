import sqlite3

from models import Metal

METALS = [
    {
      "id": 1,
      "metal": "Sterling Silver",
      "price": 12.42
    },
    {
      "id": 2,
      "metal": "14K Gold",
      "price": 736.4
    },
    {
      "id": 3,
      "metal": "24K Gold",
      "price": 1258.9
    },
    {
      "id": 4,
      "metal": "Platinum",
      "price": 795.45
    },
    {
      "id": 5,
      "metal": "Palladium",
      "price": 1241
    }
  ]

def get_all_metals(): 
     with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM `Metals` m
        """)

        metals = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            metal = Metal(row['id'], row['metal'], row['price'])
            metals.append(metal.__dict__)

        return metals



def get_single_metal(id):
    """function to find single metal
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM `Metals` m  
        WHERE m.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        metal = Metal(data['id'], data['metal'], data['price'])

        return metal.__dict__

def create_metal(new_metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Metals
            ( metal, price )
        VALUES
            ( ?, ? );
        """, (new_metal['metal'], new_metal['price'],
              ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the metal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_metal['id'] = id


    return new_metal



def update_metal(id, new_metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals
        SET
            metal = ?,
            price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
