# python validate_tester2.py validate_descriptors1
"""
Вариант 2: проверка достоверности с помощь состояния 
для каждого экземпляра клиентского класса 
"""
from __future__ import print_function
from validate_tester import loadclass

CardHolder = loadclass()
bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')   # addr отличается:
# клиентские данные
print('bob:', bob.name, bob.acct, bob.age, bob.addr)
sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
print('sue:', sue.name, sue.acct, sue.age, sue.addr)

print("bob:", bob.name, bob.acct, bob.age, bob.addr)    # name, acct, age
                                                        # переписываются?
