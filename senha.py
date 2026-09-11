import string
import secrets

def gerar_senha(tamanho=12):
    # Definir os caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gerar a senha garantindo pelo menos um de cada tipo (minúscula, maiúscula, número, especial)
    while True:
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        if (any(c.islower() for c in senha)
                and any(c.isupper() for c in senha)
                and any(c.isdigit() for c in senha)
                and any(c in string.punctuation for c in senha)):
            break
            
    return senha

if __name__ == '__main__':
    senha_gerada = gerar_senha(12)
    print(f"Sua senha forte de 12 caracteres: {senha_gerada}")
