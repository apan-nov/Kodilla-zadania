import subprocess
# BLACKBOX


def test_addition_positive():
    result = subprocess.run(['python', 'main.py', '2', '+', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '5\r\n'


def test_addition_negative():
    result = subprocess.run(['python', 'main.py', '-3', '+', '-5'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-8\r\n'


def test_addition_zeros():
    result = subprocess.run(['python', 'main.py', '0', '+', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'


def test_subtraction_positive():
    result = subprocess.run(['python', 'main.py', '6', '-', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '4\r\n'


def test_subtraction_negative():
    result = subprocess.run(['python', 'main.py', '-7', '-', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-4\r\n'

def test_subtraction_zeros():
    result = subprocess.run(['python', 'main.py', '0', '-', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'


# multiplication does not work
def test_multiplication_positive():
    result = subprocess.run(['python', 'main.py', '6', '*', '8'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '48\r\n'


def test_multiplication_negative():
    result = subprocess.run(['python', 'main.py', '-3', '*', '-6'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '18\r\n'


def test_multiplication_by_zero():
    result = subprocess.run(['python', 'main.py', '0', '*', '4'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'
###############################################


def test_division_positive():
    result = subprocess.run(['python', 'main.py', '8', '/', '4'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '2\r\n'


def test_division_negative():
    result = subprocess.run(['python', 'main.py', '-4', '/', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-2.0\r\n'


def test_division_zero():
    result = subprocess.run(['python', 'main.py', '0', '/', '-2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0.0\r\n'


# Negative tests
def test_division_by_zero():
        result = subprocess.run(['python', 'main.py', '9', '/', '0'], stdout=subprocess.PIPE)
        assert result.stdout.decode('utf-8') == ''


def test_lack_of_dividend():
    result = subprocess.run(['python', 'main.py', '', '/', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == ''


def test_lack_of_divider():
    result = subprocess.run(['python', 'main.py', '4', '/', ''], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == ''


def test_too_many_arguments():
    result = subprocess.run(['python', 'main.py', '4', '/', '2', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == ''


def test_not_numbers():
    result = subprocess.run(['python', 'main.py', 'asd', '/', '&*(', ], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == ''


def test_not_intigers():
    result = subprocess.run(['python', 'main.py', '7.34', '/', '2.3', ], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == ''
