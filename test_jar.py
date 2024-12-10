from jar import Jar
import pytest

def test_init():
  with pytest.raises(ValueError):
    Jar(-3)
  with pytest.raises(ValueError):
    Jar(3.5)

def test_deposit():
  jar = Jar(5)
  jar.deposit(4)
  assert jar.size == 4
  with pytest.raises(ValueError):
    jar.deposit(2)

def test_str():
  jar = Jar()
  jar.size = 3
  assert jar.__str__() == 3 * "\N{Cookie}"

def test_witndraw():
  jar = Jar()
  jar.size = 4
  jar.witndraw(3)
  assert jar.size == 1
  with pytest.raises(ValueError):
    jar.withdraw(2)

