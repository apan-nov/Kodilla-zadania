# Twoim zadaniem będzie napisanie programu, któ®y wyszuka różne produkty i sprawdzi,
# czy ich oczekiwana ilość jest zgodna z rzeczywistą.
#
# Używając Selenium, otwórz w przeglądarce (Kodilla Store)
# Napisz kod, który będzie testował stronę https://kodilla.com/pl/test/store pod kątem wyszukiwanych fraz:
#
# NoteBook
# School
# Brand
# Business
# Gaming
# Powerful

# Dla potrzeb testów zakładamy, że w tym sklepie nigdy nie pojawi się żaden nowy produkt
# i wyniki wyszukiwania zawsze będą takie same.
# Dopisz testy, które zweryfikują, czy ilość zwróconych wyników odpowiada tej, której się spodziewamy.
# Następnie rozbuduj testy o weryfikację, czy wyszukiwarka ignoruje wielkość znaków przy wyszukiwaniu
# (ilość wyników powinna być taka sama niezależnie od wielkości znaków).

from selenium.webdriver.common.by import By
import time


def test_store(selenium):
    selenium.get("https://kodilla.com/pl/test/store/")
    search_textbox = selenium.find_element(By.XPATH, '//*[@id="searchField"]')

    def change_element(fraze, assert_value):
        search_textbox.clear()
        search_textbox.send_keys(fraze)
        elements = selenium.find_elements(By.XPATH, '//*[@id="elements-wrapper"]/div')
        num_of_elements = len(elements)
        assert (num_of_elements == assert_value), f"Wrong number of elements {fraze}- it should be {num_of_elements}"
        time.sleep(1)

    change_element("Laptop", 3)
    change_element("School", 1)
    change_element("Brand", 1)
    change_element("Business", 0)
    change_element("Gaming", 1)
    change_element("Powerful", 0)

# (ilość wyników powinna być taka sama niezależnie od wielkości znaków).
    change_element("LAPTOP", 3)

    time.sleep(5)
    selenium.quit()
