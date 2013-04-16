import Card

class Deck():
    def __init__(self, empty=False, cards=[]):
        self.deck = cards

        if len(cards)==0 and not empty:
            for suit in range(4):
                for rank in range(1,14):
                    self.deck.append(Card.Card(rank,suit))
                
    def __str__(self):
        ret = ''
        for card in self.deck[::-1]:
            ret += str(card)+", "
            
        ret = ret[:-2]
        return ret
        
    # def __copy__(self):
        # return Deck(self.deck[:])
        
    def __len__(self):
        return len(self.deck)
        
    # def shuffle(self):
        # from random import shuffle as sh
        # sh(self.deck)
        
    # def drawCard(self):
        # try:
            # card = self.deck.pop()
            # return card
        # except IndexError:
            # raise IndexError('No more cards in deck')
            
    # def insertCard(self,card):
        # if isinstance(card, Card.Card):
            # self.deck.append(card)
        # else:
            # raise ValueError('Card not instance of Card()')
        
    # def __add__(self,card):
        # self.insertCard(card)
    
def _test():
    myDeck = Deck()

    # print myDeck
    # print len(myDeck)
    # assert len(myDeck)==52
    
    myDiscard = Deck(empty=True)
    
    print myDiscard
    print len(myDiscard)
    assert len(myDiscard)==0
    
    # myCard = myDeck.drawCard()
    # print myCard
    # print myDeck
    # print len(myDeck)
    # assert len(myDeck)==51
    
    # myDiscard.insertCard(myCard)
    
    # print myDiscard
    # print len(myDiscard)
    # assert len(myDiscard)==1
    
    # myDeck.shuffle()
    
    # print myDeck
    # myCard = myDeck.drawCard()
    # print myCard
    # print myDeck
    # print len(myDeck)
    # assert len(myDeck)==50
    

if __name__ == '__main__':
    _test()