import os
import random
import sys

while True:
    cpf_gerado = []
    for i in range(9):
        cpf_gerado.append(random.randint(0, 9))

    verificar_cpf_repetido = []
    for verificador in cpf_gerado:
        verificar_cpf_repetido.append(cpf_gerado[0])

    if cpf_gerado == verificar_cpf_repetido:
        continue
    
    i = 10
    multi_num_1 = []
    for conta_multi_cpf_1 in cpf_gerado:
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
        os.system('cls')
        cpf_gerado.append(0)
    elif restodiv_num_1 <= 9:
        os.system('cls')
        cpf_gerado.append(restodiv_num_1)
            
    j = 11
    multi_num_2 = []
    for conta_multi_cpf_2 in cpf_gerado:
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
        os.system('cls')
        cpf_gerado.append(0)
    elif restodiv_num_1 <= 9:
        os.system('cls')
        cpf_gerado.append(restodiv_num_2)

    cpf_formatado = f'{cpf_gerado[0]}{cpf_gerado[1]}{cpf_gerado[2]}'\
    f'.{cpf_gerado[3]}{cpf_gerado[4]}{cpf_gerado[5]}'\
    f'.{cpf_gerado[6]}{cpf_gerado[7]}{cpf_gerado[8]}'\
    f'-{cpf_gerado[9]}{cpf_gerado[10]}'
    print(f'CPF Gerado: {cpf_formatado}')
    sys.exit()