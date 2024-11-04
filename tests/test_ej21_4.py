import pytest
from src.condicionales.ej21_4 import comprueba_parimpar  

def test_comprueba_parimpar_par(capsys):
    resultado = comprueba_parimpar(4)
    assert resultado == "El número indicado es par"

def test_comprueba_parimpar_impar(capsys):
    resultado = comprueba_parimpar(5)
    assert resultado == "El número indicado es impar"

def test_comprueba_parimpar_zero(capsys):
    resultado = comprueba_parimpar(0)
    assert resultado == "El número indicado es par"

def test_input_par(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '10')
    from src.condicionales.ej21_4 import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "El número indicado es par"

def test_input_impar(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '7')
    from src.condicionales.ej21_4 import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "El número indicado es impar"
