
class Player:

    def __init__(self, name, casino_acount, bet =0) -> None:
        self.name = name
        self.bet = bet
        self.casino_acount = casino_acount
        self.cards = []

    def set_bet(self, p_bet):
        if (self.casino_acount - p_bet) < 0:
            print('Sorry, you dont have enough money')
            print(f'You only have {self.casino_acount}$ left in your acount')
            return False
        
        else: 
            self.casino_acount -= p_bet
            self.bet += p_bet
            print(f'Your bet of {p_bet} was set succefully')
            return True
            

    def __str__(self) -> str:
        message =f'----{self.name} information------\n'
        for card in self.cards:
            message += f'card: {card.rank} of {card.suit}--value:{card.value} \n'
        message += f'Actual bet: {self.bet}\n'
        message += f'Money left: {self.casino_acount}\n'
        message += '---------------------------------'
        return message