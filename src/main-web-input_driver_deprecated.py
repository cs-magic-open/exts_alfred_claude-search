"""
使用 driver 很慢，而且完了就关闭浏览器了，不推荐，仅供学习
"""
import sys

# ref: https://stackoverflow.com/a/78006137/9422455
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import get_chrome_user_data_dir


def operate_on_claude(driver, query):
    driver.get("https://claude.ai/new")

    input_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "core div[aria-label='Write your prompt to Claude'] div[contenteditable='true']")))

    input_field.send_keys(query)
    input_field.send_keys(Keys.RETURN)


def main(query):
    chrome_options = uc.ChromeOptions()

    # decide which profile to use
    chrome_options.add_argument(f"--user-data-dir={get_chrome_user_data_dir()}")
    chrome_options.add_argument("--profile-directory=Default")  # or your specific profile

    # chrome_options.add_argument("--window-size=1280,960")
    # chrome_options.add_argument("--window-position=0,0")

    # [dev] enhancer
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # [dev] keep dev open
    # chrome_options.add_argument("--auto-open-devtools-for-tabs")

    try:

        driver = uc.Chrome(options=chrome_options)

        # driver.get('https://bot.sannysoft.com/')
        # driver.save_screenshot('out/walkaround.png')

        # driver.get("https://github.com/markshawn2020")

        operate_on_claude(driver, query)
    finally:
        # input("Press Enter to close the browser...")
        # time.sleep(30)
        # driver.quit()
        pass


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "hello world"
    main(query)
