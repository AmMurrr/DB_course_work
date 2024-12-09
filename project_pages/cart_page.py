import streamlit as st 
import repositories.cart


def get_products_cart():
    return repositories.cart.get_products_cart(st.session_state.logged_in)
    




def show_cart_page():
    cart_products = get_products_cart()
    st.title("Корзина" )
    st.write(cart_products)