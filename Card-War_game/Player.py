class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []

    
    def add(self, cards):
        self.all_cards.extend(cards)

    def play_card(self):
        return self.all_cards.pop(0)
    
    def __str__(self) -> str:
        return f'Payer {self.name} has {len(self.all_cards)} cards left'