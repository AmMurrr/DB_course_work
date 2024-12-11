from datetime import date
import repositories.sales

import logging
import log_config

class SaleService:
    def process_sale(user_id, sale_products, sale_date,total_cost):
        sale_id = repositories.sales.add_sale(user_id,sale_date,total_cost)
        
        if not sale_id:
            logging.info("Добавить покупку не получилось")
            return -1

        logging.info(f"Покупка с ID {sale_id} добавлена")
        for item in sale_products:
            repositories.sales.add_sale_detail(sale_id,item["product_id"], item["amount"])    
            logging.info(f"Детали покупки {sale_id} добавлены")

        logging.info("Обновляем количество на складе")
        repositories.sales.sale_amount_update(user_id)
        return sale_id
        
