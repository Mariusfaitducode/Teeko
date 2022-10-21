from constante import *
import affichage


def clickcase(event, grid, tour, list_pos, cnv, cnv1, cnv2):

    if tour[0] < 8:
        ligne = int(event.y / (HEIGHT_TAB/NB_LINE))
        colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

        if grid[ligne][colonne] == '_':
            pion = pion_tour(tour[0])
            grid[ligne][colonne] = pion
            affichage.draw_piece(cnv, ligne, colonne, pion)

            if pion == 'x':
                cnv1.config(width=(3-int(tour[0]/2))*(COTE_CASE+LINE_WIDTH))
            else:
                cnv2.config(width=(3-int(tour[0]/2))*(COTE_CASE+LINE_WIDTH))

            if victoire(grid, tour[0]):
                print(f'Victoire, {pion_tour(tour[0])} ')
            else:
                tour[0] += 1

    elif not list_pos:

        ligne = int(event.y / (HEIGHT_TAB / NB_LINE))
        colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

        if grid[ligne][colonne] == pion_tour(tour[0]):

            list_pos.append((ligne, colonne))
            list_pos.append(show_case(ligne, colonne, grid, cnv))

    else:
        print("second")
        print(list_pos)

        ligne = int(event.y / (HEIGHT_TAB / NB_LINE))
        colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

        last_case = list_pos[0]
        list_case = list_pos[1]

        if (ligne, colonne) in list_case:

            move_the_piece(ligne, colonne, list_case, last_case, grid, tour, cnv)
            list_pos.clear()

        elif grid[ligne][colonne] == pion_tour(tour[0]):

            hide_case(list_case, cnv)
            list_pos.clear()
            list_pos.append((ligne, colonne))
            list_pos.append(show_case(ligne, colonne, grid, cnv))
            cnv.update()

        else:
            hide_case(list_case, cnv)
            list_pos.clear()




def move_the_piece(ligne, colonne, list_case, last_case, grid, tour, cnv):

    last_l, last_c = last_case

    list_case.remove((ligne, colonne))
    print("good_line")

    pion = pion_tour(tour[0])

    affichage.remove_piece(cnv, last_l, last_c)
    grid[last_l][last_c] = '_'

    affichage.draw_piece(cnv, ligne, colonne, pion)
    grid[ligne][colonne] = pion

    hide_case(list_case, cnv)

    if victoire(grid, tour[0]):
        print(f'Victoire, {pion_tour(tour[0])} ')
    else:
        tour[0] += 1


def show_case(l, c, grid, cnv):

    list_pos = []

    for i in range(-1, 2, 2):

        if 0 <= l + i < NB_LINE and grid[l + i][c] == '_':
            print("ok")
            affichage.draw_possible_case(cnv, l+i, c)
            list_pos.append((l+i, c))

        if 0 <= c + i < NB_COLUMN and grid[l][c + i] == '_':
            print("ok")
            affichage.draw_possible_case(cnv, l, c + i)
            list_pos.append((l, c+i))

    return list_pos


def hide_case(list_pos, cnv):

    for i in list_pos:

        l, c = i

        affichage.hide_possible_case(cnv, l, c)


def pion_tour(tour):

    if tour % 2 == 0:
        return 'x'
    else:
        return 'o'


def victoire(grid, tour):

    for i in range(0, NB_LINE):
        for z in range(0, NB_COLUMN-3):
            compte = 0
            for j in range(z, z+4):

                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for j in range(0, NB_COLUMN):
        for z in range(0, NB_LINE-3):
            compte = 0
            for i in range(z, z+4):
                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for z in range(0, NB_LINE-3):
        for y in range(0, NB_COLUMN-3):
            compte = 0
            for x in range(0, 4):
                l = z + x
                c = y + x
                if grid[l][c] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for y in range(NB_LINE-1, NB_LINE-3, -1):
        for z in range(0, 2):
            compte = 0
            for i in range(y, y-4, -1):
                j = y - i + z
                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True
