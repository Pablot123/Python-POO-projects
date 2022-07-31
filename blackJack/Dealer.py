from Deck import Deck

class Dealer:

    def __init__(self, cards =[]) -> None:
        self.cards = cards
        self.deck = Deck()
        self.deck.shuffle_deck()
    

    def deal_cards(self):
        dealer_cards = []
        player_cards = []

        for i in range(4):
            if i%2 ==0:
                dealer_cards.append(self.deck.used_card())
            else:
                player_cards.append(self.deck.used_card())
        self.cards = dealer_cards
        return dealer_cards, player_cards

    def give_card(self):
        return self.deck.used_card()

    def __str__(self) -> str:
        message =f'----Casa information------\n'
        for card in self.cards:
            message += f'card: {card.rank} of {card.suit}--value:{card.value} \n'
        message += '---------------------------------'
        return message
