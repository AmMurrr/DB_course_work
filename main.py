from project_pages.selling_page import show_selling_page
from project_pages.cart_page import show_cart_page
import repositories.account
import streamlit as st


Admin_ids =[1]
st.session_state.is_admin = True
st.session_state.logged_in = 1

def sign_in(mail, password):
    # if mail in repositories.account.get_mails():
    user_id = repositories.account.get_sign_in(mail)
    # else:
    if user_id is None:
        return -1
    # проверка пароля 
    print(user_id)

    if user_id['user_id'] in Admin_ids:
        st.session_state.is_admin = True

    return user_id["user_id"]
    

def password_hashing(password):
    return password

def sign_up(login, mail, password, birth_date):
    if mail not in repositories.account.get_mails():
        return -1
    
    new_user_id = repositories.account.add_user(login,mail,birth_date)

    hashed_password = password_hashing(password)
    repositories.account.add_hash(new_user_id,hashed_password)
    return new_user_id

@st.dialog("Регистрация")
def signing_up():

    st.write("Введите логин")
    login = st.text_input("  ")
    st.write("Введите почту")
    mail = st.text_input(" ")
    st.write("Введите пароль")
    password = st.text_input("Пароль должен содержать не менее 24 символов, хотя бы одну заглавную букву, цифру, специальный символ,эмодзи, иероглиф и узелковое письмо инков")
    st.write("Введите свою дату рождения")
    birth_date = st.date_input(" ")

    if st.button("Подтвердить "):
        if login != "" and password != "" and mail != "":
            # to do check mail
            valid_user_check = sign_up(login,mail,password,birth_date)
            if valid_user_check != -1:
                st.session_state.logged_in = valid_user_check
                st.rerun()
            else:
                st.write("Неправильные данные для аккаунта")
            
            
        else:
            st.write("Некоторые данные не заполнены")


@st.dialog("Вход")
def signing_in():

    st.write("Введите почту")
    mail = st.text_input(" ",key = -1)
    st.write("Введите пароль")
    password = st.text_input(" ",key = -2)

    if st.button(" Подтвердить",):
        valid_user_check = sign_in(mail,password)
        if valid_user_check != -1:
            st.session_state.logged_in = valid_user_check
            st.rerun()
        else:
            st.write("Такого пользователя не существует")
        

def main():
    # st.title("Продажа туристического снаряжения")
    st.sidebar.title("Магазин туристического снаряжения Rock&Stone")
    if "logged_in" not in st.session_state:
        if st.sidebar.button("Зарегистрироваться"):
            signing_up()
        if st.sidebar.button("Войти"):
            signing_in()
    page = st.sidebar.radio("Выбранная страница",["Каталог товаров","Корзина"])
    if page == "Каталог товаров":
        show_selling_page()
    if page == "Корзина":
        if "logged_in" in st.session_state:
            show_cart_page()
        else:
            st.write("Войдите в аккаунт")


if __name__=="__main__":
    main()



# доделать добавление пользователей( пароли и хэши) TOMORROW
# сделать логи и/или отлов ошибок
# добавление в корзину TOMORROW
# добавить поддержку картинок товаров
# !!!! обработка покупок (количество товара должно уменьшаться после покупки)
# ! сохранение информации после рестарта страницы ( через куки) TOMORROW
# отзывы сделать
# ? скидки если будет время
# убедиться что sql файлы создают всё правильно
# !!! разобраться нужно ли пересоздавать sales_history
# удаление товаров админом !!
# 
