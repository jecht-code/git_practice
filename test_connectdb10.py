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

prov_query = """SELECT comp_ppt.profession, count(*) 
FROM comp_ppt 
inner join provider_practice_table as ppt_city
ON comp_ppt.provider_id = ppt_city.provider_id
WHERE profession = 'DO'
	AND city LIKE '%er%'
group by comp_ppt.profession"""

cursor.execute(prov_query)

a = cursor.fetchall()

print(a)


con.commit()
con.close()

