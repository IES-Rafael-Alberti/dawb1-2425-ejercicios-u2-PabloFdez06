import pytest
from src.bucles.ej22_12 import pedir_frase, pedir_letra, contar_letras

def test_pedir_frase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Hola mundo')
    frase = pedir_frase()
    assert frase == 'hola mundo'

def test_pedir_letra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'a')
    letra = pedir_letra()
    assert letra == 'a'

def test_contar_letras_con_letra_present(monkeypatch):
    frase = 'Hola mundo'
    letra = 'o'
    resultado = contar_letras(frase, letra)
    assert resultado == "La letra ingresada se repite en total 2 veces."

def test_contar_letras_sin_letra_present(monkeypatch):
    frase = 'Hola mundo'
    letra = 'x'
    resultado = contar_letras(frase, letra)
    assert resultado == "La letra ingresada se repite en total 0 veces."

def test_contar_letras_con_letra_en_mayusculas(monkeypatch):
    frase = 'Hola Mundo'
    letra = 'M'
    resultado = contar_letras(frase.lower(), letra.lower())
    assert resultado == "La letra ingresada se repite en total 1 veces."
