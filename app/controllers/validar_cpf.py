
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