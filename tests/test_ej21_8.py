import pytest
from src.condicionales.ej21_8 import pedir_puntuacion, comprobar_nivel  

def test_pedir_puntuacion_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '0.4')
    puntuacion = pedir_puntuacion()
    assert puntuacion == 0.4

def test_pedir_puntuacion_invalida(monkeypatch):
    inputs = iter(['1.0', 'abc', '0.6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    puntuacion = pedir_puntuacion()
    assert puntuacion == 0.6

def test_comprobar_nivel_inaceptable():
    assert comprobar_nivel(0.0) == "Tu puntuacion de este año es inaceptable"

def test_comprobar_nivel_aceptable():
    assert comprobar_nivel(0.4) == "Tu puntuación de este año es aceptable, recibiras: 960.0€"

def test_comprobar_nivel_meritorio():
    assert comprobar_nivel(0.6) == "Tu puntuación de este año es aceptable, recibiras: 1440.0€"
