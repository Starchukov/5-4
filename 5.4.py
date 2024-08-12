class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        #Название объекта добавлялось в список cls.houses_history
        #Название строения можно взять из args по индексу.
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    #В Python магический метод __new__ должен возвращать адрес нового
    # созданного объекта. Здесь функция super() возвращает ссылку на базовый
    # класс и через нее мы вызываем метод __new__ с одним первым аргументом.


Хорошо, давайте адрес нового объекта. Но откуда мы его возьмем? Для этого можно вызвать аналогичный метод базового класса и делается это, следующим образом:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)