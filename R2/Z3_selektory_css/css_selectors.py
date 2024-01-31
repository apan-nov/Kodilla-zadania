# Twoim zadaniem będzie zmodyfikowanie projektu z submodułu o selektorach XPath.
#
# Wszystkie selektory XPath zmodyfikuj, aby używać CSS_SELECTOR, TAG_NAME, ID lub CLASS_NAME. Wybór należy do Ciebie.
#
# Dodaj wait, który poczeka na pierwszy wynik wyszukiwania.
# Po wyświetleniu się wyników wyszukiwania znajdź wszystkie karty produktów i przypisz je do jednej listy.
#
# Wskazówka: skorzystaj z driver.find_element oraz np. z selektora css section>article.
#
# Za pomocą pola text wyświetl informacje o produkcie.
# Nie musisz pisać oddzielnych selektorów,
# wystarczy dla każdego elementu z listy produktów pobrać text, aby wyświetlić wszystkie informacje o produkcie.
from selenium.webdriver.common.by import By
import time
import subprocess

def test_store(selenium):
    selenium.get("https://kodilla.com/pl/test/store/")
    search_textbox = selenium.find_element(By.CSS_SELECTOR, '#searchField')

    def change_element(fraze, assert_value):
        search_textbox.clear()
        search_textbox.send_keys(fraze)

        elements = selenium.find_elements(By.CSS_SELECTOR, '#elements-wrapper > div')
        num_of_elements = len(elements)
        assert (num_of_elements == assert_value), f"Wrong number of elements {fraze}- it should be {num_of_elements}"
        # there is no os.wait() for windows
        time.sleep(1)

    change_element("Laptop", 3)
    change_element("NoteBook", 2)
    change_element("Gaming", 1)
    change_element("Bussines", 1)

    time.sleep(5)
    selenium.quit()
