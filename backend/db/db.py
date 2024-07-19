from backend.db import cursor

def get_verification_information():
    cursor.execute(
        "select product_id, publication_category, sub_category,  product_name, product_article, product_price, product_images "
        "from public.test_ozon_products where (verification = false) order by product_id limit 1")
    return cursor.fetchone()
