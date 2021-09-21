import random

# Corresponding card and its value
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, \
    'J': 10, 'Q': 10, 'K':10, 'A': 11}

# Whether the game is active (not in stand).
is_playing = True
# Whether the current scoring is valid (no player has busted)
valid_game = True

class Deck:
    def __init__(self):
        """
        Initiate a 52-card DECK. This DECK consists of 4 suits.
        Each suit consists of:
            - "number cards" with a face value of 2-10, worth the number on the card
            - "face cards" (King, Queen, Jack), each worth 10 points
            - "aces" (Ace), worth 1 or 11 points
        """
        self.deck = []
        for _ in range(4):
            for card in values.keys():
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        """
        Shuffle the DECK and deal a single card.
        """
        deal_card = self.deck.pop()
        return deal_card

class Hand:
    def __init__(self):
        """
        - CARDS contains the cards in hand
        - VALUE is the total score of the cards in hand
        - ACES is the number of "Ace" in hand
        """
        self.cards = []
        self.value = 0
        self.aces = 0           

    def draw_card(self, card):
        """
        Draw a single card from shuffled deck and add the card into hand collection.
        Add the card value to the total scores of hand collection.
        """
        self.cards.append(card)
        self.value += values[card]
        if card == 'A':
            self.aces += 1
    
    def ace_value(self):
        """
        Aces can be 1 point or 11 points. The exact score of Ace is optimized
        based on the total score. If Ace-11 leads to a bust, then the value of
        Ace is 1. If Ace-11 does not lead to a bust, it then represents 11.
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Blackjack:
    def player_hit(deck, hand, dealer):
        """
        If player chooses to Hit, draw a card from the deck and adjust for 
        the Ace value if Ace is present.
        """
        hand.draw_card(deck.deal())
        hand.ace_value()

    def hit_or_stand(deck, hand, dealer):
        """
        Prompts the player with the option of Hit or Stand.
        """
        global is_playing

        print("Would you like to (H)it or (S)tand?", end=' ')
        option = input()
        if option[0] == 'H' or option[0] == 'h':
            Blackjack.player_hit(deck, hand, dealer)
            valid_game = Blackjack.check_valid_game(hand, dealer)
            if valid_game:    
                Blackjack.display_partial(hand, dealer)
            else:
                Blackjack.check_winner(hand, dealer)
        elif option[0] == 'S' or option[0] == 's':
            print("\nPlayer stands with: {p_card1} {p_card2} = {score}".format(\
                p_card1=hand.cards[0], p_card2=hand.cards[1], score=hand.value))
            print("\n")
            is_playing = False
        else:
            print("\nInvalid input. Would you like to (H)it or (S)tand?", end=' ')

    def dealer_hit(deck, dealer):
        dealer.draw_card(deck.deal())
        dealer.ace_value()

    def display_partial(player, dealer):
        print("\nDealer has: {d_card1} ? = ?".format(d_card1=dealer.cards[0]))           
        print("Player has: {p_card1} {p_card2} = {score}".format(\
            p_card1=player.cards[0], p_card2=player.cards[1], score=player.value))           

    def display_all(player, dealer):
        print("\nDealer has: {d_card1} {d_card2} = {score}".format(\
            d_card1=dealer.cards[0], d_card2=dealer.cards[1], score=dealer.value))      
        print("Player has: {p_card1} {p_card2} = {score}".format(\
            p_card1=player.cards[0], p_card2=player.cards[1], score=player.value)) 

    def check_valid_game(player, dealer):
        if player.value < 21 and dealer.value < 21:
            return True
        else:
            return False

    def check_winner(player, dealer):
        if dealer.value > 21:
            Blackjack.dealer_busts(player, dealer)
        elif dealer.value == 21:
            Blackjack.dealer_wins(player, dealer, True)
        elif dealer.value > player.value:
            Blackjack.dealer_wins(player, dealer, False)
        elif dealer.value < player.value and player.value < 21:
            Blackjack.player_wins(player, dealer, False)
        elif dealer.value == player.value:
            Blackjack.tie()
    
    def tie():
        print("Tie")
        exit(0)

    def player_wins(player, dealer, blackjack):
        if blackjack:
            print("Player wins!")
            print("Blackjack!")
        else:
            print("Player wins!")
            s = ''
            for i in range(len(player.cards)):
                s += str(player.cards[i])
                s += ' '
            s = s + '= ' + str(player.value) + " to Dealer's "
            for j in range(len(dealer.cards)):
                s += str(dealer.cards[j])
                s += ' '
            s = s + '= ' + str(dealer.value)
            print(s)
        exit(0)

    def player_busts(player):
        print("\nPlayer has: {p_card1} {p_card2} {p_card3} = {score}".format(\
            p_card1=player.cards[0],p_card2=player.cards[1], p_card3=player.cards[2],\
            score=player.value)) 
        print("Player busts with {score}".format(score=player.value))
        print("Dealer wins")
        exit(0)
    
    def dealer_wins(player, dealer, blackjack):
        if blackjack:
            print("\nDealer wins!")
            print("Blackjack!")
        else:
            print("\nDealer wins!")
            s = ''
            for i in range(len(dealer.cards)):
                s += str(dealer.cards[i])
                s += ' '
            s = s + '= ' + str(dealer.value) + " to Player's "
            for j in range(len(player.cards)):
                s += str(player.cards[j])
                s += ' '
            s = s + '= ' + str(player.value)
            print(s)
        exit(0)

    def dealer_busts(player, dealer):
        print("\nDealer has: {d_card1} {d_card2} {d_card3} = {score}".format(\
            d_card1=dealer.cards[0], d_card2=dealer.cards[1], d_card3=dealer.cards[2],\
            score=dealer.value)) 
        print("Dealer busts with {score}".format(score=dealer.value))
        print("Player wins")
        exit(0)

def main():
    global valid_game
    while True:
        print("-------------------------------------")
        print("       WELCOME TO BLACKJACK!         ")
        print("-------------------------------------")

        # Create and shuffle the deck, deal two initial cards to each player.
        deck = Deck()
        deck.shuffle()
        
        player = Hand()
        player.draw_card(deck.deal())
        player.draw_card(deck.deal())

        dealer = Hand()
        dealer.draw_card(deck.deal())
        dealer.draw_card(deck.deal())

        # Display initial hands (hiding Dealer's second card and score).
        Blackjack.display_partial(player, dealer)

        # Player continues to play the card until Player has stood, won (score==21), or busted.
        while is_playing and valid_game:
            # Promp Player to choose Hit or Stand playing options.
            Blackjack.hit_or_stand(deck, player, dealer)

            # If Player chooses Hit 
            if is_playing:
                if player.value == 21:
                    Blackjack.player_wins(player, dealer, True)
                if player.value > 21:
                    Blackjack.player_busts(player)

        # If Player chooses Stand and hasn't busted or won, Dealer plays
        while dealer.value < 17:
            s = 'Dealer has: '
            for i in range(len(dealer.cards)):
                s += str(dealer.cards[i])
                s += ' '
            print(s)
            if dealer.value >= 17:
                print("Dealer stands")
                print("\n")
                break
            else:
                Blackjack.dealer_hit(deck, dealer)
                print("Dealer hits")
            valid_game = Blackjack.check_valid_game(player, dealer)
            if not valid_game:
                Blackjack.check_winner(player, dealer)
            
        Blackjack.check_winner(player, dealer)

if __name__ == '__main__':
    main()