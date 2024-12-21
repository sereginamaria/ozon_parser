from my_parsers.parser_db import cursor, connection, logger
from my_parsers.parser_ozon import schema

def add_product(product: schema.Product):
    logger.info('Start add_product')

    sql = 'INSERT INTO public.ozon_products (product_name, product_price_original, ' \
          'product_price, product_price_with_ozon_card, product_images,' \
          'product_brand_name, product_brand_link, product_rating, ' \
          'product_categories, product_color, product_article, product_sizes,' \
          'product_all_articles, product_url, publication_category, ' \
          'verification, is_published, description, sub_category, stored, styled_set) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,FALSE,FALSE,%s,%s,FALSE,%s)' \
          'ON CONFLICT (product_article) DO NOTHING;'

    data = [(
            product.name,
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
            product.sub_category,
            []
    )]

    cursor.executemany(sql, data)
    connection.commit()

    if format(cursor.rowcount) == 0:
        logger.warning(f'Товар не добавлен (скорее всего он уже есть в базе данных): {product.article}')
    else:
        logger.info(f'Добавлен товар: {product.name}, {product.article}')
    logger.info('End add_product')
