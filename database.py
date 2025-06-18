import  sqlite3

def create_goods_table():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS goods_receiving(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              product_name TEXT,
              supplier_name TEXT,
              quantity INTEGER,
              unit TEXT,
              rate_per_unit REAL,
              tax REAL,
              total REAL
              )'''  )
    
    conn.commit()
    conn.close()
def create_sales_table():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS sales(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              customer_name TEXT,
              product_name TEXT,
              quantity INTEGER,
              unit TEXT,
              rate_per_unit REAL,
              tax REAL,
              total REAL
              )'''  )
    
    conn.commit()
    conn.close()

def create_product_table():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS product_master(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              product_name TEXT,
              barcode TEXT,
              sku_id TEXT,
              category TEXT,
              subcategory TEXT,
              description TEXT,
              image_path TEXT,
              tax REAL,
              unit TEXT,
              price REAL
              )'''  )
    
    conn.commit()
    conn.close()


if __name__=="__main__":
    create_goods_table()
    create_sales_table()
    create_product_table()