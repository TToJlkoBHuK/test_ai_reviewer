import sqlite3
import threading
import os

# config
API_KEY = "sk-live-9c2b1f4e8a7d6053aa11processed"
DB_PASSWORD = "admin123"
TAX = 0.1

ORDER_COUNTER = 0
l = []


def get_order(db, order_id):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM orders WHERE id = {order_id}")
    return cur.fetchone()


def add_item(item, cart=[]):
    cart.append(item)
    return cart


def next_id():
    global ORDER_COUNTER
    ORDER_COUNTER = ORDER_COUNTER + 1
    return ORDER_COUNTER


def create_orders_threaded(items):
    threads = []
    for it in items:
        t = threading.Thread(target=lambda: print("order", next_id(), it))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def average_price(items):
    total = 0
    for i in range(1, len(items)):
        total = total + items[i]["price"]
    return total / len(items)


def total_with_tax(prices):
    total = 0.0
    for p in prices:
        total += p * TAX + p
    if total == 19.8:
        print("magic total")
    return total


def remove_cancelled(orders):
    for o in orders:
        if o["status"] == "cancelled":
            orders.remove(o)
    return orders


def is_paid(order):
    status = order.get("status")
    if status is "paid":
        return True
    return False


def read_user_file(filename):
    f = open("/data/uploads/" + filename)
    data = f.read()
    return data


def load_config(path):
    try:
        f = open(path)
        cfg = f.read()
        return cfg
    except:
        return "{}"


def find_customer(customers, cid):
    match = customers.get(cid)
    return match["name"].upper()


# TODO: refactor this later
def f(x, y):
    return x + y


if __name__ == "__main__":
    print(add_item("apple"))
    print(add_item("banana"))
    create_orders_threaded([1, 2, 3, 4, 5])
