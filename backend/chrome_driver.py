import undetected_chromedriver as uc
import logging
import atexit
import sys

# driver = ''

ucOptions = uc.ChromeOptions()
# ucOptions.headless = False
# ucOptions.add_argument('--headless')
ucOptions.add_argument('--headless=new')
# ucOptions.add_argument('--no-sandbox')

# ucOptions.add_argument("--disable-extensions")
ucOptions.add_argument('--disable-application-cache')
# ucOptions.add_argument("--disable-setuid-sandbox")
# ucOptions.add_argument("--disable-gpu")
ucOptions.add_argument("--remote-allow-origins=*")
# ucOptions.add_argument("--log-path=/home/masha/chromelogs")
ucOptions.add_argument("--disable-dev-shm-usage")
ucOptions.add_argument("--lang=ru-ru")
ucOptions.add_argument("--ozone-platform=wayland")
ucOptions._session = None

ucOptions.binary_location = '/home/vk/Downloads/chrome_6778_13/chrome-linux64/chrome'
# ucOptions.binary_location = '/home/masha/ozon_parser/chromedriver/chrome117/chrome-linux64/chrome'
# ucOptions.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-headless-shell-linux64/chrome-headless-shell'

driver = uc.Chrome(
    # driver_executable_path='/home/masha/ozon_parser/chromedriver/chromedriver-linux64/chromedriver',
    driver_executable_path='/home/vk/Downloads/chromedriver_6778_13/chromedriver-linux64/chromedriver',
    # patcher_force_close=True, 
    # enable_cdp_events=True,
    no_sandbox=False, 
    suppress_welcome=True, use_subprocess=True,
    options=ucOptions,
    log_level=0)

def printmessage(message):
    print(pformat(message))


# to print all evenets
driver.add_cdp_listener('*', printmessage)


def exit_handler():
    driver.quit()


atexit.register(exit_handler)