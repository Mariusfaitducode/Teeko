from tkinter import *
from affichage import *
from game_rules import *


typeGame = NO_GAME

window = Tk()

window.title("Teeko")
window.geometry("1080x720")

cnv = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

cnv.pack()
cnv.place(x=TAB_GAP, y=TAB_GAP)
draw_grid(cnv)

cnv1 = Canvas(window, width=4*(COTE_CASE+LINE_WIDTH), height=COTE_CASE)
cnv2 = Canvas(window, width=4*(COTE_CASE+LINE_WIDTH), height=COTE_CASE)

cnv1.place(x=1.1 * TAB_GAP + WIDTH_TAB, y=2.5*TAB_GAP)
cnv2.place(x=1.1 * TAB_GAP + WIDTH_TAB, y=3.5*TAB_GAP)

draw_list_pieces(cnv1, cnv2)

grid = [['_' for x in range(NB_COLUMN)] for y in range(NB_LINE)]
tour = [0]

cnv.bind("<Button-1>", lambda event: first_clickcase(event, grid, tour, cnv, cnv1, cnv2))

# cnv.bind("<Button-1>", lambda event: click_case(event, grid, tour, cnv))
# cnv.bind("<Button-1>", click_case)

window.mainloop()
