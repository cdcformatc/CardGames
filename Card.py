
class Card():
    def __init__(self,rank,suit):
        if (suit < 0 or suit > 4) and (rank < 1 or rank > 13):
            raise ValueError('Invalid Suit and Rank')
        if suit < 0 or suit > 4:
            raise ValueError('Invalid Suit')
        if rank < 1 or rank > 13:
            raise ValueError('Invalid Rank')
        self.suit = suit
        self.rank = rank
    
    def getSuit(self):
        if self.suit==0:
            return "Spades"
        if self.suit==1:
            return "Clubs"
        if self.suit==2:
            return "Diamonds"
        else:
            return "Hearts"
        
    def getRank(self):
        if self.rank == 1:
            return "Ace"
        if self.rank == 11:
            return "Jack"
        if self.rank == 12:
            return "Queen"
        if self.rank == 13:
            return "King"
        else:
            return str(self.rank)
    
    def __str__(self):
        return self.getRank()+" of " + self.getSuit()
        
        
def _test():
    myCard = Card(1,0)
    print myCard
    
    for s in range(4):
        for r in range(1,14): 
            myCard = Card(r,s)
            print myCard
            
    try:
        Card(0,1)
    except ValueError as error:
        print error
        
    try:
        Card(14,1)
    except ValueError as error:
        print error
        
    try:
        Card(1,6)
    except ValueError as error:
        print error
        
    try:
        Card(1,-1)
    except ValueError as error:
        print error
        
    try:
        Card(0,-1)
    except ValueError as error:
        print error

if __name__ == '__main__':
    _test()