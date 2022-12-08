from main import *
from tkinter import *
import time
import os

def game_graph():
    window = Tk()
    window.geometry('1400x800')
    window.resizable(False,False)
    window.title('Diamants')
    nb_player = menu(window)
    print(nb_player,' joueurs')
    list_player = start_game_graph(window,nb_player)
    for i in range (3) :
        for j in range (len(list_player)): # Remet tous les joueurs dans la partie
            list_player[j].in_game = True
        list_player = round_graph(window,list_player, i)
    window.mainloop()


def menu(window):
    win = Frame(window)
    win.pack(side="top", expand=True, fill="both")
    entry_player=Entry(win, width= 25)
    entry_player.insert(0,0)
    okvar = IntVar()

    def on_click(text,entry_player):
        entry_player.delete(0, END)
        entry_player.insert(0,text)
        return entry_player
    
    def confirm(entry_player):
        global nb_player
        nb_player = int(entry_player.get())
        if 2<nb_player<9 :
            okvar.set(1)

    global loadimage
    loadimage = PhotoImage(file="Start-Button.png")
    Label(win, text="Sélectionner le nombre de joueur :",font='Arial 14 bold').place(relx= 0.715,rely=0.3)

    start_button = Button(win, command = lambda : confirm(entry_player), cursor='hand2', image = loadimage)
    start_button.place(relx = 0.785, rely = 0.65)
    nb3_button = Button(win, text = '3', command = lambda : on_click(3,entry_player), cursor='hand2',font='Arial 11 bold', bg='gray65', height = 3, width = 4)
    nb3_button.place(relx = 0.75, rely = 0.4)
    nb4_button = Button(win, text = '4', command = lambda : on_click(4,entry_player), cursor='hand2',font='Arial 11 bold', bg='gray65', height = 3, width = 4)
    nb4_button.place(relx = 0.8, rely = 0.4)
    nb5_button = Button(win, text = '5', command = lambda : on_click(5,entry_player), cursor='hand2',font='Arial 11 bold', bg='gray65', height = 3, width = 4)
    nb5_button.place(relx = 0.85, rely = 0.4)
    nb6_button = Button(win, text = '6', command = lambda : on_click(6,entry_player), cursor='hand2',font='Arial 11 bold', bg='gray65', height = 3, width = 4)
    nb6_button.place(relx = 0.75, rely = 0.5)
    nb7_button = Button(win, text = '7', command = lambda : on_click(7,entry_player), cursor='hand2',font='Arial 11 bold', bg='gray65', height = 3, width = 4)
    nb7_button.place(relx = 0.8, rely = 0.5)
    nb8_button = Button(win, text = '8', command = lambda : on_click(8,entry_player), cursor='hand2',font='Arial 11 bold', bg='gray65', height = 3, width = 4)
    nb8_button.place(relx = 0.85, rely = 0.5)
    start_button.wait_variable(okvar)
    win.destroy()
    return nb_player


def start_game_graph(window,nb_player):
    name_win = Frame(window)
    name_win.pack(side="top", expand=True, fill="both")
    global list_player
    list_player = []
    verif_list = []
    okvar = IntVar()

    def check_list(list_player):
        for i in range(len(list_player)):
            if list_player[i] == '':
                return None
        okvar.set(1)

    def ad_name(i,entry,but) :
        temp_name = entry.get()[:8]
        if temp_name != '':
            list_player[i] = player(temp_name)
            but.destroy()

    for i in range(8):
        verif_list.append(False)

    for i in range (nb_player):
        Label(name_win,text = "Nom joueur " + str(i+1) + " :",font='Arial 20 bold').place(relx = 0.27, rely = 0.11*i+0.05)
        verif_list[i]=True
        list_player.append('')

    name0_entry = Entry(name_win,font='Arial 20')
    name0_entry.place(relx = 0.42, rely = 0.05)
    but0 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(0,name0_entry,but0), cursor='hand2')
    but0.place(relx = 0.65, rely = 0.05)
    name1_entry = Entry(name_win,font='Arial 20')
    name1_entry.place(relx = 0.42, rely = 0.11+0.05)
    but1 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(1,name1_entry,but1), cursor='hand2')
    but1.place(relx = 0.65, rely = 0.11+0.05)
    name2_entry = Entry(name_win,font='Arial 20')
    name2_entry.place(relx = 0.42, rely = 0.22+0.05)
    but2 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(2,name2_entry,but2), cursor='hand2')
    but2.place(relx = 0.65, rely = 0.22+0.05)
    
    if verif_list[3]:
        name3_entry = Entry(name_win,font='Arial 20')
        name3_entry.place(relx = 0.42, rely = 0.33+0.05)
        but3 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(3,name3_entry,but3), cursor='hand2')
        but3.place(relx = 0.65, rely = 0.33+0.05)
    if verif_list[4]:
        name4_entry = Entry(name_win,font='Arial 20')
        name4_entry.place(relx = 0.42, rely = 0.44+0.05)
        but4 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(4,name4_entry,but4), cursor='hand2')
        but4.place(relx = 0.65, rely = 0.44+0.05)
    if verif_list[5]:
        name5_entry = Entry(name_win,font='Arial 20')
        name5_entry.place(relx = 0.42, rely = 0.55+0.05)
        but5 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(5,name5_entry,but5), cursor='hand2')
        but5.place(relx = 0.65, rely = 0.55+0.05)
    if verif_list[6]:
        name6_entry = Entry(name_win,font='Arial 20')
        name6_entry.place(relx = 0.42, rely = 0.66+0.05)
        but6 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(6,name6_entry,but6), cursor='hand2')
        but6.place(relx = 0.65, rely = 0.66+0.05)
    if verif_list[7]:
        name7_entry = Entry(name_win,font='Arial 20')
        name7_entry.place(relx = 0.42, rely = 0.77+0.05)
        but7 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(7,name7_entry,but7), cursor='hand2')
        but7.place(relx = 0.65, rely = 0.77+0.05)
    
    launch_button = Button(name_win, text = "Commencer", font='Arial 15 bold',activebackground='green', command = lambda : check_list(list_player), cursor='hand2',height=2,width=12)
    launch_button.pack(side='bottom',pady=25)
    launch_button.wait_variable(okvar)
    name_win.destroy()
    return list_player


def round_graph(window,list_player, round):
    deck = create_deck()
    deck_shown = []
    end_round = False
    dis_win = Frame(window)
    dis_win.pack(side="top", expand=True, fill="both")
    dis_win.pack_propagate(False)
    player_win = Frame(window,bg='red')
    player_win.pack(side="top", expand=True, fill="both")
    while not end_round :
        if check_end(list_player) :
            end_round = True
        if not end_round :
            draw(deck, deck_shown, list_player)
        if trap_check(deck_shown) :
            end_round = True
            display_graph(dis_win,player_win,deck_shown, list_player, round)
            time.sleep(2)
        if not end_round :
            display_graph(dis_win,player_win,deck_shown, list_player, round)
            player_action_graph(player_win,deck_shown, list_player)
    dis_win.destroy()
    player_win.destroy()
    return list_player


def player_display(player_win,list_player,round,temp_total):
    Label(player_win, text = "Gemmes restantes : " + str(temp_total), font='Arial 12 bold').place(relx = 0.1, rely = 0.01)
    for i in range(len(list_player)):
        Label(player_win, text = list_player[i].name, font='Arial 16 bold').place(relx = 0.08 + i*0.12, rely = 0.5)
    player_win.update()


def display_graph(dis_win,player_win,deck_shown,list_player,round):
    temp_total = 0
    if deck_shown[-1].danger :
        print('DANGER',deck_shown[-1].type_danger)
        danger_graph = Label(dis_win, text = "DANGER "+str(deck_shown[-1].type_danger), font='Arial 12 bold')
        danger_graph.pack()
    elif deck_shown[-1].treasure :
        print('TRESOR')
        tresor_graph = Label(dis_win, text = "TRÉSOR", font='Arial 12 bold')
        tresor_graph.pack()
        temp_total += deck_shown[-1].nbr_gem
    elif deck_shown[-1].relic :
        print('RELIQUE')
        relic_graph = Label(dis_win, text = "RELIQUE", font='Arial 12 bold')
        relic_graph.pack()
    dis_win.update()
    print()
    print('Gemmes restantes :',temp_total)
    player_display(player_win,list_player,round,temp_total)
    print()
    for i in range (len(list_player)):
        if list_player[i].in_game :
            position = '(dans le temple)'
        else :
            position = '(au campement) '
        print('{:>15s}{:>19s}{:>11s}{:>21s}'.format(str(list_player[i].name),position+' :',str(list_player[i].temp_gem)+' gemmes',str(list_player[i].total_gem)+' gemmes stockées'))
    print()

def player_action_graph(window,deck_shown, list_player):
    time.sleep(1)

game_graph()