"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof
import sys

class MyUser:
    def __init__(self, nickname, level, xp, mp):
        self.nickname = nickname
        self.level = level
        self.xp = xp
        self.mp = mp

class MyUserSlots:
    __slots__ = ('nickname', 'level', 'xp', 'mp')

    def __init__(self, nickname, level, xp, mp):
        self.nickname = nickname
        self.level = level
        self.xp = xp
        self.mp = mp


my_user = MyUser('lokasan','80','1350','470')
my_user_slots = MyUserSlots('lokasan','80','1350','470')
print(f'{my_user.__dict__} {asizeof.asizeof(my_user)}') # 368 занимаемая память
print(f'{my_user_slots.__slots__} {asizeof.asizeof(my_user_slots)}') # 168 занимаемая память

# атрибуты
print(f'nickname: {asizeof.asizeof(my_user.nickname)} level: {asizeof.asizeof(my_user.level)} xp: '
      f'{asizeof.asizeof(my_user.xp)} mp: {asizeof.asizeof(my_user.mp)}')
print(f'nickname: {asizeof.asizeof(my_user_slots.nickname)} level: {asizeof.asizeof(my_user_slots.level)} xp: '
      f'{asizeof.asizeof(my_user_slots.xp)} mp: {asizeof.asizeof(my_user_slots.mp)}')
# атрибуты занимают одинаковый объем памяти по 32 каждый
