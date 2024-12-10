from datetime import date
import repositories.sales


class SaleService:
    def process_sale(user_id, sale_products, sale_date):
        sale_id = repositories.sales.add_sale(user_id,sale_date)
        # log
        if not sale_id:
            return -1
        for item in sale_products:
            repositories.sales.add_sale_detail(sale_id,item["product_id"], item["amount"])
            
            # log
        repositories.sales.sale_amount_update(user_id)
        return sale_id
        
