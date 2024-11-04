import pytest
from src.condicionales.ej21_10 import pedir_pizza, elegir_ingredientes  

def test_pedir_pizza_vegetariana(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'vegetariana')
    pizza = pedir_pizza()
    assert pizza == "vegetariana"

def test_pedir_pizza_normal(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'normal')
    pizza = pedir_pizza()
    assert pizza == "normal"

def test_pedir_pizza_invalid(monkeypatch):
    inputs = iter(['invalid', 'vegetariana'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    pizza = pedir_pizza()
    assert pizza == "vegetariana"

def test_elegir_ingredientes_normal(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'peperoni')
    pizza = elegir_ingredientes("normal")
    assert pizza == "Tu pizza no es vegetariana, y como base lleva tomate y mozzarella más tu personal que es peperoni"

def test_elegir_ingredientes_vegetariana(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'tofu')
    pizza = elegir_ingredientes("vegetariana")
    assert pizza == "Tu pizza es vegetariana, y como base lleva tomate y mozzarella más tu personal que es tofu"

def test_elegir_ingredientes_invalid_normal(monkeypatch):
    inputs = iter(['invalid', 'jamón'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    pizza = elegir_ingredientes("normal")
    assert pizza == "Tu pizza no es vegetariana, y como base lleva tomate y mozzarella más tu personal que es jamón"

def test_elegir_ingredientes_invalid_vegetariana(monkeypatch):
    inputs = iter(['invalid', 'pimiento'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    pizza = elegir_ingredientes("vegetariana")
    assert pizza == "Tu pizza es vegetariana, y como base lleva tomate y mozzarella más tu personal que es pimiento"
