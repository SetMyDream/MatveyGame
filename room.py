import door


class Room:
    def __init__(self, doors: list[door], name: str, lem, death=False):
        self.doors = doors  # количество дверей учитывывая из которой вышел
        self.name = name  # название комнаты в котокрой персонаж (названия разные и весёлые)
        self.lem = lem  # яркость света в комноте (+  от этого зависит яркость экрана персонажа 1..10)
        self.death = death  # умрёт ли человек если войдёт в данную комнату

    def getDoors(self):
        return self.doors

    def printDoors(self):
        print('Перед тобой ' + str(len(self.doors)) + ' двери')
        for door in self.doors:
            print(door.name + ' дверь.')
            # print('Надпись на двери: ', door.desc)

    pass
