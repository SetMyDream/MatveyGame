import door
import initialization as init


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


if __name__ == '__main__':
    name_of_player, pol_of_player = init.initialization()
    if len(pol_of_player) == 0:
        init.history += f' Легендарное золотоискательное тело под именем {name_of_player}'
    elif pol_of_player.lower()[0] == 'ж':
        init.history += f' Легендарная золотоискательница {name_of_player}'
    elif pol_of_player.lower()[0] == 'м':
        init.history += f' Легендарный золотоискатель {name_of_player}'
    else: init.history += f' Легендарное золотоискательное тело под именем {name_of_player}'
    print(init.history)
    input("Нажмите Enter чтобы продолжыть:").lower()
    clearConsole()
    commands()




    # Текущее положение игрока
    currentRoom = init.outdoor

    while True:
        command = input("Ваш ход:").lower()
        if 'двер' in command:
            currentRoom.printDoors()
        # for dorr in currentRoom.getDoors():
        #     if str(dorr.name) in command:
        #         print('You entered door name')
        #         currentRoom = dorr.enter()
        if 'команд' in command:
            commands()
        if ('войти в ' in command):
            doors2enter = door_from_the_list(currentRoom.doors, command)
            if (len(doors2enter) != 0):
                door2enter = doors2enter[0]
                currentRoom = door2enter.enter(init.player1)
            else:
                print("Прости, не понял куда идти")
        if 'выйти' in command:
            print('Прогрес сохранён')
            break
        if ('положение' in command or 'где я' in command):
            print('Вы находитесь в комнате', currentRoom.name)
        if ('инвент' in command):
            init.player1.inventory()