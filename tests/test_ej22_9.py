import pytest
from src.bucles.ej22_9 import almacenar_contrasenia, comprobar_contrasenia

def test_comprobar_contrasenia_correcta(capsys):
    contraseña_correcta = almacenar_contrasenia()
    comprobar_contrasenia(contraseña_correcta)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Contraseña Correcta!"

def test_comprobar_contrasenia_incorrecta(capsys):
    comprobar_contrasenia("contraseña_incorrecta")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Contraseña incorrecta...!"
