import sqlite3 as sq

def get_product():
    products_to_scr = []
    connection = sq.connect('database/products.db')

    cursor = connection.cursor()

    request_to_read_data = "SELECT * FROM products"

    cursor.execute(request_to_read_data)

    data = cursor.fetchall()
    
    for i in data:
        products_to_scr.append({'name': i[1], 'price': i[2], 'stock': i[3], 'image': i[4]})
    return products_to_scr