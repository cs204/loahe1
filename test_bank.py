from bank import value

def test_здравствуйте():
    assert value("Здравствуййте, Боб!") == 0

def test_здрасти():
    assert value ("Здрасти, Боб!") == 20

def teat_hello():
    assert value("Hello, Harry!") == 100
