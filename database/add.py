import sqlite3 as sq

connection = sq.connect('main.db')

cursor = connection.cursor()


products_tb = '''
CREATE TABLE IF NOT EXISTS products (
     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
     product_nm TEXT NOT NULL,
     price REAL CHECK (price >= 0),
     stock_quantity INTEGER CHECK(stock_quantity >= 0)
)
'''

cursor.execute(products_tb)

connection.commit()

new_product = ('asd', 99.31, 56)

request_to_insert_data = '''
INSERT INTO products (product_nm, price, stock_quantity) VALUES (?, ?, ?);
'''

cursor.execute(request_to_insert_data, new_product)

connection.commit()

cursor.close()
connection.close()