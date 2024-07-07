import psycopg2

conn = psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="1234",port="5432")

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS person(
            id int primary key,
            name varchar(255),
            age int ,
            gender varchar(10));
            """)
cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
            (5,'Bharath',21,'m'),
            (6,'Akash',22,'m'),
            (7,'Chandru',23,'m'),
            (8,'Chethan',24,'m');
            """)

conn.commit()

cur.close()
conn.close()