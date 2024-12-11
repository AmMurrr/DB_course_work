from repositories.db_connection import execute_query
from datetime import date



def add_sale(user_id,sale_date,total_cost):
    query = """
        INSERT INTO sales_history (user_id, sale_date,total_cost) VALUES
        (%s,%s,%s) RETURNING sale_id
    """
    return execute_query(query,(user_id,sale_date,total_cost),True)[0]["sale_id"]

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
    query =""" 
    SELECT 
        sh.sale_id,
        sh.user_id,
        sh.sale_date,
        sh.total_cost,
    ARRAY_AGG(
        JSON_BUILD_OBJECT(
            'product_id', sd.product_id,
            'amount', sd.sale_amount
        )
    ) AS sale_details
    FROM 
        sales_history sh
    LEFT JOIN 
        sale_details sd
    ON 
        sh.sale_id = sd.sale_id
    GROUP BY 
        sh.sale_id, sh.user_id, sh.sale_date, sh.total_cost;

    """
    return execute_query(query,is_fetch=True)



def clear_sales():
    query = """
       DELETE FROM sales_history
    """
    return execute_query(query)