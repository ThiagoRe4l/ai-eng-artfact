import csv
import sqlite3
from functools import lru_cache
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

SCHEMA = """
CREATE TABLE categories (category_id INTEGER PRIMARY KEY, name TEXT, description TEXT);
CREATE TABLE products (product_id INTEGER PRIMARY KEY, price_brl REAL, name TEXT, category_id INTEGER,
    description TEXT, stock_quantity INTEGER, status TEXT, specs TEXT, created_at TEXT);
CREATE TABLE promotions (promotion_id INTEGER PRIMARY KEY, product_id INTEGER, discount_percent REAL,
    description TEXT, is_active INTEGER);
CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, city TEXT);
CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT, status TEXT,
    total_brl REAL, payment_method TEXT, tracking_code TEXT, estimated_delivery TEXT, notes TEXT);
CREATE TABLE order_items (order_id INTEGER, quantity INTEGER, product_id INTEGER);
"""

TABLES = ("categories", "products", "promotions", "customers", "orders", "order_items")


def _load_csv(conn: sqlite3.Connection, table: str) -> None:
    with open(DATA_DIR / f"{table}.csv", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        rows = [[row[col] or None for col in columns] for row in reader]  # "" -> NULL
    placeholders = ", ".join("?" for _ in columns)
    conn.executemany(
        f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})", rows
    )


@lru_cache(maxsize=1)
def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    for table in TABLES:
        _load_csv(conn, table)
    conn.commit()
    return conn


def query(sql: str, params: tuple = ()) -> list[dict]:
    return [dict(row) for row in get_connection().execute(sql, params)]