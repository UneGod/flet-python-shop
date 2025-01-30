import sqlite3 as sq

def register_product(*product):
    connection = sq.connect('database/products.db')

    cursor = connection.cursor()


    products_tb = '''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_nm TEXT NOT NULL,
            price REAL CHECK (price >= 0),
            stock_quantity INTEGER CHECK(stock_quantity >= 0),
            url TEXT NOT NULL
        )
    '''

    cursor.execute(products_tb)

    connection.commit()

    request_to_insert_data = '''
    INSERT INTO products (product_nm, price, stock_quantity, url) VALUES (?, ?, ?, ?);
    '''

    try:
        cursor.execute(request_to_insert_data, product)
        connection.commit()
    except Exception as e:
        return 0

    cursor.close()
    connection.close()