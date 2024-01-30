import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_store_search(selenium):
    selenium.get("https://kodilla.com/pl/test/store")
    search = WebDriverWait(selenium, 60).until(
        lambda s: s.find_element(By.NAME, "search")
    )
    search.send_keys("School")
    time.sleep(3)
    selenium.quit()

    element.click()
