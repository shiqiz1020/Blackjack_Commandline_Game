# Blackjack_Commandline_Game
## Running the Program
Run `python3 blackjack.py`

## Game Overview
1. Deal initial cards(two cards to each player)
2. Display initial hands(hiding dealer's second card and score) 
3. Prompt user(Hit or Stand?)
    * Hit: add card to hand (check if busted)
    * Stand: end turn
    * Show updated hand and value
    * Repeat until player has stood, won (score == 21), or busted (score > 21)
4. Dealer plays(if player has neither busted nor won) print dealer's full hand, score dealer keeps hitting until score >= 17
5. Decide and report the winner,including hands and scores where relevant
