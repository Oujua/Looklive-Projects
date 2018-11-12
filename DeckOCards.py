from random import shuffle
class Card:
    def __init__(self,suit,value): #Takes in a suit and a value for each card
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"
class Deck:
    def __init__(self):
        self.cards = []
        suitlist = ["Hearts", "Diamonds", "Clubs", "Spades"] #Definition of the different suits
        valuelist = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] #Definition of the different values
        for suit in suitlist:
            for value in valuelist:
                self.cards.append(Card(suit,value)) #Assigns each card a suit
        print(self.cards)

    def count(self):
        return len(self.cards) #Returns the number of cards left in the deck

    def __repr__(self):
        return f"\nThere are {self.count()} cards left in the deck"

    def shuffle(self):
        if self.count() < 52:
            raise ValueError(f"There must be 52 cards in the deck for a shuffle to occur! Current cards: {self.count()}") #Doesn't shuffle if less than 52 cards
        shuffle(self.cards) #shuffles using random import (Udemy course reference used)
        return self

    def _deal(self, numOfCards):
        count = self.count()
        if count == 0:
            raise ValueError("All the cards have been dealt currently.") #If deck is empty, return a different error
        amountDealt = min([count, numOfCards])
        print(f"\nRemoving {amountDealt} card(s)...\n") #Removes the top card(s)
        cards = self.cards[-amountDealt:]
        self.cards = self.cards[:-amountDealt]
        return cards

    def deal_hand(self,num):
        return self._deal(num) #Deals num amount of cards

    def deal_one(self):
        return self._deal(1)[0] #Deals a single card located at the zero index, with the 1 being defined inside

 ###UNIT TESTS###

a = Deck()
a.shuffle()
card = a.deal_one()
print(card)
hand = a.deal_hand(5)
print(hand)
print(a)
