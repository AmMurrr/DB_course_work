import psycopg2
import psycopg2.extras
from settings import DB_CONFIG



def execute_query(query,parameters=None,is_fetch = False,is_fetchall = False):
    try:
        with psycopg2.connect(**DB_CONFIG) as conn: 
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(query, parameters)

                if is_fetch:
                    result =  cur.fetchall()
                else:
                    result =  None
                conn.commit()
                return result

    except psycopg2.Error as e:
        conn.rollback()
        print(f"Ошибка {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
