import os

while True:
    cpf_digitado = input('Digite seu CPF: ')

    organizar_cpf = []
    for remover_pontos in cpf_digitado:
        try:
            remover_pontos = int(remover_pontos)
            organizar_cpf.append(remover_pontos)
        except ValueError:
            continue

    verificar_cpf_repetido = []
    for verificador in organizar_cpf:
        verificar_cpf_repetido.append(organizar_cpf[0])

    if organizar_cpf == verificar_cpf_repetido:
        os.system('cls')
        print('Você digitou números repetidos, digite novamente.\n')
        continue
 
    qtd_cpf = len(organizar_cpf)
    if qtd_cpf > 11:
        os.system('cls')
        print('Você digitou números a mais, digite novamente.\n')
    elif qtd_cpf < 11:
        os.system('cls')
        print('Você digitou números a menos, digite novamente.\n')
    else:
        i = 10
        multi_num_1 = []
        for conta_multi_cpf_1 in organizar_cpf:
            conta_multi_cpf_1 *= i
            i -= 1
            multi_num_1.append(int(conta_multi_cpf_1))
            if i == 1:
                break

        soma_num_1 = 0
        for conta_soma_cpf_1 in multi_num_1:
            soma_num_1 += conta_soma_cpf_1

        multi10_num_1 = soma_num_1 * 10
        restodiv_num_1 = multi10_num_1 % 11

        if restodiv_num_1 > 9:
            if organizar_cpf[9] == 0:
                os.system('cls')
            else:
                os.system('cls')
                print('CPF digitado inválido, digite novamente.\n')
        elif restodiv_num_1 <= 9:
            if organizar_cpf[9] == restodiv_num_1:
                os.system('cls')
            else:
                os.system('cls')
                print('CPF digitado inválido, digite novamente.\n')
        
        j = 11
        multi_num_2 = []
        for conta_multi_cpf_2 in organizar_cpf:
            conta_multi_cpf_2 *= j
            j -= 1
            multi_num_2.append(int(conta_multi_cpf_2))
            if j == 1:
                break

        soma_num_2 = 0
        for conta_soma_cpf_2 in multi_num_2:
            soma_num_2 += conta_soma_cpf_2

        multi10_num_2 = soma_num_2 * 10
        restodiv_num_2 = multi10_num_2 % 11

        if restodiv_num_2 > 9:
            if organizar_cpf[10] == 0:
                os.system('cls')
                print('CPF digitado válido.\n')
                break
            else:
                os.system('cls')
                print('CPF digitado inválido, digite novamente.\n')
        elif restodiv_num_1 <= 9:
            if organizar_cpf[10] == restodiv_num_2:
                os.system('cls')
                print('CPF digitado válido.\n')
                break
            else:
                os.system('cls')
                print('CPF digitado inválido, digite novamente.\n')