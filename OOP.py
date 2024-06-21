class Fclub:
    """Класс карточка футбольного клуба"""
    name = 'Juventus'
    ceo = 'Anneli'
    age = '185'

    def __new__(cls, *args, **kwargs):
        print("Делаем до создания обьекта класса")
        return super().__new__(cls)

    def __init__(self):
        self.name = "Default name"
        self.ceo = "Default ceo"
        self.age = "Default age"

    def __del__(self):
        print(f"Обьект {self} удален, c клубом {self.name}")

    def get_coach(self):
        return f"ceo {self.name} - {self.ceo}"

    def set_goalkeeper(self, name):
        self.namegoalkeeper = name.split()[0]
        self.surnamegoalkeeper = name.split()[1]


juve = Fclub()
print(juve)
juve.name = "Juventus"

