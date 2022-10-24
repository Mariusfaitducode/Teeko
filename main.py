from tkinter import *
from affichage import *
from game_rules import *
import button


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


button_ami = Button(text="Contre un ami", font='Helvetica 15 bold', background='light gray',
                    command=(lambda:button.toggle_ami(button_ami, button_ordi, typeGame, cnv_text)))

button_ami.place(x=1.7 * TAB_GAP + WIDTH_TAB, y=1.7 * TAB_GAP)

button_ordi = Button(text="Contre l'ordi", font='Helvetica 15 bold', background='light gray',
                     command=(lambda:button.toggle_ordi(button_ami, button_ordi, typeGame, cnv_text)))

button_ordi.place(x=3.5 * TAB_GAP + WIDTH_TAB, y=1.7 * TAB_GAP)

button_reset = Button(window, text="reset", font='Helvetica 15 bold', background='light gray',
                      command=(lambda: button.reset_grid(cnv, grid, tour, typeGame, button_ami, button_ordi, cnv_text)))

button_reset.place(x=1.7 * TAB_GAP + WIDTH_TAB, y=5 * TAB_GAP)


cnv_text = Canvas(window, width=4 * COTE_CASE, height=0.8*COTE_CASE)
cnv_text.pack()
cnv_text.place(x=1.5 * TAB_GAP + WIDTH_TAB, y=0.7*TAB_GAP)

cnv_text.create_text(COTE_CASE * 2, COTE_CASE / 2, text="Select a game mode :",
                     fill="black", font='Helvetica 20 bold')


draw_list_pieces(cnv1, cnv2)

grid = [['_' for x in range(NB_COLUMN)] for y in range(NB_LINE)]
tour = [0]
list_pos = []
typeGame = [NO_GAME]

#list_pos.

cnv.bind("<Button-1>", lambda event: clickcase(event, grid, tour, list_pos, cnv, cnv1, cnv2))
# cnv.bind("<Button-1>", lambda event: second_clickcase(event, grid, tour, cnv))

# cnv.bind("<Button-1>", lambda event: click_case(event, grid, tour, cnv))
# cnv.bind("<Button-1>", click_case)

window.mainloop()
