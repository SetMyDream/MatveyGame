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
third_door = door.Door('Оголённые_провода')
fourth_door = door.Door('Змеи')
fifth_door = door.Door('Пауки')
sixth_door = door.Door('Гвозди')
seventh_door = door.Door('Вода')
eighth_door = door.Door('Лава')
ninth_door = door.Door('Цветы')

# Создаём комнаты
outdoor = room.Room([entrance], 'Улица', 10)
hostinnaya = room.Room([entrance, first_door, second_door, third_door], 'Гостиная', 8)
lava = room.Room([first_door, fourth_door, fifth_door, sixth_door], 'Лава', 9)
crocodile = room.Room([second_door], 'Крокодилы', 2, True)
provoda = room.Room([third_door], 'Оголённые_провода', 5, True)
zmei = room.Room([fourth_door], 'Змеи', 4, True)
pauki = room.Room([fifth_door, seventh_door, eighth_door, ninth_door], 'Пауки', 6)
gvzdi = room.Room([sixth_door], 'Гвозди', 6, True)
voda = room.Room([seventh_door], 'Вода', 5)
lavaa = room.Room([eighth_door], 'Лава', 9, True)
cvetu = room.Room([ninth_door], 'Цветы', 8, True)

# соединяем команты и двери
entrance.setRooms(outdoor, hostinnaya)
first_door.setRooms(hostinnaya, lava)
second_door.setRooms(hostinnaya, crocodile)
third_door.setRooms(hostinnaya, provoda)
fourth_door.setRooms(lava, zmei)
fifth_door.setRooms(lava, pauki)
sixth_door.setRooms(lava, gvzdi)
seventh_door.setRooms(pauki, voda)
eighth_door.setRooms(pauki, lavaa)
ninth_door.setRooms(pauki, cvetu)

#  создаём персонажа
player1 = personage.Personage()
player1.set_room(outdoor)

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


"""                                               Улица
                                                (Золото)
                                               Гостинная
                                        //          ||       \\
                                    (Лава)     (Крокодилы)  (Провода)
                                     Лава       Крокодилы    Провода
                                     ||      
                                    (Змеи)       (Пауки)       (Гвозди)
                                     Змеи         Пауки         Гвозди
                                                   ||
                                    (Вода)       (Лава)         (Цветы)
                                     Вода         Лава           Цветы
                                                   ||
                                    (Робот)      (Собака)        (Кот)
                                     Робот        Собака          Кот
                                                    ||
                                (Битое стекло)    (Конат)    (Супер липкий пол)                            
                                 Битое стекло      Конат      Супер липкий пол
                                                     ||
                                    (Яйца)         (Газ)        (Кислота)                   
                                     Яйца           Газ          Кислота        
                                      ||
                                                                   
                                                                   
                                                                   ||
                                                                   
                                                                   
                                                                   ||
                                                                   
                                                                   
                                                                   ||
"""
