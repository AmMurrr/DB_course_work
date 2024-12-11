CREATE TABLE "goods"(
    "product_id" SERIAL PRIMARY KEY,
    "type" TEXT NOT NULL,
    "product_name" TEXT NOT NULL,
    "company" TEXT NOT NULL,
    "cost" BIGINT NOT NULL,
    "amount" BIGINT NOT NULL,
    "info" TEXT NOT NULL
);
-- ALTER TABLE
--     "goods" ADD PRIMARY KEY("product_id");
CREATE TABLE "auth"(
    "user_id" BIGINT NOT NULL,
    "password_hash" TEXT NOT NULL
);
CREATE TABLE "sales_history"(
    "sale_id" SERIAL PRIMARY KEY,
    "user_id" BIGINT,
    -- "product_id" BIGINT NOT NULL,
    "sale_date" DATE NOT NULL,
    "total_cost" BIGINT NOT NULL
);
-- ALTER TABLE
--     "sales_history" ADD PRIMARY KEY("serial");
CREATE TABLE "discounts"(
    "product_id" BIGINT NOT NULL,
    "discount_percent" BIGINT NOT NULL
);
CREATE TABLE "rewiews"(
    "sale_id" BIGINT NOT NULL,
    "review_text" TEXT NOT NULL,
    "rate" BIGINT NOT NULL,
    "review_date" DATE NOT NULL
);
CREATE TABLE "media"(
    "product_id" BIGINT NOT NULL,
    "picture" bytea NOT NULL
);
CREATE TABLE "cart"(
    "user_id" BIGINT NOT NULL,
    "product_id" BIGINT NOT NULL,
    "amount" BIGINT NOT NULL
);
CREATE UNIQUE INDEX cart_user_product_idx ON cart (user_id, product_id);
CREATE TABLE "users"(
    "user_id" SERIAL PRIMARY KEY,
    "login" TEXT NOT NULL,
    "mail" TEXT NOT NULL,
    "birth_date" DATE NOT NULL
);
-- ALTER TABLE
--     "users" ADD PRIMARY KEY("user_id");
ALTER TABLE
    "media" ADD CONSTRAINT "media_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id") ON DELETE CASCADE;
ALTER TABLE
    "rewiews" ADD CONSTRAINT "rewiews_serial_foreign" FOREIGN KEY("sale_id") REFERENCES "sales_history"("sale_id") ON DELETE SET NULL;
-- ALTER TABLE
--     "sales_history" ADD CONSTRAINT "sales_history_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id");
ALTER TABLE
    "cart" ADD CONSTRAINT "cart_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id") ON DELETE CASCADE;
ALTER TABLE
    "sales_history" ADD CONSTRAINT "sales_history_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id")ON DELETE SET NULL;
ALTER TABLE
    "cart" ADD CONSTRAINT "cart_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id") ON DELETE CASCADE;
ALTER TABLE
    "auth" ADD CONSTRAINT "auth_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id") ON DELETE CASCADE;
ALTER TABLE
    "discounts" ADD CONSTRAINT "discounts_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id") ON DELETE CASCADE;


CREATE TABLE sale_details (
    sale_id BIGINT NOT NULL,                -- ID продажи, связан с sale_history
    product_id BIGINT,             -- ID товара, связан с goods
    sale_amount BIGINT NOT NULL,            -- Количество проданных единиц
    
    -- Внешний ключ для связи с sale_history.sale_id
    CONSTRAINT sale_details_sale_id_fk 
    FOREIGN KEY (sale_id) 
    REFERENCES sales_history(sale_id)
    ON DELETE CASCADE,                      -- Удаление записи при удалении связанной записи из sale_history
    
    -- Внешний ключ для связи с goods.product_id
    CONSTRAINT sale_details_product_id_fk 
    FOREIGN KEY (product_id) 
    REFERENCES goods(product_id)
    ON DELETE SET NULL
);

CREATE TABLE goods_log (
    log_id SERIAL PRIMARY KEY,
    product_id BIGINT,
    ACTION TEXT,
    log_time TIMESTAMP default CURRENT_TIMESTAMP
);


-- Функция
CREATE OR REPLACE FUNCTION log_goods_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'DELETE' THEN
        INSERT INTO goods_log (product_id,action)
        VALUES (OLD.product_id, 'DELETE');
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO goods_log (product_id,action)
        VALUES (NEW.product_id, 'INSERT');
    ELSE
        INSERT INTO goods_log (product_id,action)
        VALUES (NEW.product_id, 'UPDATE');
    END IF;
    RETURN NULL;

END;
$$ LANGUAGE plpgsql;

-- Триггер
CREATE TRIGGER goods_changes_trigger
AFTER INSERT OR UPDATE OR DELETE ON goods
FOR EACH ROW EXECUTE FUNCTION log_goods_changes();


-- Процедура
CREATE OR REPLACE PROCEDURE clear_goods_log()
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM goods_log;
END;
$$