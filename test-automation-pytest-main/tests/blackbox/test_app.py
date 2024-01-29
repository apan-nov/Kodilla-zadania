import subprocess

def test_addition():
    result = subprocess.run(['python', 'main.py', '2', '+', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '5\n'

# TODO