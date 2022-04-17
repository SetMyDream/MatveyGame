# import personage
import room


class Door:
    rooms = []

    def __init__(self, name: str, key=False):
        self.name = name  # табличка на которой наптсано что находится за дверью
        self.key = key  # нужен ли ключ чтобы открыть двель если да то дверь одна и ключ надо найти если ключ не нужен то дверей будет несколько
        # self.desc = desc  # история как появилась комната (история будет невсегда)

    def setRooms(self, firstRoom: room, secondRoom: room):
        self.rooms = [firstRoom, secondRoom]

    def getRoom(self):
        return self.rooms[1]

    def switch_rooms(self, text):
        print(text)
        self.rooms = [self.rooms[1], self.rooms[0]]

    def transition_to_the_room(self, pers):
        if self.rooms[1].death == True:
            self.switch_rooms('Вы умерли') # to be continue
            pers.kill()
            return self.rooms[0]
        else:
            self.switch_rooms(f'Вы перешли в комнату {self.getRoom().name}')
            return self.rooms[0]

    # # @later
    def enter(self, pers):
        if self.key:
            for i in pers.poket:
                inin = i.lower().split()
                if ('ключ' in inin):
                    if inin[3].lower() == self.name.lower():
                        return self.transition_to_the_room(pers)
            print('Эту дверь не так легко открыть к ней нужен ключ')
            return self.rooms[0]
        else:
            return self.transition_to_the_room(pers)
