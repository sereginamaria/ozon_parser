import psycopg2 as pg
from web_server import logger
from parser.schema import Product

connection = pg.connect(
    host='195.133.32.87',
    database='masha',
    port=5433,
    user='masha',
    password='mashamasha01'
)

cursor = connection.cursor()

def add_product(product: Product):
    sql = 'INSERT INTO public.ozon_products (product_name, product_price_original, ' \
          'product_price, product_price_with_ozon_card, product_images,' \
          'product_brand_name, product_brand_link, product_rating, ' \
          'product_categories, product_color, product_article, product_sizes,' \
          'product_all_articles, product_url, publication_category, verification, few_photos, is_published, description, sub_category) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,FALSE,%s,FALSE,%s,%s)' \
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
         product.few_photos,
         product.description,
         product.subcategory
         )
    ]

    # добавляем с помощью множественного запроса все данные сразу
    cursor.executemany(sql, data)
    connection.commit()

    if format(cursor.rowcount) == 0:
        logger.warning(f'Товар не добавлен (скорее всего он уже есть в базе данных): {product.article}')
    else:
        logger.info(f'Добавлен товар: {product.name}')


def get_product(id: int) -> Product:
    cursor.execute(
        f'''select product_name, product_price_original, product_price, product_price_with_ozon_card, product_images, product_brand_name, product_brand_link, 
        product_rating, product_categories, product_color, product_article, product_sizes, product_all_articles, publication_category, few_photos, 
        product_url, description, sub_category
     from public.ozon_products where product_id = {id}''')

    return Product(*cursor.fetchone())
