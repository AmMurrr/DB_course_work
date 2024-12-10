from project_pages.selling_page import show_selling_page
from project_pages.cart_page import show_cart_page
from project_pages.admin_page import show_admin_page
import repositories.account
import streamlit as st
import bcrypt


Admin_ids =[1]
st.session_state.is_admin = True
st.session_state.logged_in = 1

def sign_in(mail, password):# 
    user_id = repositories.account.get_sign_in(mail) # ищем в БД айди по почте

    if not user_id : # если такого пользователя нет
        return -1

    hashed_password = repositories.account.get_hash(user_id) # получаем хэш из БД

    if not bcrypt.checkpw(password.encode('utf-8'),hashed_password.encode('utf-8')): # проверка пароля 
        return -1
    # print(user_id)

    if user_id in Admin_ids:
        st.session_state.is_admin = True

    return user_id
    

def password_hashing(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed_password

def sign_up(login, mail, password, birth_date):
    if mail in repositories.account.get_mails():
        return -1
    # проверка пароля?
    new_user_id = repositories.account.add_user(login,mail,birth_date)

    hashed_password = password_hashing(password)
    repositories.account.add_hash(new_user_id,hashed_password.decode('utf-8'))
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

    pages = ["Каталог товаров","Корзина"]
    if "is_admin" in st.session_state and st.session_state.is_admin == True:
        pages.append("Панель Администратора")

    page = st.sidebar.radio("Выбранная страница",pages)

    if page == "Каталог товаров":
        show_selling_page()
    if page == "Корзина":
        if "logged_in" in st.session_state:
            show_cart_page()
        else:
            st.write("Войдите в аккаунт")
    if page == "Панель Администратора":
            show_admin_page()
    
        
            


if __name__=="__main__":
    main()

# ad4fb8d1 - пароль для айди 1

# доделать добавление пользователей( пароли и хэши) COMPLETED
# сделать логи и/или отлов ошибок HALF_COMPLETED TOMORROW
# добавление в корзину COMPLETED
# добавить поддержку картинок товаров COMPLETED
# !!!! обработка покупок (количество товара должно уменьшаться после покупки, чек равный id покупки) TOMORROW
# ! сохранение информации после рестарта страницы ( через куки) TOMORROW
# отзывы сделать ----              THINK TOMORROW
# ? скидки если будет время -----  THINK TOMORROW
# убедиться что sql файлы создают всё правильно
# !!! разобраться нужно ли пересоздавать sales_history COMPLETED
# удаление товаров админом !!  каскадом? COMPLETED
# сделать корзину COMPLETED
# Нужно ли оформлять по особому markdown, colors? 
# Насчёт слов Вани о том, можно ли sql тут запускать ASK TOMORROW
# панель админа ( страница) со статистикой продаж HALF_COMPLETED TOMORROW
# порядок после изменения goods меняется TOMORROW
# приведи изображение и товары в порядок
