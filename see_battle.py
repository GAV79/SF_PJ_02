# класс Игры (Game)
# приветствие, запрос имени игрока
# создание "игрока" - экземпляр класса Доска (Board) и для ИИ
# установка кораблей (запрос и создание экземпляра класса Корабль(Ship))
# для ИИ расстановка происходит рандомно
# должны быть в итоге списки: с координатами кораблей игрока и ИИ, с координатами кораблей и соседних точек по кругу кораблей    
# класс Выстрелов(Shut): возращаем списки выстрелов игрока и ИИ
# условие окончания Игры (буду сверять входят ли элементы списка кораблей ИИ в список выстрелов Игрока и наоборот)
# описать исключения на всех этапах (функция принимающая сообщение об ошибке) и инициировать новую попытку

import random
import sys

class Game:
    def __init__(self):
        self.name  = input("    Ваше имя: ") # проверить введенное имя или разрешу любое
        self.board = Board()
        self.ship = Ship()
        self.play_ships = [] #корабли игрока
        self.intel_ships = []  # корабли ИИ
        self.near_play_ships = []  # окружение кораблей игрока
        self.near_intel_ships = []   # окружение кораблей ИИ
        self.error_place_play = []  # список с занятыми позициями при расстановке кораблей игрока
        self.error_place_intel = []  # список с занятыми позициями при расстановке кораблей ИИ
        self.in_1= ['11', '12', '13', '14', '15', '16',
        '21', '22', '23', '24', '25', '26',
        '31', '32', '33', '34', '35', '36',
        '41', '42', '43', '44', '45', '46',
        '51', '52', '53', '54', '55', '56',
        '61', '62', '63', '64', '65', '66']
        #  для 3х палубного горизонталь
        self.in_h_3 = ['11', '12', '13', '14',
        '21', '22', '23', '24',
        '31', '32', '33', '34',
        '41', '42', '43', '44',
        '51', '52', '53', '54',
        '61', '62', '63', '64']
        #  для 3х палубного вертикаль
        self.in_v_3 = ['11', '12', '13', '14', '15', '16',
        '21', '22', '23', '24', '25', '26',
        '31', '32', '33', '34', '35', '36',
        '41', '42', '43', '44', '45', '46']
        # для 2х палубного горизонталь
        self.in_h_2 = ['11', '12', '13', '14', '15',
        '21', '22', '23', '24', '25',
        '31', '32', '33', '34', '35',
        '41', '42', '43', '44', '45',
        '51', '52', '53', '54', '55',
        '61', '62', '63', '64', '65']
        # для 2х палубного вертикаль
        self.in_v_2 = ['11', '12', '13', '14', '15', '16',
        '21', '22', '23', '24', '25', '26',
        '31', '32', '33', '34', '35', '36',
        '41', '42', '43', '44', '45', '46',
        '51', '52', '53', '54', '55', '56']

        self.in_intel = self.in_1.copy()
        self.in_play = self.in_1.copy()


    def get_name(self):
        return self.name

    def get_board(self):
        return self.board

    def get_ship(self):
        return self.ship

    def get_error_place():
        return self.error_place_play

    def get_error_place():
        return self.error_place_intel

    def wellCome(self):
        n = Game.get_name(self)
        print()
        print(f'    {n}, начинаем игру "Морской бой"')
        print()
        print("    Расставь свои корабли")

    def messange_err(self):
        print()
        print("     попыток больше нет")
        print()
        print('       Игра окончена')
        sys.exit()
      

    def get_winner(self, player, list_ship):
        if len(list_ship) == 0:
            print(f'    {player} ПОБЕДИЛ!!!!!')
            sys.exit()
           
        else:
            pass

    def start(self):
        # начало игры
        # проверка , что выстрел игрока в пределах поля игры (ограничила 3мя попытками)

        q = 0
        while q <= 2:
            try:
                print()
                shut_play = input(" Ваш выстрел (RC, где R -номер строки; C - номер столбца (пример: 24)): ")
                if shut_play in self.in_intel:
                    break
                else:
                    raise Exception('    нет такой точки для выстрела')
            except Exception as e:
                if q == 2:
                    self.messange_err()
                else:
                    print()
                    print(e)
                    print()
                    q += 1

        if shut_play in self.intel_ships:
            print()
            print(f'  {self.name}: Попадание')
            self.intel_ships.remove(shut_play)  # удаляю точку из кораблей ИИ (использую как проверку победы)
            self.in_intel.remove(shut_play)  # удаляю из списка возможных точек выстрела по доске ИИ
            self.board.shut_ok(self.board.intel_board, shut_play)  # передаю на доску попадание
            self.get_winner(self.name, self.intel_ships)
        else:
            print()
            print(f'  {self.name}: Промах')
            self.in_intel.remove(shut_play)  # удаляю из списка возможных точек выстрела
            self.board.shut_break(self.board.intel_board, shut_play) # передаю на доску промах

        # выстрел ИИ
        shut_intel = random.choice(self.in_play)

        if shut_intel in self.play_ships:
            print()
            print('  ИИ: Попадание')
            self.play_ships.remove(shut_intel)  # удаляю точку из кораблей игрока (использую как проверку победы)
            self.in_play.remove(shut_intel)  # удаляю из списка возможных точек выстрела по доске игрока
            self.board.shut_ok(self.board.play_board, shut_intel)  # передаю на доску попадание
            self.get_winner('ИИ', self.play_ships)
        else:
            print()
            print('  ИИ: Промах')
            self.in_play.remove(shut_intel)  # удаляю из списка возможных точек выстрела
            self.board.shut_break(self.board.play_board, shut_intel) # передаю на доску промах


        # следующий выстрел
        self.start()
        
    def input_ship(self):
        print()
        print('    Формат: RC (R -номер строки; C - номер столбца (пример: 24)')
        print()
        for i in [3, 2, 2, 1, 1, 1]:
            # расстановка кораблей игрока
            # проверка расположения корабля(уместится ли на поле, не стоит ли рядом с другим кораблем)
            q = 0
            while q <= 2:
                try:
                    # проверка начальной координаты корабля
                    q1 = 0
                    while q1 <= 2:
                        try: 
                            XY = input(f'    Введите начальную координату {i}-палубного корабля: ')
                            
                            # проверка значения направления
                            q2 = 0
                            while q2 <= 2:
                                try:
                                    Z = input('    Укажите направление(0 - горизонталь, 1 - вертикаль): ')

                                    if Z == '0' or Z == '1':
                                        break
                                    else:
                                        raise Exception('    Некорректное значение направления')
                                except Exception as e2:
                                    if q2 == 2:
                                        self.messange_err()
                                    else:
                                        print()
                                        print(e2)
                                        print()
                                        q2 += 1

                            
                            if Z == '0':
                                if i == 3:
                                    self.choice_play = self.in_h_3.copy()
                                if i == 2:
                                    self.choice_play = self.in_h_2.copy()
                                if i == 1:
                                    self.choice_play = self.in_1.copy()
                            elif Z == '1':
                                if i == 3:
                                    self.choice_play = self.in_v_3.copy()
                                if i == 2:
                                    self.choice_play = self.in_v_2.copy()
                                if i == 1:
                                    self.choice_play = self.in_1.copy()

                            if XY in self.choice_play:
                                break
                            else:
                                raise Exception('    Некорректное значение начальной координаты')

                        except Exception as e1:
                            if q1 == 2:
                                self.messange_err()
                            else:
                                print()
                                print(e1)
                                print()
                                q1 += 1

                    self.ship.get_ship(i, Z, XY)

                    for j in self.ship.sh_p:
                        if j in self.near_play_ships:
                            raise Exception('    невозможно поставить корабль, попробуйте еще раз') 

                    for k in self.ship.sh_p:
                        self.play_ships.append(k)
                        self.ship.n.append(k)

                    self.ship.get_near(Z, self.ship.sh_p, self.ship.n, self.near_play_ships)

                    break

                except Exception as e:
                    if q == 2:
                        self.messange_err()
                    else:
                        print()
                        print(e)
                        print()
                        q += 1
                
            

            # расстановка кораблей ИИ
            p = 0
            while p <= 5:
                try:

                    Z1 = random.choice(['0', '1'])
                    if Z1 == '0':
                        if i == 3:
                            self.choice_intel = self.in_h_3.copy()

                        elif i == 2:
                            self.choice_intel = self.in_h_2.copy()
                            self.choice_intel = list(set(self.choice_intel).difference(set(self.near_intel_ships)))

                        elif i == 1:
                            self.choice_intel = self.in_1.copy()
                            self.choice_intel = list(set(self.choice_intel).difference(set(self.near_intel_ships)))                

                    elif Z1 == '1':
                        if i == 3:
                            self.choice_intel = self.in_v_3.copy()

                        elif i == 2:
                            self.choice_intel = self.in_v_2.copy()
                            self.choice_intel = list(set(self.choice_intel).difference(set(self.near_intel_ships)))

                        elif i == 1:
                            self.choice_intel = self.in_1.copy()
                            self.choice_intel = list(set(self.choice_intel).difference(set(self.near_intel_ships)))                

                    if self.choice_intel == []:
                        print('    ИИ не смог расставить корабли')
                        self.messange_err()
                    else:
                        X1Y1 = random.choice(self.choice_intel)
                        
                        self.ship.get_ship(i, Z1, X1Y1)

                        for j in self.ship.sh_p:
                            if j in self.near_intel_ships:
                                raise Exception('   ИИ не смог расставить корабли') 

                        for k in self.ship.sh_p:
                            self.intel_ships.append(k)
                            self.ship.n.append(k)

                        self.ship.get_near(Z1, self.ship.sh_p, self.ship.n, self.near_intel_ships)

                        break

                except Exception as e:
                    if p == 5:
                        print(e)
                        self.messange_err()
                    else:
                        p += 1
            
            # отрисовка полей игрока и ИИ
            self.board.visual_ship(self.near_play_ships, self.play_ships, self.near_intel_ships, self.intel_ships)


        self.near_play_ships = list(set(self.near_play_ships))
        self.near_intel_ships = list(set(self.near_intel_ships))


class Board:
    def __init__(self):
        
        self.play_board = [[' ', '1', '2', '3', '4', '5', '6'],
                           ['1', '.', '.', '.', '.', '.', '.'],
                           ['2', '.', '.', '.', '.', '.', '.'],
                           ['3', '.', '.', '.', '.', '.', '.'],
                           ['4', '.', '.', '.', '.', '.', '.'],
                           ['5', '.', '.', '.', '.', '.', '.'],
                           ['6', '.', '.', '.', '.', '.', '.']]
        
        self.intel_board = [[' ', '1', '2', '3', '4', '5', '6'],
                           ['1', '.', '.', '.', '.', '.', '.'],
                           ['2', '.', '.', '.', '.', '.', '.'],
                           ['3', '.', '.', '.', '.', '.', '.'],
                           ['4', '.', '.', '.', '.', '.', '.'],
                           ['5', '.', '.', '.', '.', '.', '.'],
                           ['6', '.', '.', '.', '.', '.', '.']]
    @staticmethod
    def print_name():
        print()
        print(f'  {game.get_name()}', end='')
        print('                 ', end='')
        print('ИИ')
        print()

    def print_board(self):
        for i in range(0, 7):
            print("|".join(self.play_board[i]), '  ',
                  "|".join(self.intel_board[i]))

    def visual_ship(self, near, ship, near_intel, intel):
        
        for i in near:
            x = int(i[0])
            y = int(i[1])
            self.play_board[x][y] = '-'

        for i in ship:
            x = int(i[0])
            y = int(i[1])
            self.play_board[x][y] = '▪'

        # если раскомментировать, то будет отображаться как ИИ расставляет корабли

        # for i in near_intel:
        #     x = int(i[0])
        #     y = int(i[1])
        #     self.intel_board[x][y] = '-'

        # for i in intel:
        #     x = int(i[0])
        #     y = int(i[1])
        #     self.intel_board[x][y] = '▪'
            
        self.print_name()
        self.print_board()
        print()

    def shut_ok(self, brd, point):
        x = int(point[0])
        y = int(point[1])
        brd[x][y] = 'X'

        self.print_name()
        self.print_board()
        print()

    def shut_break(self, brd, point):
        x = int(point[0])
        y = int(point[1])
        brd[x][y] = 'p'

        self.print_name()
        self.print_board()
        print()

class Ship:
    def __init__(self):
        self.sh_p = []
        self.n = []
        self.n_1 = []
        
    def get_ship_point(self):
        return self.sh_p

    def get_near(self):
        return self.n
    
    def get_ship(self, size, orient, xy):  
    # size - размер корабля
    # orient - 0(горизонталь) или 1(вертикаль)
    # xy - координаты начала корабля
    # list_ship - список координат кораблей или игрока или ИИ
    # list_near - список координат вокруг кораблей или игрока или ИИ

        self.size = size
        self.orient = orient
        self.xy = xy
        self.x = int(self.xy[0])
        self.y = int(self.xy[1])

        if self.orient == '0':
            self.sh_p = []
            self.n = []
            self.n_1 = []
            for i in range(self.size):
                j = str(self.x) + str(self.y + i)    
                self.sh_p.append(j) # вспомогательный список, корабль как список 
    

                    
        if self.orient == '1':
            self.sh_p = []
            self.n = []
            self.n_1 = []
            for i in range(self.size):
                j = str(self.x + i) + str(self.y)    
                self.sh_p.append(j)
                




    def get_near(self, orient, sh_p, n, list_near):

        self.orient = orient
        self.sh_p = sh_p
        self.n = n

        if self.orient == '0':

            for i in self.sh_p:
                j = int(i[1])
                self.n.append(i[0] + str(j - 1))
                if (j + 1) <= 6:
                    self.n.append(i[0] + str(j + 1))

            for i in self.n:
                j = int(i[0])
                self.n_1.append(str(j - 1) + i[1])
                if (j + 1) <= 6:
                    self.n_1.append(str(j + 1) + i[1])
            
            for i in self.n_1:
                self.n.append(i)

            index = []
            for k, i in enumerate(self.n):
                if '0' in i: 
                    index.append(k)
            if len(index) != 0:
                index.reverse()
                for k in index:
                    self.n.pop(k)

            self.n = list(set(self.n))

            for i in self.n:
                list_near.append(i)


                    
        if self.orient == '1':

            for i in self.sh_p:
                j = int(i[0])
                self.n.append(str(j - 1) + i[1])
                if (j + 1) <= 6:
                    self.n.append(str(j + 1) + i[1])
            for i in self.n:
                j = int(i[1])
                self.n_1.append(i[0] + str(j - 1))
                if (j + 1) <= 6:
                    self.n_1.append(i[0] + str(j + 1))

            for i in self.n_1:
                self.n.append(i)

            index = []
            for k, i in enumerate(self.n):
                if '0' in i: 
                    index.append(k)
            if len(index) != 0:
                index.reverse()
                for k in index:
                    self.n.pop(k)

            self.n = list(set(self.n))

            for i in self.n:
                list_near.append(i)


def want_game():
    print()
    print('     Игра "Морской бой"')
    print()
    print('     Обозначения:')
    print()
    print('     "." - свободная клетка')
    print()
    print('     "▪" - корабль или часть корабля')
    print()
    print('     "-" - на своем поле недоступные клетки для корабля')
    print()
    print('     "X" - попадание по кораблю или его части')
    print()
    print('     "p" - промах при стрельбе')
    print()
    
want_game()
game = Game()
game.wellCome()
Board.print_name()
Board.print_board(game.get_board())
game.input_ship()
game.start()
