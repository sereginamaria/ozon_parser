from db import cursor, connection, logger
from parser_wb import schema
def add_product(product: schema.Product):
    logger.info('Start add_product')
    sql = 'INSERT INTO public.wb_products (product_name, product_price_original, ' \
          'product_price, product_images,' \
          'product_brand_name, product_rating, ' \
          'product_categories, product_color, product_article, product_sizes,' \
          'product_all_articles, product_url, publication_category, ' \
          'sub_category, verification, is_published, stored, description, styled_set) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,FALSE,FALSE,FALSE,%s,%s)' \
          'ON CONFLICT (product_article) DO NOTHING;'

    data = [(
            product.name,
            product.price_original,
            product.price,
            product.images,
            product.brand_name,
            product.rating,
            product.categories,
            product.color,
            product.article,
            product.sizes,
            product.all_articles,
            product.url,
            product.publication_category,
            product.sub_category,
            product.description,
            []
    )]

    cursor.executemany(sql, data)
    connection.commit()

    if cursor.rowcount == 0:
        logger.warning(f'Товар не добавлен (скорее всего он уже есть в базе данных): {product.article}')
    else:
        logger.info(f'Добавлен товар: {product.name}, {product.article}')
    logger.info('End add_product')

def get_verification_information():
    cursor.execute(
        "select product_id, publication_category, sub_category,  product_name, product_article, product_price, product_images "
        "from public.wb_products where (verification = false and stored = false) order by product_id")
    product_information = cursor.fetchone()

    cursor.execute(
        "select count(*) "
        " from public.wb_products where (publication_category = (select publication_category from public.wb_products "
         "where (verification = false and stored = false) order by product_id limit 1) and verification = true and is_published = false)")
    connection.commit()
    return product_information, cursor.fetchone()

def save_product(json, current_date):
    images = ''
    i = 1
    for image in json['images']:
        if i == len(json['images']):
            images += image
        else:
            images += image + ', '
        i += 1
    cursor.execute(
        "update public.wb_products set product_name = '%s', product_images = '%s', verification = '%s', "
        "sub_category = '%s', publication_category = '%s' where product_id = '%s'" % (
            json['name'], images, True, json['sub_category'], json['category'], json['id']
        )
    )
    connection.commit()

def delete_product(json):
    cursor.execute(
        "update public.wb_products set verification = null where product_id = '%s'" % (
            json['id']
        )
    )
    connection.commit()

def store_category(json):
    cursor.execute(
        "update public.wb_products set stored = true where (verification = false and publication_category = '%s')" % (
            json['category']
        )
    )
    connection.commit()

def return_all_categories():
    cursor.execute(
        "update public.wb_products set stored = false where stored = true"
    )
    connection.commit()

def get_products_for_post(json):
    cursor.execute(
        "select product_id, product_name, product_price_original, product_price, product_images, "
        "product_brand_name, product_rating, product_categories, product_sizes, product_color, "
        "product_article, product_all_articles, product_url, publication_category, description, sub_category "
        "from public.wb_products where (verification = true and is_published = false and "
        "publication_category = '%s') order by product_id limit 12" % (json['category']))

    connection.commit()
    return cursor.fetchall()


def count_of_verified_products():
    cursor.execute(
        "select publication_category, count(*) "
        " from public.wb_products where (verification = true and is_published = false) group by publication_category")
    connection.commit()
    return cursor.fetchall()

def count_of_not_verified_products():
    cursor.execute(
        "select publication_category, count(*) "
        " from public.wb_products where (verification = false and is_published = false) group by publication_category")
    connection.commit()
    return cursor.fetchall()

def publish_product(id, current_date):
    cursor.execute(
        "update public.wb_products set is_published = true, publication_date = '%s' where product_id = '%s'" % (
            current_date, id
        )
    )
    connection.commit()



def delete_product_from_db(json):
    cursor.execute(
        "delete from public.wb_products where product_id = '%s'" % (
            json['id']
        )
    )
    connection.commit()


def return_verification_false(id):
    cursor.execute(
        "update public.wb_products set verification = false where product_id = '%s'" % (
            id
        )
    )
    connection.commit()


def product_article_in_db(product_article):
    cursor.execute(
        " select "
        " EXISTS (select * from public.wb_products where product_article = '%s')" % (product_article))
    connection.commit()
    return cursor.fetchone()

def get_products_for_stile_card(product1, product2, product3, product4, current_date):
    product_categories_list = [product1, product2, product3, product4]

    products_list = []
    for product in product_categories_list:
        cursor.execute(
            "select product_id, product_name, product_price_original, product_price, product_images, "
            "product_brand_name, product_rating, product_categories, product_sizes, product_color, "
            "product_article, product_all_articles, product_url, publication_category, description, sub_category "
            "from public.wb_products where (publication_category = '%s' and is_published = true and publication_date > '%s') "
            "ORDER BY RANDOM() Limit 1" % (product, current_date)
        )
        connection.commit()
        products_list.append(cursor.fetchone())

    # print(products_list)
    return products_list

def save_styled_card(products_list):
    articles = [product['article'] for product in products_list]
    # print(articles)

    cursor.execute(
        "update public.wb_products set styled_set = styled_set || ARRAY[ARRAY %s ] "
        "where product_article = '%s'" % (
            articles, products_list[0]['article']
        )
    )
    connection.commit()

    for product in products_list:
        images = ''
        i = 1
        for image in product['images']:
            if i == len(product['images']):
                images += image
            else:
                images += image + ', '
            i += 1

        cursor.execute(
            "update public.wb_products set product_images = '%s' "
            "where product_article = '%s'" % (
                images, product['article']
            )
        )
        connection.commit()

def get_styled_card(current_date):
    import random

    cursor.execute(
        "select styled_set "
        "from public.wb_products where (is_published = true and publication_date > '%s' and ARRAY_LENGTH(styled_set, 1) IS NOT NULL) "
        "ORDER BY RANDOM()"
        % (current_date))

    styled_set = random.choice(cursor.fetchone()[0])
    # print('styled_set')
    # print(styled_set)
    # print(type(styled_set))

    # print(random.choice(styled_set[0]))

    products_list = []
    for product in styled_set:
        cursor.execute(
            "select product_id, product_name, product_price_original, product_price, product_images, "
            "product_brand_name, product_rating, product_categories, product_sizes, product_color, "
            "product_article, product_all_articles, product_url, publication_category, description, sub_category "
            "from public.wb_products where (product_article = '%s') "
            % (product)
        )
        connection.commit()
        products_list.append(cursor.fetchone())

    # print(products_list)
    return products_list

def get_stylist_panel_image(product_category, current_date):
    cursor.execute(
            "select product_id, product_name, product_price_original, product_price, product_images, "
            "product_brand_name, product_rating, product_categories, product_sizes, product_color, "
            "product_article, product_all_articles, product_url, publication_category, description, sub_category "
            "from public.wb_products where (publication_category = '%s' and is_published = true and publication_date > '%s') "
            "ORDER BY RANDOM() limit 1"
            % (product_category, current_date)
        )
    connection.commit()
    return cursor.fetchone()

def count_of_styled_cards(current_date):
    cursor.execute(
        "select count(*) "
        " from public.wb_products where (ARRAY_LENGTH(styled_set, 1) IS NOT NULL and publication_date > '%s')"
        % (current_date))
    connection.commit()
    return cursor.fetchone()