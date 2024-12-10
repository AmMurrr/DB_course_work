# import psycopg2
# import psycopg2.extras
# from settings import DB_CONFIG
from datetime import date
from repositories.db_connection import execute_query


def add_user(login, mail, birth_date):
    query = """
        INSERT INTO "users" (login, mail, birth_date) VALUES
        (%s,%s,%s) RETURNING user_id;
    """
    return execute_query(query,(login,mail,birth_date),True)[0]["user_id"]

def add_hash(new_user_id, password_hash):
    query = """
        INSERT INTO auth (user_id,password_hash) VALUES
        (%s,%s)
    """
    return execute_query(query,(new_user_id,password_hash))


def get_hash(user_id):
    query = """
         SELECT password_hash FROM auth WHERE user_id = %(user_id)s
    """
    result  = execute_query(query,{"user_id":user_id},True)
    if not result:
        # log
        return None
    return result[0]["password_hash"]
    


def get_mails():
    query = """
     SELECT mail FROM users
    """
    # with psycopg2.connect(**DB_CONFIG) as conn:
    #     with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    #         cur.execute(query)
    #         return cur.fetchall()
    return execute_query(query,is_fetch=True)

def get_sign_in(mail):
    query = """
        SELECT user_id FROM users WHERE mail = %(mail)s
    """
    # with psycopg2.connect(**DB_CONFIG) as conn:
    #     with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    #         cur.execute(query, (mail))
    #         return cur.fetchone()
    result = execute_query(query,{"mail": mail},is_fetch=True)

    if not result:
        # log
        return None
    return result[0]["user_id"]
