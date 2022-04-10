import room


class Personage:
    def __init__(self, location=None, poket=None, pasxalki=0):
        if poket is None:
            poket = ['фонарь', 'отмычка', 'ручка', 'ключ от двери лава']
        self.location = location
        self.poket = poket
        self.pasxalki = pasxalki

    pasxalki = 0

    def get_room(self):
        return self.location

    def set_room(self, current_room: room):
        self.location = current_room

    def inventory(self):
        proc = 'У вас в корманах есть:'
        for i in range(len(self.poket)):
            proc += self.poket[i] + ', '
            proc2 = proc[:-2]
        print(proc2)

    def clear_inventory(self):
        self.__init__()
