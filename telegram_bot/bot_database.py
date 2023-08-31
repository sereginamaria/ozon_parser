import sqlite3 as sl
import bot_requests

# открываем файл с базой данных
con = sl.connect('ozon_product_db.db', check_same_thread=False)


def verification_db():
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


def get_post_create_card_db(get_post_publication_category_post, get_post_publishing_platform, get_post_date_of_publication):
    with con:
        product = con.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images from ozon_products where (publication_category = '%s' and publishing_platform = '%s' and date_of_publication = '%s' and few_photos == false and verification == true) limit 30" % (get_post_publication_category_post, get_post_publishing_platform, get_post_date_of_publication))

    product_list = product.fetchall()
    bot_requests.create_card_request(product_list)
    return product_list

def create_card_db(publication_category_post):
    with con:
        product = con.execute(
            "select product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images from ozon_products where (publication_category = '%s' and date_of_publication is null and publishing_platform is null and few_photos == false and verification == true) limit 30" % publication_category_post)

    product_list = product.fetchall()
    bot_requests.create_card_request(product_list)
    return product_list

def choice_db(date_of_publication, publishing_platform, data):
    with con:
        con.execute(
            "update ozon_products set date_of_publication = '%s', publishing_platform = '%s' where product_id = '%s'" % (
                date_of_publication, publishing_platform, data.split('|')[1]))
