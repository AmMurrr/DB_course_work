# import psycopg2
# import psycopg2.extras
# from settings import DB_CONFIG
from repositories.db_connection import execute_query
from datetime import date


def remove_from_cart(user_id,product_id):
    query = """
        DELETE FROM cart
        WHERE user_id = %s AND product_id = %s
    """
    return execute_query(query,(user_id, product_id))

def take_from_cart(user_id, product_id):
    query = """
        UPDATE cart
        SET amount = cart.amount - 1
        WHERE user_id = %s AND product_id = %s
    """

    return execute_query(query,(user_id, product_id))

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


def get_cart_products(user_id):
    query = """
    SELECT product_id, amount FROM cart WHERE user_id = %(user_id)s
    """
    return execute_query(query,{"user_id": user_id},True)