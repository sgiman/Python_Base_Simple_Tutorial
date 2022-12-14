# coding=utf-8
# *******************************************************************
# 020 - Декораторы
# Gosha Dudar, 2017
# *******************************************************************
# Writing sgiman, 2017
# Last Modification, 2022, aug
# -------------------------------------------------------------------
# Декоратор это "обертка" функции до выполнения и после выполенения
#

def decorator(func):
    def wrapper():
        print("Код до выпонения функции")
        func()
        print("Код, который сработал после функции")

    return wrapper


def test(func):
    def wrapper():
        print("Код до выполнения функции 2")
        func()
        print("Код, который сработал после функции 2")

    return wrapper


@decorator
@test
def show():
    print("Я обычная функция")


show()

# dec = decorator (show)
# dec ()
