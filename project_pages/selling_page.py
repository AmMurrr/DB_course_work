import pandas as pd 
import streamlit as st 
from datetime import date
import repositories.products
from repositories.cart import add_to_cart

if "cart_counter" not in st.session_state:
    st.session_state.cart_counter = 0


@st.dialog("Добавление товара")
def adding_product():
    type = st.text_input("Тип товара")
    product_name = st.text_input("Название товара")
    company = st.text_input("Компания-производитель товара")
    cost = st.text_input("Цена товара")
    amount = st.text_input("Доступное количество товара")
    info = st.text_input("Описание товара")
    if st.button("Добавить товар"):
        repositories.products.add_product(type,product_name,company,cost,amount,info)
        st.rerun()


def get_products():
    return repositories.products.get_products()


def get_amount(product_id): # получаем количество товара на данный момент
    return next((row['amount'] for row in st.session_state.products if row["product_id"] == product_id),None)

def product_to_cart(product_id):
    product_amount = get_amount(product_id)
    if product_amount == 0:
        st.write("Товар закончился")
        return False
    add_to_cart(st.session_state.logged_in,product_id)
    st.session_state.cart_counter += 1
    st.write(f"В корзину добавлено {st.session_state.cart_counter} товара")

if "products" not in st.session_state:
    st.session_state.products = get_products()
 

def show_selling_page():
    st.session_state.products = get_products()
    # print(st.session_state.products)
    st.title("Каталог Товаров")
    
    if "is_admin" in st.session_state and st.session_state.is_admin == True:
        if st.button("+Добавить товар"):
            adding_product()
    for product in st.session_state.products:
        with st.container(border=True):
            cols = st.columns([1,2])
            with cols[0]:
                st.write("Image")
            with cols[1]:
                st.subheader(product["product_name"])
                st.write(product["company"])
                st.write(product["info"])
                if st.button("В корзину",key=product["product_id"]):
                    if "logged_in" in st.session_state:
                        product_to_cart(product["product_id"])
                    else:
                        st.write("Войдите в аккаунт или зарегистрируйтесь для покупки")
