# 1.1 UPDATE name: Green numbers is beatiful!
import sys
from random import randrange
# как мы, программисты любим, колорама! Ловите!
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
user_num = input(Back.GREEN + "Ограничьте подбор до целого числа, это число:")
result = randrange(int(user_num))
print(Back.BLUE + "Рандомное число:" + str(result) + "." + Back.BLUE)
