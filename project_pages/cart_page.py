import streamlit as st 
import repositories.cart

@st.cache_data
def find_product_by_id(product_id,products):
    for product in products:
        if product["product_id"] == product_id:
            return product
    return None

def get_cart_products():
    return repositories.cart.get_cart_products(st.session_state.logged_in)
    

def update_cart_product(product_id,change):
    match change:
        case 1:
            repositories.cart.add_to_cart(st.session_state.logged_in,product_id)
        case -1:
            repositories.cart.take_from_cart(st.session_state.logged_in,product_id)
        case 0:
            repositories.cart.remove_from_cart(st.session_state.logged_in,product_id)


def show_cart_page():
    st.title("🛒 Корзина товаров")
    total_cost = 0

    # Получаем данные о товарах в корзине
    cart_products = get_cart_products()

    if not cart_products:
        st.write("Ваша корзина пуста.")
        return

    # Отображаем товары в корзине
    for item in cart_products:
        product_id = item["product_id"]
        amount = item["amount"]
        product = find_product_by_id(product_id,st.session_state.products)
        if not product:
            st.warning(f"Товар с ID {product_id} не найден в каталоге")
            continue

        product_name = product["product_name"]
        cost = product["cost"]
        # info?

        total_cost += cost * amount

        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            # Загружаем и отображаем изображение товара
            try:
                st.write("Image_cart")
            except Exception:
                st.write("Нет изображения")

        with col2:
            # Информация о товаре
            st.subheader(product_name)
            st.write(f"Цена: {cost} ₽")
            st.write(f"Количество: {amount}")


            # Кнопки для изменения количества
            if st.button("➖ Уменьшить", key=f"decrease-{product_id}"):
                if amount > 1:
                    update_cart_product( product_id, -1)
                else:
                    update_cart_product( product_id, 0) 
                st.rerun()

            if st.button("➕ Увеличить", key=f"increase-{product_id}"):
                update_cart_product( product_id, 1)
                st.rerun()

        with col3:
            # Кнопка удаления товара
            if st.button("❌ Удалить", key=f"delete-{product_id}"):
                update_cart_product( product_id, 0)
                st.rerun()

    # Общая стоимость корзины
    # total_cost = sum(cost * amount for _, _, cost, _, amount in cart_products)
    st.write(f"### Общая стоимость: {total_cost} ₽")
    sale_btn = st.button("Купить")
    # оформелние? 
    if sale_btn:
        st.success("Hurray!")