print('=' * 10, 'BANCO PH', '=' * 10)
nota1 = 100
count = 0
valor = int(input('Digite o valor de saque: '))
while True:
    if valor >= nota1:  # AQUI É A LOGICA ENQUANTO O VALOR DO SAQUE FOR MAIOR QUE A MAIOR NOTA  #
        valor -= nota1  # AQUI RETIRAR CASO O VALOR DENTRO DO LOOPING CONTINUE SENDO MAIOR  #
        count += 1      # AQUI SERA CONTABILIZADO QUANTAS NOTAS DE MAIOR VALOR FORAM RETIRADAS #
    else:
        print(f'Emitido {count} notas de R$:{nota1}')
        if nota1 == 100:
            nota1 = 50  # SE A NOTA FOR MAIOR QUE O VALOR RESTANTE A NOTA SERÁ SUBSTITUIDA POR UM VALOR MENOR #
        elif nota1 == 50:
            nota1 = 20
        elif nota1 == 20:
            nota1 = 10
        elif nota1 == 10:
            nota1 = 5
        elif nota1 == 5:
            nota1 = 1
        count = 0  # AQUI SERÁ CONTABILIZADO AS NOVAS NOTAS DE VALOR MENOR #
        if valor == 0:
            break  # CASO O VALOR RESTANTE SEJA IGUAL A ZERO O LOOPING IRÁ PARAR DANDO FIM A OPERACAO #
print('Fim da Operação Volte Sempre!')
