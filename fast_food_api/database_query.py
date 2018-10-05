import psycopg2
import os
if os.getenv("FLASK_ENV") == "Production":
    con = psycopg2.connect(os.getenv("DATABASE_URL"))
con = psycopg2.connect("dbname=fastfoodapp user=postgres host=localhost password=root")
cur = con.cursor()
class database_query:
    def check_table(self, table_name):
        cur.execute("select * from information_schema.tables where table_name=%s", (table_name,))
        return bool(cur.rowcount)
