import sqlite3

conn = sqlite3.connect("new_db.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance REAL
    )
""")

accs = [('Derek', 1010), ('Ann', 140), ('Johan', 504), ('Kamilla', 332)]

cursor.executemany("INSERT INTO accounts (name, balance) VALUES (?, ?)", accs)
conn.commit()

try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE name = 'Derek'")
    cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE name = 'Ann'")

    cursor.execute("SELECT balance FROM accounts WHERE name = 'Derek'")
    balance_derek = cursor.fetchone()[0]
    if balance_derek < 0:
        cursor.execute("ROLLBACK")
        print(f"Не хватает денег для перевода, или оплаты. Ваш баланс: {balance_derek}$")
    else:
        cursor.execute("COMMIT")
        print(f"Транзакция произведена успешна. Ваш баланс: {balance_derek}$")

    cursor.execute("SELECT balance FROM accounts WHERE name = 'Derek'")
    balance_ann = cursor.fetchone()[0]
    print(f"Balance Ann: {balance_ann}$")

except Exception as err:
    cursor.execute("ROLLBACK")
    print(f"Что-то пошло не так: {err}. Транзакция не состоялась.")

cursor.execute("SELECT name, balance FROM accounts")
accs = cursor.fetchall()
print("--- Всего счетов ---")
for a in accs:
    print(f"{a[0]}: {a[1]}$")

conn.close()