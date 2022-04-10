class Personage:
    def __init__(self, location: str, poket: list):
        self.location = location
        self.poket = poket


    def inventory(self):
        proc = 'У вас в корманах есть:'
        for i in range(len(self.poket)):
            proc += self.poket[i] + ', '
            proc2 = proc[:-2]
        print(proc2)