import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

'''
test_card = Card(ranks[3],suits[3])
print(test_card)

'''


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.deck.append(new_card)

    def __str__(self):
        for card_object in self.deck:
            print(card_object)
        return "----"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

'''

test_deck = Deck()
print(test_deck)

'''


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def __str__(self):
        for hand_object in self.cards:
            print(hand_object)
        return "---"

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        #count aces
        if card.rank == 'Ace':
            self.aces += 1


    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, last_total = 100):
        self.total = last_total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
        if self.total == 0:
            print("Player you have 0 chips left! Time to get a job, it looks like Vegas just isn't your calling :(")


def take_bet():
    while True:
        try:
            print(f"You have {chips.total} total chips.")
            chips.bet = int(input("\nWhat will be your bet player?"))
            if chips.bet > chips.total:
                print("That bet is more than your available chips; Try again.")
            else:
                print(f"Bet of {chips.bet} accepted.")
                break
        except ValueError:
            print("Please place an integer bet. Try again.")



def hit(deck, hand):
    hand.add_card(deck.deal())



def hit_or_stand(deck, hand):
    global playing   # to control an upcoming while loop
    while True:
        choice = input("Would you like to hit or stand? (h or s)")
        if choice[0].lower() == "h":
            hit(deck,player_hand)
        elif choice[0].lower() == "s":
            playing = False
        else:
            print("That wasn't a valid response, please try again")
            continue

        break



def show_some(player, dealer):
    print("\nOne of Dealer's Cards:")
    print(dealer[0].__str__())
    print("\nPlayer's Cards:")
    for card in player:
        print(card.__str__())

def show_all(player, dealer):
    print('\n++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("All of Dealer's cards:")
    for card_object in dealer:
        print(card_object.__str__())
    print("\nAll of Player's Cards:")
    for card_object in player:
        print(card_object.__str__())
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')

def player_busts():
    print("PLAYER BUSTS! YOU LOSE!")

def player_wins():
    print("You Win Player!! Congrats!")


def dealer_busts():
    print("Dealer Busts!")


def dealer_wins():
    print("Dealer Wins! Player loses")


def push():
    print("Dealer and Player Tie!")


round_count = 0

while True:
    # Print an opening statement
    print("Hello Player! Welcome to BlackJack")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()

    card_count = 0
    while card_count < 2:
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        player_hand.adjust_for_ace()
        dealer_hand.adjust_for_ace()
        card_count += 1


    # Set up the Player's chips


    # Prompt the Player for their bet
    if round_count == 0:
        # Set up the Player's chips
        chips = Chips()
        # Prompt the Player for their bet
        take_bet()
    else:
        chips = Chips(end_chip_total)
        take_bet()

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand.cards,dealer_hand.cards)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand.cards,dealer_hand.cards)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        player_hand.adjust_for_ace()
        if player_hand.value > 21:  #calculate value of player hand as well
            player_state = False
            playing = False
        else:
            player_state = True

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_state == True:
        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal())
            dealer_hand.adjust_for_ace()
    # Show all cards
    show_all(player_hand.cards,dealer_hand.cards)
    dealer_hand.adjust_for_ace()
    player_hand.adjust_for_ace()
    print(dealer_hand.value)
    print(player_hand.value)
    # Run different winning scenarios
    if dealer_hand.value > 21:
        dealer_busts()
        player_wins()
        chips.win_bet()
    elif player_state == False:
        player_busts()
        chips.lose_bet()
    elif dealer_hand.value > player_hand.value:
        dealer_wins()
        chips.lose_bet()
    elif player_hand.value> dealer_hand.value:
        player_wins()
        chips.win_bet()
    elif player_hand.value == dealer_hand.value:
        push()




    # Inform Player of their chips total
    end_chip_total = chips.total
    print(f"Player you have ended this round with {chips.total} chips")
    # Ask to play again
    game_end = False
    while True:
        result = input("Would you like to play again player? (y or n)")
        if result[0].lower() == 'y':
            playing = True
            game_end = False
            round_count += 1
            break
        elif result[0].lower() == 'n':
            playing = False
            game_end = True
            break
        else:
            print('That was not a valid response. Try again')
    if game_end:
        break
    else:
        continue


print("Thanks for playing!")
