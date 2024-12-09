import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
from datetime import date


def add_user(login, mail, birth_date):
    query = """
    
    """

def add_hash(new_user_id, hash_password):
    query = """
    
    """


def get_mails():
    query = """
     SELECT mail FROM users
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def get_sign_in(mail):
    query = """
        SELECT user_id FROM users WHERE mail = %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, (mail))
            return cur.fetchone()
