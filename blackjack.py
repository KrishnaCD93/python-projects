# Card game, blackjack, using ASCII art
import random, sys

hearts = chr(9829)
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)
backside = 'backside'

def main():
    print('''Rules: Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')
    
    money = 5000
    while True: # main game loop
        if money <= 0:
            print("You're broke! Thanks for playing.")
            sys.exit()
        
        print('Money: ', money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        # player actions:
        print('Bet: ', bet)
        while True: # keep looping until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)

            if move == 'D': # double down
                additionalBet = getBet(min(bet, (money - bet)))
                bet  += additionalBet
                print(f'Bet increase to {bet}')
                print('Bet: ', bet)
            if move in ('H','D'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}.')
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21: # player bust
                    continue
            if move in ('S','D'): # end turn
                break
        # dealer actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('The dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21: # dealer bust
                    break
                input('Press enter to continue...')
                print('\n\n')
        #display hands:
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print(f'Dealer busts! You win ${bet}!')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print(f'You won ${bet}!')
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie, the bet is returned to you.")
        input('Press enter to continue...')
        print('\n\n')

def getBet(maxBet):
# Ask player how much they want to bet this round.
    while True:
        print(f'How much do you want to bet? (1 - {maxBet})')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not (bet.isdecimal() or bet.replace('.','',1).isdecimal()):
            continue
        bet = float(bet)
        if 0 < bet <= maxBet:
            return bet

def getDeck():
# Return a list of (rank, suit) tuples for all 52 cards.
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J','Q','K','A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
# Show the player's and dealer's cards. Hide dealer's first
# card if showDealerHand is False.
    print()
    if showDealerHand:
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        displayCards([backside] + dealerHand[1:])
    print('Player:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
# Returns the value of the cards.
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K','Q','J'):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value +=10
    return value

def displayCards(cards):
# Display all the cards in the cards list.
    rows = ['','','','','']
    for i, card in enumerate(cards):
        rows[0] += '__ '
        if card == backside:
            rows[1] = '|## | '
            rows[2] = '|###| '
            rows[3] = '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
        for row in rows:
            print(row)

def getMove(playerHand, money):
# Ask player for their move and return hit, stand or double.
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H','S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()