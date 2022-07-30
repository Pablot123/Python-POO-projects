
class Player:

    def __init__(self, name, casino_acount) -> None:
        self.name = name
        self.casino_acount = casino_acount
        self.cards = []

    def set_bet(self, bet):
        if (self.casino_acount - bet) < 0:
            print('Sorry, you dont have enough money')
        
        else: 
            pass