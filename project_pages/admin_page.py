import streamlit as st 
import repositories.sales

import logging
import log_config

def get_all_sales_info():
    logging.info("Запрос на все покупки")
    return repositories.sales.get_all_sales()


def show_admin_page():
    st.title(f"Панель Администратора ID {st.session_state.logged_in}")
    option = st.selectbox("Сейчас выбрано", ["Все продажи", "Статистика"])
    if option == "Все продажи":
        logging.info(f"Выбрана опция {option} в Панели администратора")
        all_sale_info = get_all_sales_info()
        st.write(all_sale_info)