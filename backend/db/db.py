from backend.db import cursor, connection, logger
from backend.parser.schema import Product

def add_product(product: Product):
    logger.info('Start add_product')

    sql = 'INSERT INTO public.test_ozon_products (product_name, product_price_original, ' \
          'product_price, product_price_with_ozon_card, product_images,' \
          'product_brand_name, product_brand_link, product_rating, ' \
          'product_categories, product_color, product_article, product_sizes,' \
          'product_all_articles, product_url, publication_category, ' \
          'verification, is_published, description, sub_category, stored) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,FALSE,FALSE,%s,%s,FALSE)' \
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
            product.sub_category
    )]

    cursor.executemany(sql, data)
    connection.commit()

    if format(cursor.rowcount) == 0:
        logger.warning(f'Товар не добавлен (скорее всего он уже есть в базе данных): {product.article}')
    else:
        logger.info(f'Добавлен товар: {product.name}, {product.article}')
    logger.info('End add_product')


def get_verification_information():
    cursor.execute(
        "select product_id, publication_category, sub_category,  product_name, product_article, product_price, product_images "
        "from public.test_ozon_products where (verification = false and stored = false) order by product_id")
    connection.commit()
    return cursor.fetchone()

def save_product(json):
    images = ''
    for image in json['images']:
        if json['images'][-1] == image:
            images += image
        else:
            images += image + ', '
    cursor.execute(
        "update public.test_ozon_products set product_name = '%s', product_images = '%s', verification = '%s' where product_id = '%s'" % (
            json['name'], images, True, json['id']
        )
    )
    connection.commit()

def delete_product(json):
    cursor.execute(
        "update public.test_ozon_products set verification = null where product_id = '%s'" % (
            json['id']
        )
    )
    connection.commit()

def store_category(json):
    cursor.execute(
        "update public.test_ozon_products set stored = true where publication_category = '%s'" % (
            json['category']
        )
    )
    connection.commit()

def return_all_categories():
    cursor.execute(
        "update public.test_ozon_products set stored = false where stored = true"
    )
    connection.commit()