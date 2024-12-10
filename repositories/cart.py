
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


def check_cart_amount(user_id,product_id):
    query = """
    SELECT amount FROM cart WHERE user_id = %s AND product_id = %s
    """
    return execute_query(query,(user_id,product_id),True)

def get_cart_products(user_id):
    query = """
    SELECT product_id, amount FROM cart WHERE user_id = %(user_id)s
    """
    return execute_query(query,{"user_id": user_id},True)

def clear_cart(user_id):
    query = """
    DELETE FROM cart WHERE user_id = %s
    """
    return execute_query(query,(user_id,))