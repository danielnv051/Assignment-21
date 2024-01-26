import sqlite3
con = sqlite3.connect('chinook.db')
my_cursor = con.cursor()

result = my_cursor.execute("SELECT * FROM customers WHERE Country = 'France'")
french_customers = result.fetchall()

for customer in french_customers:
    print(customer[1], customer[2])

