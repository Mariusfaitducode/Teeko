from constante import *
import affichage


def first_clickcase(event, grid, tour, cnv, cnv1, cnv2):

    if tour[0]<8:
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

            tour[0] += 1




def pion_tour(tour):

    if tour % 2 == 0:
        return 'x'
    else:
        return 'o'