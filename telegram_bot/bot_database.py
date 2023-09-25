import sqlite3 as sl
import bot_requests

# открываем файл с базой данных
con = sl.connect('ozon_product_db.db', check_same_thread=False)


def verification():
    with con:
        products = con.execute(
            "select product_id, product_images from ozon_products where (verification != true) limit 1")
    return products


def callback_verification(data):
    if data.split('|')[1] == "yes":
        with con:
            con.execute("update ozon_products set verification = true where product_id ==" + str(data.split('|')[2]))
    if data.split('|')[1] == "no":
        with con:
            con.execute("delete from ozon_products where product_id == " + str(data.split('|')[2]))


def create_post(date_of_publication, time_of_publication, publishing_platform, product_id):
    with con:
        con.execute(
            "update ozon_products set date_of_publication = '%s', time_of_publication = '%s', publishing_platform = '%s' where product_id = '%s'" % (
                date_of_publication, time_of_publication, publishing_platform, product_id))


def create_card(publication_category):
    with con:
        product = con.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images from ozon_products where (publication_category = '%s' and "
            "date_of_publication is null and publishing_platform is null and few_photos == false and verification == "
            "true) limit 30" % publication_category)

    product_list = product.fetchall()
    bot_requests.create_card(product_list)
    return product_list


def get_post_from_db(publication_category, publication_platform, date_of_publication):
    with con:
        product = con.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images from ozon_products where (publication_category = '%s' and "
            "publishing_platform = '%s' and date_of_publication = '%s' and few_photos == false and verification == "
            "true) limit 30" % (publication_category, publication_platform, date_of_publication))

    product_list = product.fetchall()
    bot_requests.create_card(product_list)

def autoposting_date(now, time):
    with con:
        product = con.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, "
            "product_price_with_ozon_card, product_images, publication_category, product_url "
            "from ozon_products where (date_of_publication = '%s' and time_of_publication <= '%s' "
            "and few_photos == false and verification == "
            "true and published == false)" % (str(now), time))



    product_list = product.fetchall()
    bot_requests.create_post(product_list)

    print(product_list)
    for product in product_list:
        (product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card,
         product_images, publication_category, product_url) = product
        print(product_id)
        with con:
            con.execute(
                "update ozon_products set published = true where product_id = '%s'" % (product_id))
