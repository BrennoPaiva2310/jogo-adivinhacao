perguntas = {

    'Pergunta 01':{
        'perguntas': 'Quanto é 2 + 2 ? ',
        'respostas': {'a': '4', 'b': '5', 'c': '6'},
        'resposta_certa': 'a'


    },
    'Pergunta 02': {
        'perguntas': 'Qual o nome do país onde moramos ? ',
        'respostas': {'a': 'EUA', 'b': 'Africa', 'c': 'Brasil'},
        'resposta_certa': 'c'

    },
    'Pergunta 03':{
        'perguntas': 'Qual o ano que estamos?',
        'respostas': {'a': '2022', 'b': '2011', 'c': '1999'},
        'resposta_certa': 'a'


    }

}

acertos = 0

for pk, pv in perguntas.items():
    print(f'\n{pk} : {pv["perguntas"]}')
    for dk,dv in pv["respostas"].items():
        print(f'{[dk]}{dv}')

    resposta_usuario = input('Digite sua resposta: ')

    if resposta_usuario == '':
        print('Digite uma resposta valida')
        continue

    if resposta_usuario == pv["resposta_certa"]:
        print('resposta Correta')
        acertos += 1
    else:
        print('Resposta Incorreta')

print(f'\nVocê acertou {acertos}')

qtd_perguntas = len(perguntas)
conta = acertos/qtd_perguntas * 100
print(f'\nSeu Percetual é {conta}% ')