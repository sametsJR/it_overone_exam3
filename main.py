# 1. Функция скрывающая номер карточки
def card_hide(card):
    return '*' * (len(card)-4) + card[-4:]

print(card_hide("1111222233334444"))

# 2. Проверка, является ли слово палиндромом

def palindrome(s):
    rev = ''.join(reversed(s))

    if (s == rev):
        return ("Палиндром")
    else:
        return ("Не палиндром")

s = input("Введите слово: ")
ans = palindrome(s)
print(ans)

# 3. Задача про томаты. Признаюсь, решение я нагуглил :(

class Tomato:

    # Стадии созревания помидора
    states = {0: 'Зерно', 1: 'Цветок', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Помидорка {self._index} {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num-1)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник закончил')

    # Собираем урожай
    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Садовник закончил')
        else:
            print('Слишком рано. Растение еще не созрело')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''В идеале время сбора урожая помидоров должно наступить.
когда плод зрелый зеленый и
затем позволили созреть лозе.
Это предотвращает расслоение и синяки.
и позволяет в определенной мере контролировать процесс созревания''')


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Alex', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()