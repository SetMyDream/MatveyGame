# import main
import room


class Personage:
    def __init__(self, location=None, poket=None, alive=True):
        if poket is None:
            poket = ['фонарь', 'отмычка', 'ручка']
        self.location = location
        self.poket = poket
        self.alive = alive

    pasxalki = 0

    def compose_item(self, words: list, i: int):
        item = ''
        for iva in range(i, len(words)):
            item += words[iva] + ' '
        return item[:-1]

    def poketdobav(self, command: str):
        words = command.split()
        item = ''
        for i in range(len(words)):
            if 'инвентарь' in words[i]:
                i1 = i + 1
                item = self.compose_item(words, i1)
                self.poket.append(item)
                return print('Предмет ', item, ' добавлен в ваш инвентарь')

    def poket_ybavit(self, command: str):
        words = command.split()
        for niin in range(len(words)):
            for i in range(len(words)):
                if 'инвентаря' in words[i]:
                    item = self.compose_item(words, i+1)
                    self.poket.remove(item)
                    return print('Предмет', item, 'удалён из вашего инвентаря')

    def get_room(self):
        return self.location

    def set_room(self, current_room: room):
        self.location = current_room

    def inventory(self):
        proc = 'У вас в корманах есть:'
        for i in range(len(self.poket)):
            proc += (str(self.poket[i]) + ', ')
            proc2 = proc[:-2]
        print(proc2)

    def kill(self):
        self.alive = False
