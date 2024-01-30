#Twoim zadaniem jest napisanie miniaplikacji otwierającej przeglądarkę na stronie https://www.ebay.com/
# oraz wpisanie w pole wyszukiwania przedmiotów słowa "Laptop"
# oraz zatwierdzenie wyszukiwania, jak pokazano na poniższym zrzucie ekranu ( w paszku wyszukiwania)



# W celu realizacji zadania:
#
# Stwórz w pliku test_ebay funkcję testową korzystającą z fixutry selenium,
# W funkcji testowej napisz kod, który znajduje pole do wyszukiwania przedmiotów, wstawia do niego napis "Laptop" i zatwierdza wyszukiwanie,
# Użyj asercji, które stwierdzą, że procedury wykonała się poprawnie
# (np. sprawdź, że po lewej stronie, pod "Computers/Tablets & Networking" jest napis "Laptops & Netbooks").

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_store_search(selenium):

    selenium.get("https://www.ebay.com/")
    search = WebDriverWait(selenium, 60).until(
        lambda s: s.find_element(By.NAME, "_nkw")
    )
    search.send_keys("Laptop")

    element = WebDriverWait(selenium, 60).until(
        lambda s: s.find_element(By.XPATH, '//*[@id="gh-btn"]'))

    element.click()


    # Użyj asercji, które stwierdzą, że procedury wykonała się poprawnie
    # # (np. sprawdź, że po lewej stronie, pod "Computers/Tablets & Networking" jest napis "Laptops & Netbooks").
    assert_text = WebDriverWait(selenium, 20).until\
        (lambda s: s.find_element(By.XPATH, '//*[@id="x-refine__group__0"]/ul/li/ul/li[2]/a/span').text)
    assert assert_text == 'Laptops & Netbooks'

    time.sleep(5)
    selenium.quit()

# pytest test_ebay.py --driver Chrome