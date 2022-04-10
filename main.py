import door
import initialization as init
import personage

def clearConsole():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def commands():
    print(init.comands)


def door_from_the_list(doors: list[door], command: str) -> list[door]:
    doors2 = []
    proc = command.split(' ')
    for ni in doors:
        for i in proc:
            door_name = ni.name.lower()
            if i == door_name:
                doors2.append(ni)
    if doors2 == []:
        print('Ошибка синтаксиса')
    return doors2

p1 = 0

if __name__ == '__main__':
    name_of_player, pol_of_player = init.initialization()
    if len(pol_of_player) == 0:
        init.history += f' Легендарное золотоискательное тело под именем {name_of_player}'
    elif pol_of_player.lower()[0] == 'ж':
        init.history += f' Легендарная золотоискательница {name_of_player}'
    elif pol_of_player.lower()[0] == 'м':
        init.history += f' Легендарный золотоискатель {name_of_player}'
    else:
        init.history += f' Легендарное золотоискательное тело под именем {name_of_player}'
    print(init.history)
    input("Нажмите Enter чтобы продолжыть:").lower()
    clearConsole()
    commands()

    while True:
        command = input("Ваш ход:").lower()
        if 'двер' in command:
            init.player1.get_room().printDoors()

        if 'команд' in command:
            commands()

        if ('войти в ' in command):
            doors2enter = door_from_the_list(init.player1.get_room().doors, command)
            if (len(doors2enter) != 0):
                door2enter = doors2enter[0]
                init.player1.set_room(door2enter.enter(init.player1))
            else:
                print("Прости, не понял куда идти")

        if 'выйти' in command:
            print('Прогрес сохранён')
            break

        if ('положение' in command or 'где я' in command):
            print('Вы находитесь в комнате', init.player1.get_room().name)

        if ('инвент' in command):
            init.player1.inventory()

        if ('чбнорвт' in command):
            if p1 == 0:
                p1 += 1
                personage.Personage.pasxalki += 1
                print('Ты нашёл пасхалку')

        if ('пмн' in command):  # найденые мною масхалки
            if personage.Personage.pasxalki == 0:
                print('Ты нашёл 0 пасхалок')
            elif personage.Personage.pasxalki == 1:
                print('Ты нашёл 1 пасхалку')
            elif personage.Personage.pasxalki < 5:
                print('Ты нашёл ', personage.Personage.pasxalki, ' пасхалки')
            else:
                print('Ты нашёл ', personage.Personage.pasxalki, ' пасхалок')  # максимум 20 пасхалок
