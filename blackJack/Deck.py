from random import shuffle
from Card import Card, ranks, suits

class Deck:

    def __init__(self) -> None:

        self.all_cards =[]
        for suit in suits:
            for rank in ranks:

                created_card = Card(suit, rank)

                self.all_cards.append(created_card)
    
    def shuffle_deck(self):
        shuffle(self.all_cards)
    
    def used_card(self):
        return self.all_cards.pop()