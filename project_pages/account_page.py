import streamlit as st
import repositories.account
from services.cookies import set_cookie


import logging
import log_config



def log_out():
    logging.info(f"{st.session_state.logged_in} вышел из аккаунта")
    set_cookie("auth_token","0")
    st.session_state.logged_in = -1
    st.session_state.is_admin = False
    st.rerun()




def show_account_page():
    user_info = repositories.account.get_user_info(st.session_state.logged_in)

    login = user_info["login"]
    st.title(f"Аккаунт пользователя {login}")


    if st.button("Выйти из аккаунта"):
        log_out()