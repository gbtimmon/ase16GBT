"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
import sys
from Card import *

class Hist(dict):
    """A map from each item (x) to its frequency."""

    def __init__(self, seq=[]):
        "Creates a new histogram starting with the items in seq."
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        "Increments the counter associated with item x."
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):

    labels = ['flush', 'twopair', 'pair', 'highcard']

    def card_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        self.ranks = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.card_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Returns true if the hand has a pair, false otherwise."""
        self.card_hist()
        for val in self.ranks.values():
            if val >= 2:
              return True
        return False

    def has_twopair(self):
        """returns true if the hand has a two pair, false otherwise"""
        self.card_hist()
        pair_found = False
        for val in self.ranks.values():
            if val >= 2:
                if pair_found:
                    return True
                else:
                    pair_found = True
        return False

    def classify(self):
        """sets the label for the highest value hand"""
        if self.has_flush():
            self.label = "flush"
            return
        if self.has_twopair():
            self.label = "twopair"
            return
        if self.has_pair():
            self.label = "pair"
            return
        label = "highcard"

class PokerDeck(Deck):
    """Represents a deck of cards that can deal poker hands."""

    def deal_hands(deck, num_cards=5, num_hands=10):
        hands = []
        for i in range(num_hands):
            hand = PokerHand()
            deck.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)
        return hands


def main(*args):
    # the label histogram: map from label to number of occurances
    lhist = Hist()

    # loop n times, dealing 7 hands per iteration, 7 cards each
    n = 10000
    for i in range(n):
        if i%1000 == 0:
            print i

        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(7, 7)
        for hand in hands:
            lhist.count(hand.label)

    # print the results
    total = 7.0 * n
    print total, 'hands dealt:'

    for label in PokerHand.labels:
        freq = lhist.get(label, 0)
        if freq == 0:
            continue
        p = total / freq
        print '%s happens one time in %.2f' % (label, p)


if __name__ == '__main__':
    main(*sys.argv)



