
def validar( cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se possui 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcular o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    d1 = (soma * 10) % 11 if soma % 11 > 1 else 0
    
    # Verificar o primeiro dígito verificador
    if d1 != int(cpf[9]):
        return False
    
    # Calcular o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    d2 = (soma * 10) % 11 if soma % 11 > 1 else 0
    
    # Verificar o segundo dígito verificador
    if d2 != int(cpf[10]):
        return False
    
    return True


def validar_cnpj(cnpj: str) -> bool:
    # Remove tudo que não é número
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Deve ter 14 dígitos
    if len(cnpj) != 14:
        return False

    # Não pode ter todos os dígitos iguais
    if cnpj == cnpj[0] * 14:
        return False

    # Calcula o primeiro dígito verificador
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    digito1 = 11 - soma1 % 11
    digito1 = digito1 if digito1 < 10 else 0

    # Calcula o segundo dígito verificador
    pesos2 = [6] + pesos1
    soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    digito2 = 11 - soma2 % 11
    digito2 = digito2 if digito2 < 10 else 0

    # Verifica se os dígitos conferem
    return cnpj[-2:] == f"{digito1}{digito2}"