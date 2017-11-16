# coding: utf-8

import random

#Represents a single playing card
class Card:
    def __init__(self,p_suit="J", p_value="0"):
        self.create(p_suit,p_value)

    #creates a card with a suit, value pair
    def create(self,p_suit="J", p_value="0"):
        self.suit = p_suit
        self.value = p_value

    #returns string representation of the card
    def __str__(self):
        return "{0}{1} ".format(self.suit, self.value)


# Each card in the deck should be an object formatted as: {suit: 'hearts', value: 'A'}
class Deck:
    def __init__(self):
        self.deck = []
        self.create()

    # 1. Make the function deck_o_cards assemble an array of cards using the provided suits and values arrays.
    def create(self):
        values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        suits = ('♥', '♦', '♣', '♠')
        self.deck = []

        # Make 52 card objects and store them in the "cards" array
        for s in suits:
          for v in values:
            self.deck.append(Card(s, v))

    #2. Shuffle the cards. Fisher-Yates Shuffle: http://stackoverflow.com/a/6274398
    def shuffle(self):
        length = len(self.deck)
        for i in range(length):
            random.seed()
            index = random.randint(0,length-1)
            temp = self.deck[i];
            self.deck[i] = self.deck[index]
            self.deck[index] = temp

    #removes the deck's top element (first card) and returns the value
    def draw(self):
        return self.deck.pop()

    #returns the top element (first card) in the deck
    def peek(self):
        return self.deck[0]

    #returns size (number of items) in the deck
    def size(self):
        return len(self.deck)

    #returns string representation of the deck
    def __str__(self):
        tmp = ""
        for i in self.deck:
            tmp += str(i)
        return tmp

#### PROGRAM START
deck = Deck()

# 3. Print the results:
print('The Original Deck has {} cards.'.format(deck.size()))
print('The top card is = {}'.format(deck.peek()))
print('Original Deck:')
print(deck)
print('----')

deck.shuffle()
print('The Shuffled Deck has {} cards.'.format(deck.size()))
print('The top card is {}'.format(deck.peek()))
print('Shuffled Deck:')
print(deck)
print('----')

# BONUS: Make a new array that pulls the top 5 cards and gives you a hand of poker!!
for i in range(0,5):
  print('Draw {0}: {1}'.format(i+1,deck.draw()))

print('Shuffled Deck after Draw:')
print(deck)
