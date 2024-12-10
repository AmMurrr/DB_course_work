from repositories.db_connection import execute_query
from datetime import date

def add_sale(user_id,sale_date):
    query = """
        INSERT INTO sales_history (user_id, sale_date) VALUES
        (%s,%s) RETURNING sale_id
    """
    return execute_query(query,(user_id,sale_date),True)[0]["sale_id"]

def add_sale_detail(sale_id, product_id, sale_amount):
    query = """
        INSERT INTO sale_details (sale_id, product_id, sale_amount) VALUES
        (%s, %s, %s)
    """
    return execute_query(query,(sale_id, product_id, sale_amount))


def sale_amount_update(user_id):
    query = """
        UPDATE goods
        SET amount = goods.amount - cart.amount
        FROM cart
        WHERE goods.product_id = cart.product_id AND cart.user_id = %s 
    """
    return execute_query(query,(user_id,))


def get_all_sales():
    query = """
        SELECT
            a.sale_id,
            a.user_id,
            a.sale_date,
            b.product_id,
            b.sale_amount
        FROM
            sales_history as a
        JOIN 
            sale_details as b
        ON
            a.sale_id = b.sale_id
    """
    return execute_query(query,is_fetch=True)