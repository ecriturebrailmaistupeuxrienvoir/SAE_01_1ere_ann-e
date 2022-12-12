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
    for i in range (5) :
        for j in range (len(list_player)): # Remet tous les joueurs dans la partie
            list_player[j].in_game = True
            list_player[j].temp_gem = 0
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
    loadimage = PhotoImage(file="images/Start-Button.png")
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
    name0_entry.insert(0,'joueur 1')
    name0_entry.place(relx = 0.42, rely = 0.05)
    but0 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(0,name0_entry,but0), cursor='hand2')
    but0.place(relx = 0.65, rely = 0.05)
    name1_entry = Entry(name_win,font='Arial 20')
    name1_entry.insert(0,'joueur 2')
    name1_entry.place(relx = 0.42, rely = 0.11+0.05)
    but1 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(1,name1_entry,but1), cursor='hand2')
    but1.place(relx = 0.65, rely = 0.11+0.05)
    name2_entry = Entry(name_win,font='Arial 20')
    name2_entry.insert(3,'joueur 3')
    name2_entry.place(relx = 0.42, rely = 0.22+0.05)
    but2 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(2,name2_entry,but2), cursor='hand2')
    but2.place(relx = 0.65, rely = 0.22+0.05)
    
    if verif_list[3]:
        name3_entry = Entry(name_win,font='Arial 20')
        name3_entry.insert(0,'joueur 4')
        name3_entry.place(relx = 0.42, rely = 0.33+0.05)
        but3 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(3,name3_entry,but3), cursor='hand2')
        but3.place(relx = 0.65, rely = 0.33+0.05)
    if verif_list[4]:
        name4_entry = Entry(name_win,font='Arial 20')
        name4_entry.insert(0,'joueur 5')
        name4_entry.place(relx = 0.42, rely = 0.44+0.05)
        but4 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(4,name4_entry,but4), cursor='hand2')
        but4.place(relx = 0.65, rely = 0.44+0.05)
    if verif_list[5]:
        name5_entry = Entry(name_win,font='Arial 20')
        name5_entry.insert(0,'joueur 6')
        name5_entry.place(relx = 0.42, rely = 0.55+0.05)
        but5 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(5,name5_entry,but5), cursor='hand2')
        but5.place(relx = 0.65, rely = 0.55+0.05)
    if verif_list[6]:
        name6_entry = Entry(name_win,font='Arial 20')
        name6_entry.insert(0,'joueur 7')
        name6_entry.place(relx = 0.42, rely = 0.66+0.05)
        but6 = Button(name_win,text = "Confirmer", font='Arial 14',command = lambda : ad_name(6,name6_entry,but6), cursor='hand2')
        but6.place(relx = 0.65, rely = 0.66+0.05)
    if verif_list[7]:
        name7_entry = Entry(name_win,font='Arial 20')
        name7_entry.insert(0,'joueur 8')
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
    dis_win.grid_propagate(False)
    player_win = Frame(window)
    player_win.pack(side="top", expand=True, fill="both")
    init_player_graph(player_win,list_player,round)
    while not end_round :
        if check_end(list_player) :
            end_round = True
        if not end_round :
            draw(deck, deck_shown, list_player)
        if trap_check(deck_shown) :
            end_round = True
            display_graph(dis_win,player_win,deck_shown, list_player)
            time.sleep(2)
        if not end_round :
            display_graph(dis_win,player_win,deck_shown, list_player)
            deck_shown, list_player = player_action_graph(player_win,deck_shown, list_player)
    dis_win.destroy()
    player_win.destroy()
    return list_player


def init_player_graph(player_win,list_player,round):
    Label(player_win, text = "Manche : " + str(round+1), font='Arial 12 bold').place(relx = 0.1, rely = 0.01)
    for i in range(len(list_player)):
        Label(player_win, text = list_player[i].name, font='Arial 16 bold').place(relx = 0.04 + i*0.12, rely = 0.25)


def player_display(player_win,list_player,temp_total):
    Label(player_win, text = "Gemmes restantes : " + str(temp_total), font='Arial 12 bold').place(relx = 0.3, rely = 0.01)
    for i in range(len(list_player)):
        Label(player_win, text = list_player[i].name, font='Arial 16 bold').place(relx = 0.04 + i*0.12, rely = 0.25)
        if list_player[i].in_game :
            Label(player_win,text = "en jeu", font='Arial 14 bold', fg = "blue").place(relx = 0.04 + i*0.12, rely = 0.35)
        else :
            Label(player_win,text = "au camp", font='Arial 14 bold', fg = "blue").place(relx = 0.04 + i*0.12, rely = 0.35)
        Label(player_win,text = str(list_player[i].temp_gem) + " gemmes", font='Arial 14 bold').place(relx = 0.04 + i*0.12, rely = 0.50)
        Label(player_win,text = str(list_player[i].total_gem) + " gemmes", font='Arial 14 bold').place(relx = 0.04 + i*0.12, rely = 0.58)
        Label(player_win,text = "stockées", font='Arial 14 bold').place(relx = 0.05 + i*0.12, rely = 0.64)
    player_win.update()


def display_graph(dis_win,player_win,deck_shown,list_player):
    temp_total = 0
    for i in range (len(deck_shown)):
        if deck_shown[i].treasure :
            temp_total += deck_shown[i].nbr_gem
    if len(deck_shown) < 16:
        Label(dis_win, image = deck_shown[-1].img).grid(row = 0, column = len(deck_shown), sticky = N, padx = 10, pady= 15)
    else :
        Label(dis_win, image = deck_shown[-1].img).grid(row = 1, column = len(deck_shown) - 15, sticky = N, padx = 10, pady= 15)
    dis_win.update()
    player_display(player_win,list_player,temp_total)

def player_action_graph(player_win, deck_shown, list_player):
    okvar = IntVar()
    player_out = []
    temp_total = 0
    temp_relic = []
    cpt = []
    ver = 0
    for i in range (len(list_player)):
        if list_player[i].in_game :
            ver += 1

    def set_state(player, butr, buts, state, cpt, i, player_out):
        player.in_game = state
        butr.destroy()
        buts.destroy()
        cpt.append(i)
        if state == sortir :
            player_out.append(i)
    
    def set_ok(cpt,ver):
        if len(cpt) == ver :
            okvar.set(1)

    rester = True
    sortir = False

    bt_stay_0 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[0], bt_stay_0, bt_quit_0, rester, cpt, 0, player_out), cursor='hand2')
    bt_quit_0 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[0], bt_stay_0, bt_quit_0, sortir, cpt, 0, player_out), cursor='hand2')
    bt_stay_1 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[1], bt_stay_1, bt_quit_1, rester, cpt, 1, player_out), cursor='hand2')
    bt_quit_1 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[1], bt_stay_1, bt_quit_1, sortir, cpt, 1, player_out), cursor='hand2')
    bt_stay_2 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[2], bt_stay_2, bt_quit_2, rester, cpt, 2, player_out), cursor='hand2')
    bt_quit_2 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[2], bt_stay_2, bt_quit_2, sortir, cpt, 2, player_out), cursor='hand2')
    bt_stay_3 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[3], bt_stay_3, bt_quit_3, rester, cpt, 3, player_out), cursor='hand2')
    bt_quit_3 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[3], bt_stay_3, bt_quit_3, sortir, cpt, 3, player_out), cursor='hand2')
    bt_stay_4 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[4], bt_stay_4, bt_quit_4, rester, cpt, 4, player_out), cursor='hand2')
    bt_quit_4 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[4], bt_stay_4, bt_quit_4, sortir, cpt, 4, player_out), cursor='hand2')
    bt_stay_5 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[5], bt_stay_5, bt_quit_5, rester, cpt, 5, player_out), cursor='hand2')
    bt_quit_5 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[5], bt_stay_5, bt_quit_5, sortir, cpt, 5, player_out), cursor='hand2')
    bt_stay_6 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[6], bt_stay_6, bt_quit_6, rester, cpt, 6, player_out), cursor='hand2')
    bt_quit_6 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[6], bt_stay_6, bt_quit_6, sortir, cpt, 6, player_out), cursor='hand2')
    bt_stay_7 = Button(player_win, text = "Rester", font='Arial 12', command = lambda: set_state(list_player[7], bt_stay_7, bt_quit_7, rester, cpt, 7, player_out), cursor='hand2')
    bt_quit_7 = Button(player_win, text = "Sortir", command = lambda: set_state(list_player[7], bt_stay_7, bt_quit_7, sortir, cpt, 7, player_out), cursor='hand2')

    bt_ok = Button(player_win, text = "Continuer", command = lambda: set_ok(cpt,ver), cursor='hand2')
    bt_ok.place(relx = 0.9, rely = 0.9)

    if list_player[0].in_game :
        bt_stay_0.place(relx = 0.041, rely = 0.72)
        bt_quit_0.place(relx = 0.046, rely = 0.80)
    if list_player[1].in_game :
        bt_stay_1.place(relx = 0.161, rely = 0.72)
        bt_quit_1.place(relx = 0.166, rely = 0.80)
    if list_player[2].in_game :
        bt_stay_2.place(relx = 0.281, rely = 0.72)
        bt_quit_2.place(relx = 0.286, rely = 0.80)
    if len(list_player) > 3:
        if list_player[3].in_game :
            bt_stay_3.place(relx = 0.401, rely = 0.72)
            bt_quit_3.place(relx = 0.406, rely = 0.80)
    if len(list_player) > 4:
        if list_player[4].in_game :
            bt_stay_4.place(relx = 0.521, rely = 0.72)
            bt_quit_4.place(relx = 0.526, rely = 0.80)
    if len(list_player) > 5:
        if list_player[5].in_game :
            bt_stay_5.place(relx = 0.641, rely = 0.72)
            bt_quit_5.place(relx = 0.646, rely = 0.80)
    if len(list_player) > 6:
        if list_player[6].in_game :
            bt_stay_6.place(relx = 0.761, rely = 0.72)
            bt_quit_6.place(relx = 0.766, rely = 0.80)
    if len(list_player) > 7:
        if list_player[7].in_game :
            bt_stay_7.place(relx = 0.881, rely = 0.72)
            bt_quit_7.place(relx = 0.886, rely = 0.80)
    bt_ok.wait_variable(okvar)

    # -------------------------------------------------------------------

    if len(player_out) != 0 :
        for i in range(len(deck_shown)):
            temp_total += deck_shown[i].nbr_gem
            if deck_shown[i].relic :
                temp_relic.append(i)
        for i in range(len(player_out)):
            list_player[player_out[i]].total_gem += list_player[player_out[i]].temp_gem
            list_player[player_out[i]].temp_gem = 0
            list_player[player_out[i]].total_gem += (temp_total // len(player_out))
        for i in range (len(deck_shown)):
            deck_shown[i].nbr_gem = 0
        j = 0
        for i in range (len(deck_shown)):
            if deck_shown[i].treasure :
                deck_shown[i].nbr_gem = temp_total - ((temp_total // len(player_out)) * len(player_out))
                i = len(deck_shown)-1
        if len(temp_relic) > 0 :
                if len(player_out) == 1 :
                    for i in range (len(temp_relic)):
                        list_player[player_out[0]].total_gem += find_relic_val(list_player)
                        list_player[player_out[0]].nbr_relic += 1
                elif len(player_out) > 1 :
                    for i in range (len(temp_relic)):
                        list_player[player_out[0]].nbr_relic += 1
                for i in range (len(temp_relic)):
                    to_remove = deck_shown[temp_relic[i]]
                    deck_shown.remove(to_remove)
    return deck_shown, list_player
    
game_graph()
