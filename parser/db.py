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
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS public.ozon_products (
    #         product_id SERIAL PRIMARY KEY,
    #         product_name TEXT,
    #         product_price_original TEXT,
    #         product_price TEXT,
    #         product_price_with_ozon_card TEXT,
    #         product_images TEXT,
    #         product_brand_name TEXT,
    #         product_brand_link TEXT,
    #         product_rating TEXT,
    #         product_categories TEXT,
    #         product_sizes TEXT,
    #         product_color TEXT,
    #         product_article TEXT unique,
    #         product_all_articles TEXT,
    #         product_url TEXT,
    #         date_of_publication DATE,
    #         time_of_publication TIME,
    #         publication_category TEXT,
    #         publishing_platform TEXT,
    #         verification BOOLEAN,
    #         few_photos BOOLEAN,
    #         is_published BOOLEAN,
    #         post_type TEXT,
    #         description TEXT,
    #         sub_category TEXT
    #     );
    # """)


    # подготавливаем множественный запрос
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