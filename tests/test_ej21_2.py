import pytest

def test_contrasenia_correcta(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "contraseña")
    from src.condicionales.ej21_2 import main  # Cambia 'src.condicionales.ej21_2' por el nombre real de tu archivo sin la extensión
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Contraseña Correcta!"

def test_contrasenia_incorrecta(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "Contraseta")
    from src.condicionales.ej21_2 import main  # Cambia 'src.condicionales.ej21_2' por el nombre real de tu archivo sin la extensión
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Contraseña incorrecta...!"
