## War Game
## ver1

import random

class Card:
    '''buildcard objects'''
    ##every card object have ranking and alliance2666
    def __init__(self, rank, alliance, value):
        self.rank = rank 
        self.alliance = alliance ##
        self.value = value ##card numeric value
        
    def __repr__(self):
        return f"{self.rank}{self.alliance}"



class Deck:
    '''creates a collectioin of card objects'''
    ##a deck consist of card objects
    def __init__(self):
        self.deck = []
        for alliance in ["black","heart","clover","spades"]:
            ##create of list of card objects: 52cards
            self.deck.append(Card("A",alliance,14))
            self.deck.append(Card('2',alliance,2))
            self.deck.append(Card('3',alliance,3))
            self.deck.append(Card('4',alliance,4))
            self.deck.append(Card('5',alliance,5))
            self.deck.append(Card('6',alliance,6))
            self.deck.append(Card('7',alliance,7))
            self.deck.append(Card('8',alliance,8))
            self.deck.append(Card('9',alliance,9))
            self.deck.append(Card('10',alliance,10))
            self.deck.append(Card("Joker",alliance,11))
            self.deck.append(Card("Queen",alliance,12))
            self.deck.append(Card("King",alliance,13))
        
    def shuffle(self):
        '''shuffle the deck of cards'''
        random.shuffle(self.deck) ##shuffle deck of cards
    def __len__(self):
        return len(self.deck)
    def pop(self):
        return self.deck.pop()


class Player:
    def __init__(self, playerName):
        self.name = playerName
        self.cards = []##cards up
        self.war_cards = []
    def playcard():
        '''return card from player's set '''
        return self.cards.pop()##play a card from player's set
    def playWarcard():
        return self.war_cards.pop()
    def __repr__(self):
        return f"name {self.name}\n cards {self.cards}"




class CardGame:##this is where we play the game

    deck_of_Cards = Deck()
    player1 = Player(None)
    player2 = Player(None)
    
    def Distribute(self,player1,player2,DECK):
        '''add cards from deck to players set'''
#         print(DECK,len(DECK))
        for rep in range(26): ##distribute cards evenly among the players
            self.player1.cards.append(DECK.pop())##add cards from dec to players set
            self.player2.cards.append(DECK.pop())
    
    def compare(self,player1Card,player2Card):
        '''compare player 1 and two cards and return if player1 or 2 wins'''
        ##compare the card rankings and return value of winner(1 or 2) or tie play(o)
        if player1Card.value > player2Card.value: return 1
        elif player1Card.value < player2Card.value: return 2 
        else: return 0 ##
        

    def play(self):
        self.player1.name = input("Player1 Enter name: ")
        self.player2.name = input("Player2 Enter name: ")
        self.deck_of_Cards.shuffle() ##
        
        self.Distribute(self.player1,self.player2,self.deck_of_Cards)
#         print(player1.cards,player2.cards)
        while (len(self.player1.cards)!=0 and len(self.player2.cards)!=0): ##keep playing if the players still have cards in hand
            print(len(self.player1.cards), len(self.player2.cards))
           ##check if players have cards in set to play before drawinf from set
#           print(self.player1.cards, self.player2.cards)
            player1Card,player2Card = self.player1.cards.pop(), self.player2.cards.pop()
            
#             print(self.compare(player1Card, player2Card))
            if self.compare(player1Card,player2Card) == 1:
                self.player1.cards.insert(0,player1Card)
                self.player1.cards.insert(0,player2Card)

            elif self.compare(player1Card,player2Card)==2: 
                ##add played cards to player 2 cardset
                self.player2.cards.insert(0,player1Card)
                self.player2.cards.insert(0,player2Card)
            elif self.compare(player1Card,player2Card)==0: 
                ##if zero then the play was a tied
                print("WAR!".center(10))
                self.warPlay(player1Card,player2Card) 
         
        ##pick out the winner of the game
        if len(player1.cards) > player2.cards: return f"The Winner is {player1.name}!!"
        elif len(player2.cards) > player1.cards: return f"The Winner is {player2.name}!!"
        else: return "It's a Tie Game!\n Wanna play another round?"
        
        
        
    def warPlay(self,player1Card,player2Card):
        '''play from war set of cards'''
#       player1Card,player2Card = player1.war_cards.pop(), player2.war_cards.pop()
        ##cards on board
        boardcards = [player1Card,player2Card]
        facedownCards = []##
         
        while len(self.player1.cards)>=2 and len(self.player2.cards)>=2: ##you need at least 2 cards to play war
            facedownCards.extend([self.player1.cards.pop(), self.player2.cards.pop()])
            player1Card, player2Card = self.player1.cards.pop(), self.player2.cards.pop()
            
            if self.compare(player1Card,player2Card)==1:
                ##add board, facedown cards to player1 card list
#                 print(facedownCards,boardcards)
                self.player1.cards = facedownCards+boardcards + self.player1.cards
                break
            elif self.compare(player1Card,player2Card)==2:
#                 print(facedownCards,boardcards)
                self.player2.cards = facedownCards+boardcards+self.player2.cards
                break

            elif self.compare(player1Card,player2Card)==0:
#                 print(facedownCards,boardcards)
                self.warPlay(player1Card,player2Card)
           
#         DO: the cards on board/facedown cards goes to player with most cards. if the other player runs out of cards
        
