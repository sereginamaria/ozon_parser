from get_product_json import get_product_json
from get_products_from_page import get_products_from_page

def main():
    #Получить json продукта по ссылке на продукт
     #get_product_json("/product/plate-tvoe-560729011/")

    # Получить ссылки на продукты по страницам
    get_products_from_page("https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Летнее+платье")


if __name__ == "__main__":
    main()