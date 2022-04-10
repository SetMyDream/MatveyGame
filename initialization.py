import main
import door
import room
import personage

### Список команд
comands = ('Список команд игрока благодоря которым вы сможыте играть\n'
          'ВОЙТИ В (название двери) - вы войдёте в дверь и окажитесь в другой комнате\n'
          'СПИСОК КОМАНД ИГРОКА - выводит команды которыми может пользывыватьца игрок\n'
          'ГДЕ  Я , МОЁ МЕСТОПОЛОЖЕНИЕ - говорит где находится игрок\n'
          'ВЫЙТИ ИЗ ИГРЫ И СОХРАНИТЬ ПРОГРЕС - сохранение прогреса\n'
          'ДВЕРЬ ПЕРЕДОМНОЙ - говорит какая дверь перед игроком\n'
          'ЧТО У МЕНЯ В ИНВЕНТАРЕ - говорит что у вас в карманах\n')

# создаём двери
entrance = door.Door('Золото')
first_door = door.Door('Лава', key=True)
second_door = door.Door('Крокодилы')

# Создаём комнаты
outdoor = room.Room([entrance], 'Улица', 3)
hostinnaya = room.Room([entrance, first_door, second_door], 'Гостиная', 8)
lava = room.Room([first_door], 'Лава', 6) #+++++++++++++++++++
crocodile = room.Room([second_door], 'Кракодилы', 2, True)


# соединяем команты и двери
entrance.setRooms(outdoor, hostinnaya)
first_door.setRooms(hostinnaya, lava)
second_door.setRooms(hostinnaya, crocodile)

#  создаём персонажа
player1 = personage.Personage(outdoor, ['фонарь', 'отмычка', 'ручка', 'ключ от двери лава'])



history = ('    На мир снова нахлынула золотая лихорадка.\n '
           'В местных газетаах написали, что в лесу который\n'
           ' возле вашего города есть неплохие залижи золота\n'
           ' и многие в том числе вы отправлись искать.\n'
           ' Искавшизолото вы зашли в глухую часть леса где\n'
           ' никого нет! Сначала вы радовывались что канкурентов\n'
           ' нет но потом когда стала наступать начь стало\n'
           ' становится страшно и вы стали понимать что надо\n'
           ' найти какоето поваленое бревно чтобы под него лечь\n'
           ' но вы нашли гараздо лучше и это был недавно\n'
           ' пастроеный замок на двери было написано золото.\n'
           ' Вы уже стали предстовлять заголовки в газете.\n')


def initialization():
    name_of_player = input("Введите ваше имя:")
    pol_of_player = input("Введите ваше пол м или ж:")
    main.clearConsole()
    return [name_of_player, pol_of_player]
    # pol_of_player = input("Введите ваше пол м - мужской, ж - женский или д - другой:")


"""                                             Улица
                                               (Золото)
                                               Гостинная
                                        //          ||       \\
                                    (Лава)     (Крокодилы)  (Провода)
                                     Лава       Крокодилы    Провода
                                     
"""