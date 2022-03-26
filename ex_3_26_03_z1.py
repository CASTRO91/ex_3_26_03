from random import randint


def card_number(number):
    if len(str(number)) == 16:
        print('original number:', str(number)[:4], str(number)[4:8], str(number)[8:12], str(number)[12:16])
        print('modified number:', '****', '****', '****', str(number)[12:16])
    else:
        print('wrong data')


for i in range(10):
    card_number(randint(10 ** 15, 10 ** 16 - 1))
