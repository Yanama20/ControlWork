class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}.")

    def is_adult(self):
        if self.age >= 18:
            return print(True)
        else:
            return print(False)

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"


willy = Person('Вилли Вонка', 35, 'Лондон')
willy.introduce()

charlie = Person('Чарли', 13, 'Лондон')
magnus = Person('Магнус', 22, 'Берлин')
sergey = Person('Сергей', 16, 'Санкт-Петербург')

charlie.introduce()
magnus.introduce()
sergey.introduce()

carol = Person('Кэрол', 46, 'Нью-Йорк')
print(carol)