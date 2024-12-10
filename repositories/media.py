from repositories.db_connection import execute_query
import psycopg2

def get_all_images():
    query = """
        SELECT product_id, picture FROM media
    """
    return execute_query(query, is_fetch=True)

def get_image(product_id):
    query = """
        SELECT picture FROM media WHERE product_id = %s
    """
    return execute_query(query, (product_id,), is_fetch=True)


def add_media(product_id,img_bytes):
    query = """
        INSERT INTO media (product_id, picture) VALUES
        (%s, %s)
    """
    return execute_query(query, (product_id,img_bytes))
