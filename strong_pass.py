import random
import string

def generate_password(length=8):
    if length < 8:
        raise ValueError("Senha deve ter no mínimo 8 caracteres")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Garantia de ter pelo menos um de cada tipo de character/
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    # Preencher o restante dos espacos com a quantidade de characteres que o usuário escolheu
    for _ in range(length - 4):
        password.append(random.choice(characters))

    # Mistura os caracteres
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    password_length = int(input("Entre com o tamanho da senha desejada (mínimo 8 caracteres): "))
    password = generate_password(password_length)
    print(f"Senha gerada: {password}")