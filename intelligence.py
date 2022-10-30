from constante import *
import affichage
import game_rules as game
from player import *


def choix_case(grid, tour, cnv):

    max = -1000
    final_l = None
    final_c = None

    ordi = Player(grid, game.pion_tour(tour))
    adversaire = Player(grid, game.pion_tour(tour + 1))

    print(ordi.list_pieces)
    print(ordi.token, adversaire.token)

    choice_list = list_all_cases(grid, ordi)

    for coup_piece in choice_list:

        piece, list_coup = coup_piece

        for coup in list_coup:
            (l, c) = coup
            affichage.draw_possible_case(cnv, l, c, "blue")

            





def list_all_cases(grid, player):

    list = []

    for i in player.list_pieces:

        (l, c) = i

        list.append(((l,c), list_case(l, c, grid)))

    return list


def list_case(l, c, grid):

    list_pos = []
    for i in range(l-1, l+2):
        for j in range(c-1, c+2):

            if 0 <= i < NB_LINE and 0 <= j < NB_COLUMN and grid[i][j] == '_':
                list_pos.append((i, j))
    return list_pos












