# import psycopg2
# import psycopg2.extras
# from settings import DB_CONFIG
from repositories.db_connection import execute_query


def add_product(type,product_name, company,cost,amount,info):
    query = """
        INSERT INTO "goods" (type,product_name,company,cost,amount,info) VALUES
        (%s,%s,%s,%s,%s,%s)
    """
    return execute_query(query,(type , product_name, company,cost,amount,info))
            

def get_products():
    query = """
        SELECT * FROM goods 
    """
    return execute_query(query,is_fetch=True)