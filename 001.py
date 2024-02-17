print('---Python Calculator---')
while True:
    print('''TYPE 1 for ADDITION 
TYPE 2 for SUBTRACTION
TYPE 3 for MULTIPLICATION
TYPE 4 for DIVISION''')
    p = int(input('Which option? '))
    if p < 1 or p > 4:
        print('Only valid values.')
    else:
        n1 = float(input('Enter a number: '))
        n2 = float(input('Enter a number: '))
    if p == 1:
        s = (n1 + n2)
        print(f'The answer is {s}')
    elif p == 2:
        sub = (n1 - n2)
        print(f'The answer is {sub}')
    elif p == 3:
        m = (n1 * n2)
        print(f'The answer is {m}')
    elif p == 4:
        d = (n1 / n2)
        print(f'The answer is {d}')
    fim = input('Do you want to finish the program (y/n)? ').lower()
    if fim == 'y':
        print('See you soon...')
        break
