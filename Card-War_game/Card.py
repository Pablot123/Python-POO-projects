ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

suits = ('Diamonds', 'Hearts', 'Spades', 'Clubs') 
class Card:

    values = {
        'Two': 2,
        'Three':3,
        'Four':4,
        'Five':5,
        'Six':6,
        'Seven':7,
        'Eight':8,
        'Nine':9,
        'Ten':10,
        'Jack':11,
        'Queen':12,
        'King':13,
        'Ace':14

    }

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank =  rank
        self.value = Card.values[rank]
    
    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'
