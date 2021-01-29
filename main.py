# UPDATE 1.3! Update codename: args version
import sys
from random import randrange
# update 1.1 colorama +
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
import sys

user_num = sys.argv[1]

limit_int = 100000

result = randrange(int(user_num))

def limit():
	if result >= 100000:
		Question = input("Число больше " + str(limit_int) + ", вы точно хотите его показать?(Да, Нет)")
		if Question == 'Да' or 'да' or 'Yes' or 'y' or 'yes':
			print(Back.BLUE + "Рандомное число:" + str(result) + ".")
		
		else:
			print("Принято, нажмите enter,и программа закроется.")
			input("Press enter")
	elif result <= 100000:
		print(Back.BLUE + "Рандомное число:" + str(result) + ".")
	else:
		print(Back.RED + "Ошибка! Напишите это на странице проекта на github и добавьте скришот.")

limit()

# creators: Dibusure, Open Source Present chat. Gonate didn't want to, which is a pity ...
# T
#  H
#	 A
#	   N
#	    K
#	     S
#		   !
