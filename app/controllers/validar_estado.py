import unicodedata

def obter_sigla_estado(estado: str) -> str:
    if not estado:
        return None

    # Remove acentos e converte para minúsculo
    estado_normalizado = ''.join(
        c for c in unicodedata.normalize('NFD', estado)
        if unicodedata.category(c) != 'Mn'
    ).lower().strip()

    # Dicionário de equivalências (nome → sigla)
    estados = {
        "acre": "AC",
        "alagoas": "AL",
        "amapa": "AP",
        "amazonas": "AM",
        "bahia": "BA",
        "ceara": "CE",
        "distrito federal": "DF",
        "espirito santo": "ES",
        "goias": "GO",
        "maranhao": "MA",
        "mato grosso": "MT",
        "mato grosso do sul": "MS",
        "minas gerais": "MG",
        "para": "PA",
        "paraiba": "PB",
        "parana": "PR",
        "pernambuco": "PE",
        "piaui": "PI",
        "rio de janeiro": "RJ",
        "rio grande do norte": "RN",
        "rio grande do sul": "RS",
        "rondonia": "RO",
        "roraima": "RR",
        "santa catarina": "SC",
        "sao paulo": "SP",
        "sergipe": "SE",
        "tocantins": "TO",
    }

    # Se já for sigla válida
    for sigla in estados.values():
        if estado_normalizado == sigla.lower():
            return sigla

    # Procura por nome completo
    return estados.get(estado_normalizado)