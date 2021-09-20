import random

values = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, \
    'J': 10, 'Q': 10, 'K':10, 'A': 11}

# Whether the game is active (not in stand).
playing = True
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
        # self.deck = [[card for card in values.keys()] for _ in range(4)]

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
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Blackjack:
    def player_hit(deck, hand, dealer):
        hand.draw_card(deck.deal())
        hand.ace_value()

    def hit_or_stand(deck, hand, dealer):
        global playing

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
            playing = False
        else:
            print("\nInvalid input. Would you like to (H)it or (S)tand?", end=' ')

    def dealer_hit(deck, player, dealer):
        s = 'Dealer has: '
        for i in range(len(dealer.cards)):
            s += str(dealer.cards[i])
            s += ' '
        print(s)
        dealer.draw_card(deck.deal())
        dealer.ace_value()

    def display_partial(player, dealer):
        print("\nDealer has: {d_card1} ? = ?".format(d_card1=dealer.cards[0]))           
        print("Player has: {p_card1} {p_card2} = {score}".format(p_card1=player.cards[0], \
            p_card2=player.cards[1], score=player.value))           

    def display_all(player, dealer):
        print("\nDealer has: {d_card1} {d_card2} = {score}".format(d_card1=dealer.cards[0], \
            d_card2=dealer.cards[1], score=dealer.value))      
        print("Player has: {p_card1} {p_card2} = {score}".format(p_card1=player.cards[0], \
            p_card2=player.cards[1], score=player.value)) 
        # add dealer hits ...

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
        print("\nTie")
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

    def player_busts(player, dealer):
        print("\nPlayer has: {p_card1} {p_card2} {p_card3} = {score}".format(p_card1=player.cards[0], \
            p_card2=player.cards[1], p_card3=player.cards[2], score=player.value)) 
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
        print("\nDealer has: {d_card1} {d_card2} {d_card3} = {score}".format(d_card1=dealer.cards[0], \
            d_card2=dealer.cards[1], d_card3=dealer.cards[2], score=dealer.value)) 
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
        while playing and valid_game:
            # Promp Player to choose Hit or Stand playing options.
            Blackjack.hit_or_stand(deck, player, dealer)

            if playing:
                if player.value == 21:
                    Blackjack.player_wins(player, dealer, True)
                if player.value > 21:
                    Blackjack.player_busts(player, dealer)

        # If Player hasn't busted or won, Dealer plays
        while dealer.value < 17:
            Blackjack.dealer_hit(deck, player, dealer)
            print(deck.deck[-1])
            if dealer.value + values[deck.deck[-1]] >= 17:
                print("Dealer stands")
                print("\n")
                break
            else:
                print("Dealer hits")
            valid_game = Blackjack.check_valid_game(player, dealer)
            if not valid_game:
                Blackjack.check_winner(player, dealer)
            
        Blackjack.check_winner(player, dealer)


if __name__ == '__main__':
    main()