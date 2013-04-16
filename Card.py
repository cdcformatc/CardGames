
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
    
    def __cmp__(self,other):
        if self.rank != other.rank:
            return self.rank-other.rank
        else:
            return self.suit-other.suit
            
    def compareRanks(self,other):
        return self.rank-other.rank
        
        
def _test():
    myCard = Card(1,0)
    print myCard
    
    for s in xrange(4):
        for r in xrange(1,14): 
            myCard = Card(r,s)
            print myCard
            
    try:
        Card(0,1)
    except ValueError as error:
        print error
    except:
        assert False,"Raised Wrong exception type"
    else:
        assert False,"Creation of invalid card did not raise exception"
        
    try:
        Card(14,1)
    except ValueError as error:
        print error
    except:
        assert False,"Raised Wrong exception type"
    else:
        assert False,"Creation of invalid card did not raise exception"
        
    try:
        Card(1,6)
    except ValueError as error:
        print error
    except:
        assert False,"Raised Wrong exception type"
    else:
        assert False,"Creation of invalid card did not raise exception"
        
    try:
        Card(1,-1)
    except ValueError as error:
        print error
    except:
        assert False,"Raised Wrong exception type"
    else:
        assert False,"Creation of invalid card did not raise exception"
        
    try:
        Card(0,-1)
    except ValueError as error:
        print error
    except:
        assert False,"Raised Wrong exception type"
    else:
        assert False,"Creation of invalid card did not raise exception"
        
    myCard = Card(1,0)
    myOther = Card(1,0)
   
    print myCard==myOther
    assert myCard==myOther,"Cards not equal"
    
    print not myCard<myOther
    assert not myCard<myOther,"Card greater than or equal to other"
    
    print myCard<=myOther
    assert myCard<=myOther,"Card is greater than other"
    
    print not myCard>myOther
    assert not myCard>myOther,"Card is greater than other"
    
    print myCard>=myOther
    assert myCard>=myOther,"Card is less than other"
    
    myOther = Card(1,2)#change suit, does not change rank
    print not myCard==myOther
    assert not myCard==myOther,"Cards equal"
    
    print myCard!=myOther
    assert myCard!=myOther,"Cards equal"
    
    print myCard<myOther
    assert myCard<myOther,"Card not greater than other"
    
    print myCard<=myOther
    assert myCard<=myOther,"Card is greater than other"
    
    print not myCard>myOther
    assert not myCard>myOther,"Card is greater than other"
    
    print not myCard>=myOther
    assert not myCard>=myOther,"Card is less than equal to other"
    
    myOther = Card(2,2)#change suit and rank
    print not myCard==myOther
    assert not myCard==myOther,"Cards equal"
    
    print myCard!=myOther
    assert myCard!=myOther,"Cards equal"
    
    print myCard<myOther
    assert myCard<myOther,"Card not greater than other"
    
    print myCard<=myOther
    assert myCard<=myOther,"Card is greater than other"
    
    print not myCard>myOther
    assert not myCard>myOther,"Card is greater than other"
    
    print not myCard>=myOther
    assert not myCard>=myOther,"Card is less than equal to other"
    
    myCard,myOther = (myOther,myCard,)#swap cards
    
    print not myCard==myOther
    assert not myCard==myOther,"Cards equal"
    
    print myCard!=myOther
    assert myCard!=myOther,"Cards equal"
    
    print not myCard<myOther
    assert not myCard<myOther,"Card not greater than other"
    
    print not myCard<=myOther
    assert not myCard<=myOther,"Card is greater than other"
    
    print myCard>myOther
    assert myCard>myOther,"Card is greater than other"
    
    print myCard>=myOther
    assert myCard>=myOther,"Card is less than equal to other"
    
    cards = [Card(i,0) for i in xrange(1,14)]
    from random import shuffle
    
    copy = list(cards)
    assert cards==copy
    
    while cards==copy:
        shuffle(cards)
    
    assert cards!=copy
    
    sort = sorted(cards)
    
    for card in cards:
        print card
    
    for card in sort:
        print card
        
    assert cards!=sort
    
    cards = [Card(1,i) for i in xrange(0,4)]
    
    copy = list(cards)
    assert cards==copy
    
    while cards==copy:
        shuffle(cards)
    
    assert cards!=copy
    
    sort = sorted(cards)
    
    for card in cards:
        print card
    
    for card in sort:
        print card
        
    assert cards!=sort
    


if __name__ == '__main__':
    _test()