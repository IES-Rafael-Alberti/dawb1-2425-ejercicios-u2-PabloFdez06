import pytest
from src.bucles.ej22_4 import serie_edad, pedir_edad  

def test_serie_edad(capsys):
    serie_edad(5)
    captured = capsys.readouterr()
    assert captured.out == "5, 4, 3, 2, 1, 0\n"

def test_pedir_edad_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    edad = pedir_edad()
    assert edad == 5

def test_pedir_edad_invalida(monkeypatch):
    inputs = iter(['-1', 'abc', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    edad = pedir_edad()
    assert edad == 3

def test_pedir_edad_no_entero(monkeypatch):
    inputs = iter(['abc', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    edad = pedir_edad()
    assert edad == 7
