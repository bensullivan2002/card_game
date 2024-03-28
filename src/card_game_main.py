from enum import Enum


class Game:
    def __init__(self):
        self.players = []
        self.playing = False
        self.current_trick = Trick()

    def add_player(self, player):
        self.players.append(player)


class SuitOptions(Enum):
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"


class ValueOptions(Enum):
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 11


class Card(tuple):
    def __new__(cls, suit, value):
        assert isinstance(suit, SuitOptions)
        assert isinstance(value, ValueOptions)
        return tuple.__new__(cls, (suit, value))

    @property
    def suit(self):
        return self[0]

    @property
    def value(self):
        return self[1]

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __delattr__(self, *ignored):
        raise NotImplementedError

    def __str__(self):
        return "{} of {}s".format(self.value.name, self.suit.name)


class Deck:
    def __init__(self):
        self.cards = {
            Card(suit, value) for suit in SuitOptions for value in ValueOptions
        }


class Player:
    def __init__(self):
        self.ID = int
        self.name = str
        self.hand = Hand()

    def select_card_to_play(self):
        return input(f"Choose which card to play from {self.hand}")

    def play_card(self, select_card_to_play):
        pass

    def has_won(self):
        pass


class Hand:
    def __init__(self):
        self.cards = []


class Trick:
    def __init__(self):
        self.played_cards = []
        self.current_player = Player
        self.next_player = Player

    def is_ended(self):
        return len(self.played_cards) < 4
