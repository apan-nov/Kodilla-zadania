# Rozkład liczby całkowitej na czynniki pierwsze jest algorytmem istotnym z punktu widzenia kryptografii.
# Stosując technikę TDD, zaimplementuj funkcję prime_factors(number),
# zwracającą czynniki pierwsze number w postaci listy.
# Jeśli number jest liczbą pierwszą, lista powinna zawierać wyłącznie ją samą.
# Przykładowo: prime_factors(3958159172) powinno zwrócić [2, 2, 11, 2347, 38329].
#
# Liczy się proces dochodzenia do rozwiązania (udokumentowany historią repozytorium),
# a nie samo rozwiązanie. Nie zapomnij o uwzględnieniu przypadków szczególnych.
from contextlib import suppress
from behave import given


################

def prime_factors(number):
	return 1

# 1) Write tests that pass only if feature specifications are met


# number is not a number
@given("not_a_number")
def not_a_number(self):
	number2 = 'asd{}:}:'
	result = prime_factors(number2)
	assert result is None, "this should be WrongInputError"


# number is null
@given("null")
def null(self):
	number2 = ''
	result = prime_factors(number2)
	assert result is None, "this should be EmptyInputError"


# number is not an int
@given("not_a_int")
def not_a_int(self):
	number2 = '123.15'
	result = prime_factors(number2)
	assert result is None, "this should be NotIntInputError"


# number is 0
@given("not_a_zero")
def not_a_zero(self):
	number2 = '0'
	result = prime_factors(number2)
	assert result is None, "this should be ZeroInputError"


# number is negative int
@given("negrative_int")
def negrative_int(self):
	number2 = '-12'
	result = prime_factors(number2)
	assert result is None, "this should be NegativeIntInputError"


# number is Prime number
@given("prime_number")
def prime_number(self):
	number2 = '13'
	result = prime_factors(number2)
	assert result == [13, 1], "this should be Prime"


# number is not a Prime number
@given("not_a_prime_number")
def not_a_prime_number(self):
	number2 = '21'
	result = prime_factors(number2)
	assert result == [3, 7, 1], "this should be NotPrime"


# 2) Fail all of those tests ()


# 3) Write SIMPLEST code to pass those test
# (simplest code dosn't have to be great- just meets specification, do the job and be simple0

# 4) Run ALL test- they all needs to work

# 5) Refactor and improve
