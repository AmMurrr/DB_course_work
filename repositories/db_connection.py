import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

import logging
import log_config

def execute_query(query,parameters=None,is_fetch = False,is_fetchall = False):
    try:
        with psycopg2.connect(**DB_CONFIG) as conn: 
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(query, parameters)

                logging.info("Выполнен запрос")
                if is_fetch:
                    result =  cur.fetchall()
                    logging.info(f"получен ответ от БД: {result}")
                else:
                    logging.info("Ответа от БД не требуется")
                    result =  None
                conn.commit()
                return result

    except psycopg2.Error as e:
        conn.rollback()
        logging.info(f"Ошибка при выполнении запроса: {e}")
    finally:
        if cur:
            cur.close()
            logging.info("Курсор отключён")
        if conn:
            conn.close()
            logging.info("Соединение прекращено")
