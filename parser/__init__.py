from flask import Flask
import undetected_chromedriver as uc
import logging
import sys
import atexit

app = Flask(__name__, template_folder='../card_creator/templates')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

ucOptions = uc.ChromeOptions()
# ucOptions.headless = False
# ucOptions.add_argument('--headless')
# ucOptions.add_argument('--headless=new')
ucOptions.add_argument('--no-sandbox')
ucOptions.add_argument('--disable-dev-shm-usage')

# ucOptions.add_argument("--disable-extensions")
ucOptions.add_argument('--disable-application-cache')
ucOptions.add_argument("--disable-setuid-sandbox")
ucOptions.add_argument("--disable-gpu")
ucOptions.add_argument("--remote-allow-origins=*")
# ucOptions.add_argument("--log-path=/home/masha/chromelogs")
ucOptions.add_argument("--disable-dev-shm-usage")
ucOptions._session = None

# ucOptions.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-linux64/chrome'
# ucOptions.binary_location = '/home/masha/ozon_parser/chromedriver/chrome117/chrome-linux64/chrome'
# ucOptions.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-headless-shell-linux64/chrome-headless-shell'

driver = uc.Chrome(
    # driver_executable_path='/home/masha/ozon_parser/chromedriver/chromedriver-linux64/chromedriver',
    patcher_force_close=True, no_sandbox=True, suppress_welcome=True, use_subprocess=True,
    options=ucOptions,
    log_level=10)


def exit_handler():
    driver.quit()


atexit.register(exit_handler)
