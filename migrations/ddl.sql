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
    "serial" SERIAL PRIMARY KEY,
    "user_id" BIGINT NOT NULL,
    "product_id" BIGINT NOT NULL,
    "sale_date" DATE NOT NULL
);
-- ALTER TABLE
--     "sales_history" ADD PRIMARY KEY("serial");
CREATE TABLE "discounts"(
    "product_id" BIGINT NOT NULL,
    "discount_percent" BIGINT NOT NULL
);
CREATE TABLE "rewiews"(
    "serial" BIGINT NOT NULL,
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
    "media" ADD CONSTRAINT "media_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id");
ALTER TABLE
    "rewiews" ADD CONSTRAINT "rewiews_serial_foreign" FOREIGN KEY("serial") REFERENCES "sales_history"("serial");
ALTER TABLE
    "sales_history" ADD CONSTRAINT "sales_history_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id");
ALTER TABLE
    "cart" ADD CONSTRAINT "cart_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "sales_history" ADD CONSTRAINT "sales_history_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "cart" ADD CONSTRAINT "cart_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id");
ALTER TABLE
    "auth" ADD CONSTRAINT "auth_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "discounts" ADD CONSTRAINT "discounts_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "goods"("product_id");

    -- переделать так, чтоб был SERIAL и удаление каскадное и связи как в примере