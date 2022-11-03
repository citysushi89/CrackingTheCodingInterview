"""
Design a data structure for a deck of cards, 
describe how you would sublcass the data structure to implement blackjack
"""
import random


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1, 52):
            if i < 14:
                self.cards.append(Card(i + 1, 'Hearts'))
            elif 13 < i < 27:
                self.cards.append(Card((i - 12), 'Diamonds'))
            elif 26 < i < 39:
                self.cards.append(Card((i - 24), 'Clubs'))
            elif 38 < i < 53:
                self.cards.append(Card((i - 37), 'Spades'))


class Card:
    def __init__(self, num, symbol):
        self.num = num
        self.symbol = symbol

"""
To implement blackjack, we would create several functions in the deck class such as:
deal_start, deal_one (hit), deal_two_d (double), deal_to_s (split) and so on
If we were implementing single-hand blackjack, we would also need to track cards 
that have been removed thus far
Depending on depth we would also need some functions in the card class such as show_card 
(to account for the dealer only showing one card but the other removing from the deck)
"""
