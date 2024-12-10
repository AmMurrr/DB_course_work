from repositories.db_connection import execute_query


def add_product(type,product_name, company,cost,amount,info):
    query = """
        INSERT INTO "goods" (type,product_name,company,cost,amount,info) VALUES
        (%s,%s,%s,%s,%s,%s) RETURNING product_id
    """
    return execute_query(query,(type , product_name, company,cost,amount,info),True)[0]["product_id"]
            

def get_products():
    query = """
        SELECT * FROM goods 
    """
    return execute_query(query,is_fetch=True)

def take_from_goods():
    query = """
         
    """
   

def add_to_goods():
    query = """
        
    """

def remove_from_goods(product_id):
    query = """
        DELETE FROM goods WHERE product_id = %s
    """
    return execute_query(query,(product_id,))