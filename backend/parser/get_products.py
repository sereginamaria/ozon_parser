from backend.parser import logger, config, driver
def parse_page(publication_category, url):
    logger.info('Start parse page')
    pages = [get_html(url + '?page=' + str(i)) for i in range(1, config.MAX_PAGES + 1)]

def get_html(url):
    logger.info('Start get_html')
    logger.info(f'Viewing {url}')
    driver.get(url)
    driver.execute_script("window.scrollTo(5,4000);")
    import time
    time.sleep(5)
    html = driver.page_source
    return html