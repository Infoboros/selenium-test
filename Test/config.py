from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'http://127.0.0.1'

options = Options()
manager = ChromeDriverManager().install()
