from Player import Player
from Deck import Deck
from Dealer import Dealer


def check_values(player_cards, dealer_cards):
    total_score_dealer = 0
    total_score_player = 0
    ace_player = False
    for card in player_cards:
        if card.rank == 'Ace':
            ace_player = True
        else:
            total_score_player += card.value
    
    for card in dealer_cards:
        if card.rank == 'Ace':
            total_score_dealer+=11
        else:
            total_score_dealer += card.value
    
    if ace_player:
        if (total_score_player + 11) > 21:
            total_score_player +=1
        elif(total_score_player +11) <=21:
            total_score_player +=11
    
    
    return total_score_player, total_score_dealer

def check_winner(score_player, score_dealer):
    target_score = 21
    #verificar si jugaro esta dentro del valor permitido
    if (target_score - score_player) > 0:
        if (target_score-score_player) > (target_score-score_dealer):
            return False, f'(LA CASA GANA) - Player:{score_player} - Dealer: {score_dealer} '
        else:
            return True, f'(GANA EL JUGADOR) - Player:{score_player} - Dealer: {score_dealer}'
    elif (target_score - score_player) == 0:
        return True, F'(BLACKJACK) - Player:{score_player} - Dealer: {score_dealer}'
    else:
        return False, f'(LA CASA GANA) - Player:{score_player} - Dealer: {score_dealer} '

def keep_playing():
    while True:
        response = input('Do you want to keep playing?(y/n): ')
        if response.upper() == 'Y':
            return True
        elif response.upper() == 'N':
            return False
        else:
            print('INVALID ANSWER. try again!')

#inicialize the game
initial_amount_money = 500
player = Player('Pablo', initial_amount_money)
dealer = Dealer()


#Dealer deal the cards
playing=True
while playing:
    correct_bet = False
    dealer_game, player_game = dealer.deal_cards()

    player.cards = player_game
    print(player)
    while not correct_bet:
        player_bet = int(input('Enter the value to bet: '))

        correct_bet = player.set_bet(player_bet)
    on_game = True
    while on_game:
        print(player)
        another_card = input('Do you want another card?(y/n): ')

        if another_card.upper() == 'Y':
            other_card = dealer.give_card()
            player.cards.append(other_card)

        elif another_card.upper() == 'N':
            on_game = False
            score_player, score_dealer = check_values(player.cards, dealer_game)
            player_win, message = check_winner(score_player, score_dealer)
            if player_win:
                print(dealer)
                print(message)
                player.casino_acount += (player.bet*2)
                player.bet = 0
                playing = keep_playing()
                if playing:
                    print('Ok, new game start now\n')
                else:
                    print(f'Bye bye, your amount now is: {player.casino_acount}')
                    
            else:
                print(dealer)
                print(message)
                player.bet = 0
                playing = keep_playing()
                if playing:
                    print('Ok, new game start now\n')
                else:
                    print(f'Bye bye, your amount now is: {player.casino_acount}')
                    
        else:
            print('INVAILD VALUE. Please try again')