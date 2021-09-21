# Blackjack_Commandline_Game
## Running the Program
Run `python3 blackjack.py`

## Assumptions
* Rule 4.2: "Dealer keeps hitting until score >= 17." I peeked the last element on the deck (this would be the card that is going to be added to the hand if Dealer hits) and checked whether adding it to the current hand would result in a score that is >= 17. If this is the case, Dealer will stand. However, in real life, I'm not sure whether this peeking behavior is allowed. 
* Update: I reverted this assumtion to a simpler algorithm for checking whether Dealer has to keep hitting. I simply checked if the current score is >= 17 instead of letting the Dealer to peak the card in the deck. 

## What you did well on this project
* I have used OOP to design the program. In this way, I'm able to separate different aspects of the game into classes such as Deck and Hand behaviors as well as Blackjack game rules. I clearly documented the behaviors of the functions and named the variables in readable and understandable ways. I managed to keep each function short, so I can do unit testing easily as I develop the program. 

## Design
* Since Ace can represent both 1 and 11, I set the default value for Ace as 11. This is because we only need to check once to see whether 11 works in the current hand collection. Since 11 is added to the total score once the Ace card is drawn, we only need to see whether the current score leads to burst. If this is the case, we can simply change it to a 1 by subtracting 10. On the other hand, we will need to add 11 to the total score and check busts. 
* I used the global variable `is_playing` to represent whether Player has chosen stand. If so, this triggers the Dealer to repeatedly make decisions on hit or stand.

## Tradeoffs
* If given more time, I would find a more efficient method to display the status of the hands of Dealer and Player after each action. In some places, I used a for loop to join the string repeatedly, which is really slow and inefficient. The maximum number of cards would never exceeds 52, so using a for loop to join strings would not cause too much trouble in this context. 
* If I have more time, I would definitely write more unit tests and integration test to test out my code. Due to time constraint, I only tested my program manually on the terminal. 