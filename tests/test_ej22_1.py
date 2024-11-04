import pytest
from src.bucles.ej22_1 import multiplicar_palabra  

def test_multiplicar_palabra(capsys, monkeypatch):
    palabra_test = "Hola"
    monkeypatch.setattr('builtins.input', lambda _: palabra_test)
    
    from src.bucles.ej22_1 import main 
    main()
    
    captured = capsys.readouterr()
    
    assert captured.out == f"{palabra_test}\n" * 10
