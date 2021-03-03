DB_HOST = 'localhost'
DB_NAME = 'sql_code_test_2019'
DB_USER = 'postgres'
DB_PASS = 'yuppers1234'

import psycopg2

con = psycopg2.connect(
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASS,
            host = DB_HOST)

cursor = con.cursor()

prov_query = "SELECT provider_id, provider_name FROM provider_table"
cursor.execute(prov_query)

a = cursor.fetchall()

print(a)

for rows in a:
    ##if rows[0] = 'itemremove[1]':
        ##return
    print(rows[1])

con.commit()
con.close()

