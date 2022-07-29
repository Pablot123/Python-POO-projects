from Card import Card
from Deck import Deck
from Player import Player

def game_initialize():
    #users name
    player_1_name = input('Player 1 name: ')
    player_2_name = input('Player 2 name: ')

    player_1 = Player(player_1_name)
    player_2 = Player(player_2_name)

    all_deck = Deck()
    all_deck.shuffle_deck()
    player_1.all_cards = all_deck.all_cards[:26]
    player_2.all_cards = all_deck.all_cards[26:]

    return player_1, player_2

def print_players(player_1, player_2):
    print(player_1)
    print(player_2)

def play(player_1, player_2, cards_on_table):
    card_player_1 = player_1.play_card()
    card_player_2 = player_2.play_card()
    cards_on_table.append(card_player_1)
    cards_on_table.append(card_player_2)
    return cards_on_table, card_player_1, card_player_2

def winner(player_1, player_2):
    if len(player_1.all_cards) == 0:
        print(f'THE WINNER IS {player_2.name}!!!!')
        return False
    elif len(player_2.all_cards) == 0:
        print(f'THE WINNER IS {player_1.name}!!!!')
        return False 
    else:
        return True

def main(player_1:Player, player_2:Player):
    game_on =True
    cards_on_game = []
    while game_on:
        print_players(player_1, player_2)
        cards_on_game, card_player_1, card_player_2 = play(player_1, player_2, cards_on_game)
        
        if card_player_1.value == card_player_2.value:
            war = True
            while war:
                print('WAR!!')
                if len(player_1.all_cards) <=3 or len(player_2.all_cards) <=3:
                    for _ in range(min(len(player_1.all_cards),len(player_2.all_cards)-1)):
                        cards_on_game, card_player_1, card_player_2 = play(player_1, player_2, cards_on_game)
                    
                    cards_on_game, card_player_1, card_player_2 = play(player_1, player_2, cards_on_game)

                    if card_player_1.value == card_player_2.value:
                        war = True
                    elif card_player_1.value > card_player_2.value:
                        player_1.add(cards_on_game)
                        cards_on_game = []
                        war = False
                    elif card_player_1.value < card_player_2.value:
                        player_2.add(cards_on_game)
                        cards_on_game = []
                        war = False
                else:
                    for _ in range(3):
                        cards_on_game, card_player_1, card_player_2 = play(player_1, player_2, cards_on_game)
                    
                    cards_on_game, card_player_1, card_player_2 = play(player_1, player_2, cards_on_game)

                    if card_player_1.value == card_player_2.value:
                        war = True
                    elif card_player_1.value > card_player_2.value:
                        player_1.add(cards_on_game)
                        cards_on_game = []
                        war = False
                    elif card_player_1.value < card_player_2.value:
                        player_2.add(cards_on_game)
                        cards_on_game = []
                        war = False

        elif card_player_1.value > card_player_2.value:
            player_1.add(cards_on_game)
            cards_on_game = []

        elif card_player_1.value < card_player_2.value:
            player_2.add(cards_on_game)
            cards_on_game = []
        else:
            pass

        game_on = winner(player_1, player_2)
  



if  __name__ == '__main__':
    player_1, player_2 = game_initialize()

    main(player_1, player_2)
