import sqlite3

conn= sqlite3.connect("shop.db")
conn.execute("PRAGMA foreign_keys=ON;")
def create_table():
    c=conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            phonenumber TEXT,
            address TEXT
        );
        """
    )
    conn.commit()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE                                                 
        );
        """
    )
def add_user(username,phonenumber,address):
    c=conn.cursor()
    c.execute("INSERT INTO users (username,phonenumber,address) VALUES (?,?,?)",(username,phonenumber,address))
    conn.commit()
def delete_user(pk):
    c=conn.cursor()
    c.execute("DELETE FROM users WHERE id=?",(pk,))
    conn.commit()
def update_user(id, username,phonenumber,address):
    c=conn.cursor()
    c.execute("UPDATE users SET username=?,phonenumber=?,address=? WHERE id=?",(username,phonenumber,address,id))
    conn.commit()
def add_product(name,price,user_id):
    c=conn.cursor()
    c.execute("INSERT INTO products (name,price,user_id) VALUES (?,?,?)",(name,price,user_id))
    conn.commit()
def user_info_from_product(product_id):
    c=conn.cursor()
    c.execute("""
        SELECT u.*
        FROM users u
        JOIN products p ON u.id =p.user_id
        WHERE p.id=?
        
    """,(product_id,))
    result=c.fetchall()
    return result

create_table()
add_user("nika","12312312","varketili")
add_user("zangi","1231231","varketili1")
add_user("adamiania","123123","varketili2")
add_user("good","12312","varketili3")
add_user("haircut","1231","varketili4")
add_product("pc", 2000, 9)
delete_user(1)
create_table()
delete_user(8)
conn.close() 