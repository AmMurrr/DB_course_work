import streamlit as st 
import repositories.sales
from repositories.products import get_product_name
from repositories.account import get_user_info,user_purge


import logging
import log_config

def get_all_sales_info():
    logging.info("Запрос на все покупки")
    return repositories.sales.get_all_sales()

def get_login(user_id):
    logging.info(f"Получаем логин пользователя {user_id}")
    user_info = get_user_info(user_id)
    return user_info["login"]

def get_name(product_id):
    logging.info(f"Получаем название товара {product_id}")
    return get_product_name(product_id)

def user_purge():
    logging.info("Удаление всех пользователей")

def sale_clear():
    repositories.sales.clear_sales()

def show_admin_page():
    st.title(f"Панель Администратора ID {st.session_state.logged_in}")
    # option = st.selectbox("Сейчас выбрано", ["Все продажи", "Статистика"])

    # if option == "Все продажи":
    # logging.info(f"Выбрана опция {option} в Панели администратора")
    all_sales_info = get_all_sales_info()
    all_sales_worth = 0

    if not all_sales_info:
        logging.info("Информация о продажах не найдена")
        st.warning("Информация о продажах не найдена")

    if st.button("Очистить историю продаж"):
        logging.info("Очистка истории продаж")
        sale_clear()
        st.rerun()

    if st.button("# 💀 Удалить всех пользователей"):
        user_purge()

    for sale in all_sales_info:
        with st.container(border=True):
            cols = st.columns([1,1,1])

            sale_id = sale["sale_id"]
            sale_user_id = sale["user_id"]
            sale_date = sale["sale_date"]
            sale_cost = sale["total_cost"]
            sale_products = sale["sale_details"]

            all_sales_worth += sale_cost

            with cols[0]:
                st.subheader(f"Покупка №{sale_id}")
                user_login = get_login(sale_user_id)
                st.write(f"Совершена пользователем {user_login}")
                st.write(f"{sale_date}")
            
            with cols[1]:
                st.subheader("Купленные товары:")
                for product in sale_products:
                    product_name = get_name(product["product_id"])
                    amount = product["amount"]
                    st.write(f"### {product_name} в количестве  {amount}")

            with cols[2]:
                st.subheader("Сумма продажи:")
                st.write(f"### {sale_cost} ₽")

    st.write(f"#### Сумма продаж: {all_sales_worth} ₽")