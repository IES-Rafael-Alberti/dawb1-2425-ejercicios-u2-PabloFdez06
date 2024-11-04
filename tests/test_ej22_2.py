import pytest
from src.bucles.ej22_2 import serie_edad, pedir_edad

def test_serie_edad(capsys):
    serie_edad(5)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n4\n5\n"

def test_pedir_edad_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '25')
    edad = pedir_edad()
    assert edad == 25

def test_pedir_edad_invalida(monkeypatch):
    inputs = iter(['-5', 'abc', '20'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    edad = pedir_edad()
    assert edad == 20

def test_pedir_edad_no_entero(monkeypatch):
    inputs = iter(['abc', '30'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    edad = pedir_edad()
    assert edad == 30
