from random import shuffle


class Card:
    def __init__(self, suit, value):  # Takes in a suit and a value for each card
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        # Definition of the different suits
        suitlist = ["Hearts", "Diamonds", "Clubs", "Spades"]
        valuelist = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King"]  # Definition of the different values
        for suit in suitlist:
            for value in valuelist:
                # Assigns each card a suit
                self.cards.append(Card(suit, value))
        print(self.cards)

    def count(self):
        return len(self.cards)  # Returns the number of cards left in the deck

    def __repr__(self):
        return f"\nThere are {self.count()} cards left in the deck"

    def shuffle(self):
        if self.count() < 52:
            # Doesn't shuffle if less than 52 cards
            raise ValueError(
                f"There must be 52 cards in the deck for a shuffle to occur! Current cards: {self.count()}")
        # shuffles using random import (Udemy course reference used)
        shuffle(self.cards)
        return self

    def _deal(self, numOfCards):
        count = self.count()
        if count == 0:
            # If deck is empty, return a different error
            raise ValueError("All the cards have been dealt currently.")
        amountDealt = min([count, numOfCards])
        # Removes the top card(s)
        print(f"\nRemoving {amountDealt} card(s)...\n")
        cards = self.cards[-amountDealt:]
        self.cards = self.cards[:-amountDealt]
        return cards

    def deal_hand(self, num):
        return self._deal(num)  # Deals num amount of cards

    def deal_one(self):
        # Deals a single card located at the zero index, with the 1 being
        # defined inside
        return self._deal(1)[0]

 ###UNIT TESTS###


a = Deck()
a.shuffle()
card = a.deal_one()
print(card)
hand = a.deal_hand(5)
print(hand)
print(a)
