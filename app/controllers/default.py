from app import app
from flask import Response
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