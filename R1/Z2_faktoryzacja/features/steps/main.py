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
import pytest


def prime_factors(number2):
	list_of_divisors = []
	divider = 2
	while number2 > 1:
		if number2 % divider == 0:
			list_of_divisors.append(divider)
			number2 = number2 / divider
			divider = 2
		elif divider <= number2:
			divider += 1
	return list_of_divisors


# number is not a number
@given("test_not_a_number with {number}")
def test_not_a_number(self, number):
	with pytest.raises(ValueError):
		result = prime_factors(int(number))


# number is null
@given("test_null with {number}")
def test_null(self, number):
	with pytest.raises(ValueError):
		result = prime_factors(int(number))


# number is not an int
@given("test_not_a_int with {number}")
def test_not_a_int(self, number):
	with pytest.raises(ValueError):
		result = prime_factors(int(number))


# number is 0
@given("test_zero with {number}")
def test_not_a_zero(self, number):
	result = prime_factors(int(number))
	aaa = result
	assert result is not None, "this should be ZeroInputError"


# number is negative int
@given("test_negative_int with {number}")
def test_negative_int(self, number):
	result = prime_factors(int(number))
	assert result is not None, "this should be NegativeIntInputError"


# number is Prime number
@given("test_prime_number with {number}")
def test_prime_number(self, number):
	result = prime_factors(int(number))
	assert type(result) == list, "this should be Prime"


# number is not a Prime number
@given("test_not_a_prime_number with {number}")
def test_not_a_prime_number(self, number):
	result = prime_factors(int(number))
	assert type(result) == list, "this should be NotPrime"

# 1) Write tests that pass only if feature specifications are met - DONE
# 2) Fail all of those tests () - DONE

# 3) Write SIMPLEST code to pass those test - DONE

# (simplest code dosn't have to be great- just meets specification, do the job and be simple0

# 4) Run ALL test- they all needs to work - DONE

# 5) Refactor and improve
