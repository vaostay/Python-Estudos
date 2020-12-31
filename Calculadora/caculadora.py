#! /usr/bin/python3
#CODED BY: GRUPO DO ZAP
import time
import math
import os

print('''
  ____      _            _       _
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | (__| |_| | | (_| | || (_) | |
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|

''')
num = int(input('\033[1;32mDigite um número:\033[m '))
num2 = int(input('\033[1;32mDigite mais um número:\033[m '))
opcao = 0

while opcao != 6:
	os.system('clear')
	print('''\033[1;36m
	  ____      _            _       _
	 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
	| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
	| |__| (_| | | (__| |_| | | (_| | || (_) | |
 	 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|

\033[m''')

	print('''\033[1;37m
	Escolha uma função:

   	[1] Somar
   	[2] Multiplicar
   	[3] Maior ou menor
   	[4] Novos números
	[5] Divisão
   	[6] Sair do programa
	\033[m''')
	opcao = int(input('\n>>> Escolha uma das opções: '))

	if opcao == 1:
		result = num + num2
		print('\n\033[1;34mA soma do número {} e o número {} é igual a {}\033[m'.format(num, num2, result))
		time.sleep(5)
		os.system('clear')

	elif opcao == 2:
		result = num * num2
		print('\n\033[1;34mMultiplicando o valor {} e o valor {} o resultado é igual a {}'.format(num, num2, result))
		time.sleep(5)
		os.system('clear')

	elif opcao == 3:
		if num > num2:
			print('\n\033[1;34m{} é maior do que {}\033[m'.format(num, num2))
			time.sleep(5)
			os.system('clear')
		else:
			print('\n\033[1;34m{} é menor do que {}\033[m'.format(num, num2))
			time.sleep(5)
			os.system('clear')
	elif opcao == 4:
		num = int(input('\n\033[1;32mDigite um novo número:\033[m '))
		num2 = int(input('\n\033[1;32mDigite outro número:\033[m '))
		print('\n\033[7mVALINDANDO........\033[m')
		time.sleep(3)

	elif opcao == 5:
		result = num / num2
		print('\n\033[1;34mO resultado da divisão é {:.2f}'.format(result))
		time.sleep(5)
		os.system('clear')

	elif opcao == 6:
		print('\n\033[7mFINALIZANDO.....\033[m')
		time.sleep(1)
		print('\n\033[1;37mGoodbye Friend\033[m')
		exit()
	else:
		print('\n\033[1;31mOpção Inválida\033[m')
		time.sleep(2)
