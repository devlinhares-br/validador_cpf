from app import app
from flask import Response, request
from app.controllers import validar_estado
from app.controllers import validar_cpf
import json, re


@app.route('/', methods=['GET'])
def index():
    return geraResponse(200, 'result', 'OK')


@app.route('/validar_cpf/<cpf>', methods=['GET'])
def validar(cpf):
    padrao_cpf = r'^\d+$'
    if re.match(padrao_cpf, cpf):
        validacao = validar_cpf.validar(cpf)
        if validacao:
            return cpf_valido(cpf)
        else:
            return cpf_invalido(cpf)
    else:
        return cpf_invalido(cpf)

@app.route('/validar_cpf', methods=['POST'])    
@app.route('/validar_cnpj/', methods=['POST'])
def validar_cnpj_endpoint():
    cnpj = request.json.get('cnpj','')
    if validar_cpf.validar_cnpj(cnpj):
        return cnpj_valido(cnpj)
    else:
        return cnpj_invalido(cnpj)

@app.route('/validar_estado/', methods=['POST'])
@app.route('/validar_estado', methods=['POST'])
def validar_estado_endpoint():
    data = request.get_json()
    if not data or 'estado' not in data:
        return geraResponse(400, 'result', {'erro': 'Campo "estado" obrigatório'})

    estado_nome = data['estado']
    sigla = validar_estado.obter_sigla_estado(estado_nome)

    if sigla:
        return geraResponse(200, 'result', {'estado': estado_nome, 'sigla': sigla})
    else:
        return geraResponse(400, 'result', {'erro': 'Estado inválido'})


def geraResponse(status, nome_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_conteudo] = conteudo
    if mensagem:
        body['mesage'] = mensagem
    return Response(json.dumps(body), status, mimetype='application/json')

def cpf_invalido(cpf):
    data = {'CPF': False,
            f'{cpf}': 'Inválido'}
    return geraResponse(400, 'result', data)

def cpf_valido(cpf):
    data = {'CPF': True,
            f'{cpf}': 'Valido'}
    return geraResponse(200, 'result', data)

def cnpj_valido(cnpj):
    data = {'CNPJ': True,
            f'{cnpj}': 'Valido'}
    return geraResponse(200, 'result', data)

def cnpj_invalido(cnpj):
    data = {'CNPJ': False,
            f'{cnpj}': 'Inválido'}
    return geraResponse(400, 'result', data)