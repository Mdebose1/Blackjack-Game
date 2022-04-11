import array
# import numpy as np
import math
import random

class Blackjack:
    def __init__(self):
        self.deck = {
            "club" : None, 
            "hearts" : None,
            "diamonds" : None,
            "spades" : None,
        }
         
    def cards(self):
        cards = [card for card in range(2,14)]
        for suite in self.deck:
            self.deck[suite] = cards


    def dealer(self):
        dealer_cards = [[random.choice(list(self.deck["hearts"])), random.choice(list(self.deck.keys()))], [random.choice(list(self.deck["hearts"])), random.choice(list(self.deck.keys()))]]
        print("Dealer's Cards X and ", dealer_cards[1])

    def player(self):
        players_cards = [[random.choice(list(self.deck["hearts"])), random.choice(list(self.deck.keys()))], [random.choice(list(self.deck["hearts"])), random.choice(list(self.deck.keys()))]]
        print("Player's Cards ", players_cards)
        hit= input("Would you like a hit? Yes or No").lower()
        if hit == "yes":
            players_cards.append(self)
            print("Player's Cards ",players_cards.append(self.players_cards))
        elif hit == "no":
                print("You have chosen to stay.")

  
    # print("Your total is " + int(total))
             
 

    # def hide_first_card(self):
    #     card1 = "X"
    #     for index, value in enumerate(card1):
    #      return card1

Game1 = Blackjack()
Game1.cards()
Game1.dealer()
Game1.player()

   