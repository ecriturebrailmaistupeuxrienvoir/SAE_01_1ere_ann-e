#Main
import random

class player :
    def __init__(self, name) :
        self.name = name
        self.total_gem = 0
        self.temp_gem = 0
        self.in_game = False

class Card :
    def __init__(self, danger, type_danger, treasure, nbr_gem, relic, val_relic) :
        self.danger = danger
        self.type_danger = type_danger
        self.treasure = treasure
        self.nbr_gem = nbr_gem
        self.relic = relic
        self.val_relic = val_relic
    
def create_deck() :
    deck = []
    val_treasure = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
    value_relic = [5, 5, 5, 10, 10]
    for i in range (15) :
        deck.append(Card(False, 0, True, val_treasure[i], False, 0))
    for i in range (1, 6) :
        for j in range (3) :
            deck.append(Card(True, i, False, 0, False, 0))
    for i in range (5) :
        deck.append(Card(False, 0, False, 0, True, value_relic[i]))
    random.shuffle(deck)
    return deck

def draw(deck,deck_shown,list_player):
    new_card = deck[0]
    if new_card.treasure :
        for i in range(len(list_player)):
            list_player[i].temp_gem += (new_card.nbr_gem//len(list_player))
        new_card.nbr_gem -= (new_card.nbr_gem//len(list_player))*len(list_player)
    deck_shown.append(new_card)
    deck.remove(new_card)
    return deck, deck_shown, list_player

def trap_check(deck_shown):
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

def check_end(list_player,trap_detected):
    end_round = False
    player_out = 0
    for i in range(len(list_player)):
        if list_player[i].in_game == False :
            player_out += 1
    if trap_detected or player_out == len(list_player):
        end_round = True
    return end_round
