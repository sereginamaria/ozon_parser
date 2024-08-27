from db import cursor, connection, logger
from parser_ozon import schema

def add_product(product: schema.Product):
    logger.info('Start add_product')

    sql = 'INSERT INTO public.ozon_products (product_name, product_price_original, ' \
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
        "from public.ozon_products where (verification = false and stored = false) order by product_id")
    product_information = cursor.fetchone()

    cursor.execute(
        "select count(*) "
        " from public.ozon_products where (publication_category = (select publication_category from public.ozon_products "
         "where (verification = false and stored = false) order by product_id limit 1) and verification = true and is_published = false)")
    connection.commit()
    return product_information, cursor.fetchone()

def save_product(json):
    images = ''
    i = 1
    for image in json['images']:
        if i == len(json['images']):
            images += image
        else:
            images += image + ', '
        i += 1
    cursor.execute(
        "update public.ozon_products set product_name = '%s', product_images = '%s', verification = '%s', "
        "sub_category = '%s', publication_category = '%s' where product_id = '%s'" % (
            json['name'], images, True, json['sub_category'], json['category'], json['id']
        )
    )
    connection.commit()

def delete_product(json):
    cursor.execute(
        "update public.ozon_products set verification = null where product_id = '%s'" % (
            json['id']
        )
    )
    connection.commit()

def store_category(json):
    cursor.execute(
        "update public.ozon_products set stored = true where publication_category = '%s'" % (
            json['category']
        )
    )
    connection.commit()

def return_all_categories():
    cursor.execute(
        "update public.ozon_products set stored = false where stored = true"
    )
    connection.commit()

def get_products_for_post(json):
    cursor.execute(
        "select product_id, product_name, product_price_original, product_price, product_price_with_ozon_card, product_images, "
        "product_brand_name, product_brand_link, product_rating, product_categories, product_sizes, product_color, "
        "product_article, product_all_articles, product_url, publication_category, description, sub_category "
        "from public.ozon_products where (verification = true and is_published = false and "
        "publication_category = '%s') order by product_id limit 6" % (json['category']))

    connection.commit()
    return cursor.fetchall()


def count_of_verified_products():
    cursor.execute(
        "select publication_category, count(*) "
        " from public.ozon_products where (verification = true and is_published = false) group by publication_category")
    connection.commit()
    return cursor.fetchall()

def count_of_not_verified_products():
    cursor.execute(
        "select publication_category, count(*) "
        " from public.ozon_products where (verification = false and is_published = false) group by publication_category")
    connection.commit()
    return cursor.fetchall()

def publish_product(id):
    cursor.execute(
        "update public.ozon_products set is_published = true where product_id = '%s'" % (
            id
        )
    )
    connection.commit()