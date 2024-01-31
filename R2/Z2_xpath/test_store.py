# Twoim zadaniem będzie napisanie programu, któ®y wyszuka różne produkty i sprawdzi,
# czy ich oczekiwana ilość jest zgodna z rzeczywistą.
#
# Używając Selenium, otwórz w przeglądarce (Kodilla Store)
# [https://kodilla.com/pl/test/store]
# , a następnie rozpocznij korzystanie z elementu "Szukaj..." w celu znalezienia produktów.
# Efektem końcowym (w kodzie) mają być funkcje,
# który sprawdzają ilość wyników po wpisaniu frazy - mniej-więcej (lub dokładnie) w taki sposób:
#
# ...
# assert_amount(driver, "Laptop", "3")
# assert_amount(driver, "NoteBook", "2")
# assert_amount(driver, "Gaming", "1")

# Powyższy kod sprawdzi, czy po wpisaniu frazy "Laptop" w polu wyszukiwania,
# liczba wyników jest równa 3. Jeżeli nie, to test ma nie przejść.
# Następnie, po wpisaniu frazy "NoteBook" w polu wyszukiwania, liczba wyników ma być równa 2.
# Jeżeli nie, to test ma nie przejść. I tak dalej.
# Wywołaj możliwie dużo funkcji assert_amount i zbuduj sobie na podstawie tego ogląd tego,
# ile produktów jakiej kategorii jest w sklepie.
#
# W celu zrealizowania zadania:
#
# Utwórz plik test_store.py, a w nim funkcję test_store().
# Korzystając z XPath-Relative, napisz kod spełniający powyższe wymagania.

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
    change_element("NoteBook", 2)
    change_element("Gaming", 1)
    change_element("Bussines", 1)

    time.sleep(5)
    selenium.quit()
