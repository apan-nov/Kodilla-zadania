# Napisz funkcję is_palindrome, która sprawdza czy argument jest palindromem,
# a następnie przetestuj na odpowiednio dobranych przypadkach.
# Postaraj się uwzględnić sytuacje graniczne i nieprawidłowe dane wejściowe. Liczy się kreatywność, psuj śmiało!
#
# def is_palindrome(data):
#     ...
# Nie bój się sukcesywnie dodawać nowych warunków.
# Sformułuj kryteria akceptacji (zakres funkcjonalności).
# Jeśli w trakcie pracy naprawisz błąd, dodaj ilustrujący go przypadek.


# przykładowy polindrom A man, a plan, a canal – Panama
##################
# Twoja funkcja jest bardzo skomplikowana, uprośćmy ją do takiej postaci i napisz do niej test:

# def is_palindrome(word):
#     return word == word[::-1]


# Przez test rozumiem na przykłąd napisanie testu z użyciem frameworku "pytest" i wykorzystaniem dekoratora "pytest.mark.parametrized"

import pytest


def reverse_word(word):
	# remove whitespace nad special charakters from string
	word = ''.join(letter for letter in word if letter.isalnum())
	# change all letters to lowercase
	word = word.lower()
	# check if string is not empty
	if len(word) == 0:
		raise ValueError("\nNie podałeś słowa")
	return word[::-1]


@pytest.mark.parametrize("word, result",
						 [('ananas', 'sanana'),
						  ('A man, a plan, a canal – Panama', 'amanaplanacanalpanama'),
						  (7421, str(1247)),
						  ("%#$", ''),
						  ('', '')])
def test_multiplication(word, result):
	try:
		assert reverse_word(str(word)) == result
	except ValueError:
		print("Value Error- to nie polindrom")
