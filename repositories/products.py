# import psycopg2
# import psycopg2.extras
# from settings import DB_CONFIG
from repositories.db_connection import execute_query


def add_product(product_id,type,product_name, company,cost,amount,info):
    query = """
        INSERT INTO "goods" (type,product_name,company,cost,amount,info) VALUES
        (%s,%s,%s,%s,%s,%s)
    """
    # with psycopg2.connect(**DB_CONFIG) as conn: 
    #     with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    #         cur.execute(query, (type , product_name, company,cost,amount,info))
    return execute_query(query,(type , product_name, company,cost,amount,info))
            

def get_products():
    query = """
        SELECT * FROM goods 
    """
    # with psycopg2.connect(**DB_CONFIG) as conn:
    #     with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    #         cur.execute(query)
    #         return cur.fetchall()
    return execute_query(query,is_fetch=True)