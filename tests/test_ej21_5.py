import pytest

def test_comprobacion_tributaria_mayor_16_y_mas_de_1000(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "20" if "edad" in _ else "1500")
    from src.condicionales.ej21_5 import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Cumples los requisitos necesarios para tributar!"

def test_comprobacion_tributaria_menor_16(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "15" if "edad" in _ else "1500")
    from src.condicionales.ej21_5 import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "No cumples los requisitos necesarios para tributar! FELICIDADES."

def test_comprobacion_tributaria_menos_de_1000(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "20" if "edad" in _ else "900")
    from src.condicionales.ej21_5 import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "No cumples los requisitos necesarios para tributar! FELICIDADES."

def test_comprobacion_tributaria_exactamente_1000(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "17" if "edad" in _ else "1000")
    from src.condicionales.ej21_5 import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Cumples los requisitos necesarios para tributar!"
