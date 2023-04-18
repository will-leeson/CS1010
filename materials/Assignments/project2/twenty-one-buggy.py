import random
import time

def make_deck():
    random.seed(time.time_ns())
    deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
    shoe = deck*4

    random.shuffle(shoe)
    return shoe

def deal_card(shoe):
    card = shoe.pop()

    return card

def parse_response(question):  
    should_play = None
    while should_play is None:   
        response = input(question)
        if response == 'y':
            should_play = True
        elif response == 'n':
            should_play = False
        else:
            print("You need to respond with y or n. Try again!")

    return should_play

def get_hand_score(hand):
    score = 0

    for card in hand:
        if card == 'J' or card == 'Q' or hand == 'K':
            score+=10
        elif card == 'A':
            score+=11
        else:
            score+=int(card)

    return score

def get_score(human_hand, dealer_hand):
    human_hand_score = get_hand_score(human_hand)
    dealer_hand_score = get_hand_score(dealer_hand)

    print()
    print("Your hand:", human_hand)
    print("Your score:", human_hand_score)
    if human_hand_score > 21:
        print("You busted :(")
        score = -1
    else:
        print("Dealer hand:", dealer_hand)
        print("Dealer score", dealer_hand_score)
        if human_hand_score > 21:
            print("You busted :(")
            score = -1
        elif dealer_hand_score > 21:
            print("The dealer busted, you won!")
            score = 1
        elif human_hand_score > dealer_hand_score:
            print("You beat the dealer!")
            score = 1
        elif human_hand_score < dealer_hand_score:
            print("The dealer beat you.")
            score = -1
        else:
            print("You tied.")
            score = 0
    
    return score

def play_hand(shoe):
    human_hand = []
    dealer_hand = []

    human_hand.append(deal_card(shoe))
    dealer_hand.append(deal_card(shoe))
    human_hand.append(deal_card(shoe))
    dealer_hand.append(deal_card(shoe))
    print("The dealer is showing", dealer_hand[0])
    human_hand_score = get_hand_score(human_hand)
    dealer_hand_score = get_hand_score(dealer_hand)

    should_deal = True
    score = 0
    while should_deal:
        print("Your hand is ", human_hand)
        should_deal = parse_response("Would you like another card [y/n]: ")

        if should_deal:
            card = deal_card(shoe)
            print("You got a", card)
            human_hand.append(card)
        
        human_hand_score = get_hand_score(human_hand)

        if human_hand_score > 21:
            should_deal = False

    while dealer_hand_score < 16:
        card = deal_card(shoe)
        print("The dealer got a", card)
        dealer_hand.append(card)
        dealer_hand_score = get_hand_score(dealer_hand)

    score = get_score(human_hand, dealer_hand)

    return score
    
def main():
    print("Welcome to 21. The goal of the game is to get ")
    print("as close to 21 as possible without going over.")
    print("Number cards are worth face value, J,Q, and K ")
    print("are worth 10, and A is worth 11. You need")
    print("to get closer to 21 than me (the dealer) without")
    print("busting (going over 21). You get a point each")
    print("time you beat me, 2 points when you get 21. If")
    print("we tie, no points awarded, if I win you lose a")
    print("point. Good luck!")
    print()

    should_play = True
    score = 0

    THE_SHOE = make_deck()
    while should_play:
        score += play_hand(THE_SHOE)
        print()
        print("Your score is", score)

        should_play = parse_response("Would you like to play another hand [y/n]: ")

main()
