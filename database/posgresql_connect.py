import psycopg2

conn = psycopg2.connect("host=localhost dbname=test user=postgres password=aaaa")

cur = conn.cursor()
cur.execute("select * from users")

print(cur.fetchone())

cur.close()
