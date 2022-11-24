import random
import os

class player :
    def __init__(self, name) :
        self.name = name
        self.total_gem = 0
        self.temp_gem = 0
        self.in_game = True
        self.nbr_relic = 0

class Card :
    def __init__(self, danger, type_danger, treasure, nbr_gem, relic) :
        self.danger = danger
        self.type_danger = type_danger
        self.treasure = treasure
        self.nbr_gem = nbr_gem
        self.relic = relic
    
def create_deck() :
    deck = []
    val_treasure = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
    for i in range (15) :
        deck.append(Card(False, 0, True, val_treasure[i], False))
    for i in range (1, 6) :
        for j in range (3) :
            deck.append(Card(True, i, False, 0, False))
    deck.append(Card(False, 0, False, 0, True))
    random.shuffle(deck)
    return deck

def start_game():
    #Récupération du nombre de joueurs
    nb_player = int(input("Combien de joueurs êtes-vous ?"))
    while nb_player > 8 or nb_player < 3 :
        nb_player = int(input("Nombre de joueurs incorrects, il faut être entre 3 et 8 joueurs"))

    #Création de la liste des joueurs
    list_player = []
    for i in range (nb_player) :
        print("Joueur ",i+1,",entrez votre nom")
        name = str(input())
        list_player.append(player(name))
    
    
    return list_player

def draw(deck,deck_shown,list_player):
    '''
        Prend la première carte du deck mélangé et la met sur le plateau de jeu (dans le dec affiché)
        Réparti les diamants de la carte entre les joueurs encore en jeu
        ENTREE
            deck : liste de cartes, deck_shown : liste de cartes, list_player : liste de joueurs
        SORTIE
            deck : liste de cartes, deck_shown : liste de cartes, list_player : liste de joueurs
    '''
    new_card = deck[0]
    nbr_in_game = 0
    if new_card.treasure :
        for i in range(len(list_player)):
            if list_player[i].in_game :
                nbr_in_game += 1
        for i in range(len(list_player)):
            if list_player[i].in_game :
                list_player[i].temp_gem += (new_card.nbr_gem//nbr_in_game)
        new_card.nbr_gem -= (new_card.nbr_gem//nbr_in_game)*nbr_in_game
    deck_shown.append(new_card)
    deck.remove(new_card)
    return deck, deck_shown, list_player

def trap_check(deck_shown):
    '''
        Détecte si un piège est présent deux fois sur le plateau
    
        ENTREE
            deck_shown : liste de cartes
        
        SORTIE
            trap_detected : booléen
    '''
    trap_detected = False
    trap_in_game = []
    for i in range(len(deck_shown)):
        if deck_shown[i].type_danger != 0 :
            trap_in_game.append(deck_shown[i].type_danger)
    for i in range(1,6):
        if i in trap_in_game :
            trap_in_game.remove(i)
            if i in trap_in_game :
                trap_detected = True
    return trap_detected

def find_relic_val(list_player):
    '''
        Trouve la valeur de la prochaine relique qui va sortir (5, 5, 5, 10, 10)

        ENTREE
            list_player : liste de joueurs
        
        SORTIE
            val_relic : entier (5 ou 10)
    '''
    relic_sum = 0
    val_relic = 0
    for i in range (len(list_player)):
        relic_sum += list_player[i].nbr_relic
    if relic_sum < 3 :
        val_relic = 5
    elif relic_sum >= 3 :
        val_relic = 10
    return val_relic

def player_action(deck_shown,list_player):
    '''
        Demande au joueur s'il souhaite continuer à jouer ou rentrer au campement
        Si il veut sortir, répartit les gemmes an conséquence
        ENTREE
            deck_shown : liste de cartes, list_player : liste de joueurs
        
        SORTIE
            deck_shown : liste de cartes, list_player : liste de joueurs
    '''
    player_out = []
    temp_total = 0
    temp_relic = []
    for i in range (len(list_player)):
        if list_player[i].in_game :
            is_out = ''
            while (is_out != 'O') and (is_out != 'N') :
                is_out = input(list_player[i].name + ' Sortir ? (O/N) ').upper()
            if is_out == 'O' :
                list_player[i].in_game = False
                player_out.append(i)
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


def check_end(list_player):
    '''
        Détecte les conditions de fin de manche
        Détecte si tous les joueurs sont sortis
        Renvoie True si tous les joueurs sont sortis ou si un piège est présent deux fois sur le plateau
        ENTREE
            list_player : liste de joueurs, trap_detected : booléen
        
        SORTIE
            end_round : booléen
    '''
    end_round = False
    player_out = 0
    for i in range(len(list_player)):
        if list_player[i].in_game == False :
            player_out += 1
    if player_out == len(list_player):
        end_round = True
    return end_round

def display(deck_shown,list_player,round):
    '''
        Affiche les cartes présentes sur le plateau :
            Les cartes trésor sont affichées avec le nombre de gemmes qu'il leur reste après la distribution
            Les cartes danger sont affichées avec leur type de danger (1 à 5)
        Affiche pour chaque joueur :
            Son nom
            Son statut dans le jeu (dans le temple / au camp)
            Le nombre de gemmes qu'il a dans le temple
            Le nombre de gemmes qu'il a au camp
        
        ENTREE
            deck_shown : liste de cartes, list_player : liste de joueurs
        
        SORTIE
            ---
    '''
    os.system('clear')
    print('Manche',round,'/ 5','\n')
    temp_total = 0
    for i in range (len(deck_shown)):
        if deck_shown[i].danger :
            print('DANGER',deck_shown[i].type_danger)
        elif deck_shown[i].treasure :
            print('TRESOR')
            temp_total += deck_shown[i].nbr_gem
        elif deck_shown[i].relic :
            print('RELIQUE')
    print()
    print('Gemmes restantes :',temp_total)
    print()
    for i in range (len(list_player)):
        if list_player[i].in_game :
            position = '(dans le temple)'
        else :
            position = '(au campement) '
        print('{:>15s}{:>19s}{:>11s}{:>21s}'.format(str(list_player[i].name),position+' :',str(list_player[i].temp_gem)+' gemmes',str(list_player[i].total_gem)+' gemmes stockées'))
    print()

def round(list_player, round) :
    deck = create_deck()
    deck_shown = []
    end_round = False
    while not end_round :
        if check_end(list_player) :
            end_round = True
        if not end_round :
            draw(deck, deck_shown, list_player)
        if trap_check(deck_shown) :
            end_round = True
        if not end_round :
            display(deck_shown, list_player, round) 
            player_action(deck_shown, list_player) 
            display(deck_shown, list_player, round)
    return list_player
