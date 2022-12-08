import psycopg2


def create_table():
    create_client_table = (
        """
        CREATE TABLE cliente (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL
        )
        """
    )

    try:
        conn = psycopg2.connect("dbname=endwhzad  user=endwhzad ")
        cur = conn.cursor()
        cur.execute(create_client_table)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
create_table()