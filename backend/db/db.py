from backend.db import cursor, connection
from backend.parser.schema import Product
def add_product(product: Product):

    # подготавливаем множественный запрос
    sql = 'INSERT INTO public.test_ozon_products (product_name, product_price_original, ' \
          'product_price, product_price_with_ozon_card, product_images,' \
          'product_brand_name, product_brand_link, product_rating, ' \
          'product_categories, product_color, product_article, product_sizes,' \
          'product_all_articles, product_url, publication_category, ' \
          'verification, is_published, description, sub_category) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,FALSE,FALSE,%s,%s)' \
          'ON CONFLICT (product_article) DO NOTHING;'


    # указываем данные для запроса
    data = [
        (product.name,
         product.price_original,
         product.price,
         product.price_with_ozon_card,
         product.images,
         product.brand_name,
         product.brand_link,
         product.rating,
         product.categories,
         product.color,
         product.article,
         product.sizes,
         product.all_articles,
         product.url,
         product.publication_category,
         product.description,
         product.sub_category
         )
    ]

    cursor.executemany(sql, data)
    connection.commit()
    #
    # if format(cursor.rowcount) == 0:
    #     logger.warning(f'Товар не добавлен (скорее всего он уже есть в базе данных): {product.article}')
    # else:
    #     logger.info(f'Добавлен товар: {product.name}')

def get_verification_information():
    cursor.execute(
        "select product_id, publication_category, sub_category,  product_name, product_article, product_price, product_images "
        "from public.test_ozon_products where (verification = false) order by product_id limit 1")
    return cursor.fetchone()
