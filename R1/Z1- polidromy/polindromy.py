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
def is_palindrome(data: str):
	print("Typ zmiennej: ", type(data))

	# remove whitespace nad special charakters from string
	data = ''.join(letter for letter in data if letter.isalnum())
	# change all letters to lowercase
	data = data.lower()

	data_length = len(data)
	data_l = data_length
	x = 0
	polindrome = True

	# check if string is not empty
	if data_length == 0:
		raise ValueError("\nNie podałeś słowa")

	while data_l > 0:
		# check if element is letter
		word_is_legal = data[x].isnumeric()
		if word_is_legal:
			raise ValueError("\nNie podawaj numerów")

		if data[x] != data[data_l-1]:
			polindrome = False

		x += 1
		data_l -= 1

	print("Czy to polindrom? " + str(polindrome))


data2 = input("Podaj słowo. Sprawdzimy, czy to polindrom. Słowo: ")
word_is_legal2 = is_palindrome(data2)
