""" 
Файл access2.py (Python 3.X + 2.X)
Декораторы классов с объявлениями атрибутов Private и Public.
Управляют внешним доступом к атрибутам, хранящимся в экземпляре или 
унаследованным из его классов.
Private объявляет имена атрибутов, которые нельзя извлекать или присваивать
им значения за пределами декорируемого класса, а Public объявляет все имена,
к которым можно применять упомянутые действия.

Предостережение: в Python 3.X это работает только явно именованных 
атрибутов: в классах
нового стиля методы перезагрузки операций __X__, неявно запускаемых для
встроенных операций,
не вызывают ни __getattr__, ни __getattribute__. Чтобы перехватывать и 
делегировать выполнение
встроенных операций, необходимо добавить здесь методы __Х__.
"""
