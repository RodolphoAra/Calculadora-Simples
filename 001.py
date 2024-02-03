print('---CALCULADORA EM PYTHON---')
while True:
    print('''Digite 1 para SOMA 
Digite 2 para SUBTRAÇÃO 
Digite 3 para MULTIPLICAÇÃO
Digite 4 para DIVISÃO''')
    p = int(input('Qual sua opção? '))
    if 1 > p > 4:
        print('Somente valores válidos.')
    else:
        n1 = float(input('Digite um nº: '))
        n2 = float(input('Digite um nº: '))
    if p == 1:
        s = (n1 + n2)
        print(f'A resposta é {s}')
    elif p == 2:
        sub = (n1 - n2)
        print(f'A resposta é {sub}')
    elif p == 3:
        m = (n1 * n2)
        print(f'A resposta é {m}')
    else:
        d = (n1 / n2)
        print(f'A resposta é {d}')
    fim = input('Deseja finalizar o programa (s/n)? ').lower()
    if fim == 's':
        print('Até logo...')
        break
