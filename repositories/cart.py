# import psycopg2
# import psycopg2.extras
# from settings import DB_CONFIG
from repositories.db_connection import execute_query
from datetime import date

def add_to_cart(user_id, product_id):
    query = """
        INSERT INTO cart (user_id, product_id, amount)
        VALUES (%s, %s, 1)
        ON CONFLICT (user_id, product_id)
        DO UPDATE SET amount = cart.amount + 1;
    """

    return execute_query(query,(user_id,product_id),False)
    # with psycopg2.connect(**DB_CONFIG) as conn: 
    #     with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    #         cur.execute(query, (user_id,product_id))
             # заготовка для отлова ошибок тут логи должны быть


def get_products_cart(user_id):
    query = """
    SELECT product_id, amount FROM cart WHERE user_id = 1
    """
    return execute_query(query,(user_id),True)