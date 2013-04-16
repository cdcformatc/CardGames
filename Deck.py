import Card

class Deck():
    def __init__(self, empty=False, cards=[]):
        self.deck = list(cards)
        
        if len(cards)==0 and not empty:
            self.deck = [Card.Card(r,s) for s in xrange(4) for r in xrange(1,14)]
            
    def __str__(self):
        if len(self.deck)==0:
            return '[]'
        ret = '['
        for card in self.deck[::-1]:
            ret += str(card)+", "
            
        ret = ret[:-2]+']'
        return ret
        
    def copy(self):
        return Deck(cards=self.deck[:])
        
    def __len__(self):
        return len(self.deck)
        
    def __cmp__(self,other):
        return cmp(self.deck,other.deck)
        
    def drawCard(self):
        try:
            return self.deck.pop()
        except IndexError:
            raise IndexError('No more cards in deck')
        
    def pop(self):
        return self.drawCard()
            
    def append(self,card):
        if isinstance(card, Card.Card):
            self.deck.append(card)
        else:
            raise ValueError('Card not instance of Card()')
            
    def shuffle(self):
        from random import shuffle as sh
        sh(self.deck)
        
    def __add__(one, two):
        if isinstance(one,Deck) and isinstance(two,Deck):
            return Deck(cards=one.deck[:] + two.deck[:])
        else:
            raise TypeError(' can only concatenate Deck not "'+type(other)+'"to Deck')
        
    
def _test():
    myDeck = Deck()

    print myDeck
    print len(myDeck)==52
    assert len(myDeck)==52
    
    myDiscard = Deck(empty=True)
    
    print myDiscard
    print len(myDiscard)==0
    assert len(myDiscard)==0
    
    myCard = myDeck.drawCard()
    print myCard
    print myDeck
    print len(myDeck)==51
    assert len(myDeck)==51
    
    myDiscard.append(myCard)
    print myDiscard
    print len(myDiscard)==1
    assert len(myDiscard)==1
    
    myCard = myDeck.pop()
    print myCard
    print myDeck
    print len(myDeck)==50
    assert len(myDeck)==50
    
    myDiscard.append(myCard)
    print myDiscard
    print len(myDiscard)==2
    assert len(myDiscard)==2
    
    myCopyDeck = myDiscard.copy()
    
    print myCopyDeck
    print len(myCopyDeck)==2
    assert len(myCopyDeck)==2
    print myDiscard==myCopyDeck
    
    myCopyDeck = myDeck.copy()
    myDeck.shuffle()
    
    print myDeck
    print myDeck!=myCopyDeck
    assert myDeck!=myCopyDeck
    
    myDeck = myDeck+myDiscard
    print myDeck
    print len(myDeck)==52
    assert len(myDeck)==52
    
    print myDeck!=myCopyDeck
    assert myDeck!=myCopyDeck
    

if __name__ == '__main__':
    _test()
