import re
import pytest
from strong_pass import generate_password

def test_tamanho_correto():
    for length in range(8, 20):
        password = generate_password(length)
        assert len(password) == length

def test_pelo_menos_um_maiuculo():
    password = generate_password()
    assert any(char.isupper() for char in password)

def test_pelo_menos_um_minusculo():
    password = generate_password()
    assert any(char.islower() for char in password)

def test_pelo_menos_um_digito():
    password = generate_password()
    assert any(char.isdigit() for char in password)

def test_pelo_menos_um_caractere_especial():
    password = generate_password()
    special_chars = re.compile('[' + re.escape('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~') + ']')
    assert bool(special_chars.search(password))

def test_tamanho_invalido():
    with pytest.raises(ValueError):
        generate_password(7)
