""" BlackJack Game

    Useful Keybindings:
    ctrl+/ : comment code
    shift+tab: down one indentation
"""
import random

oneSuit = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
fourSuits= oneSuit * 4
current_deck = fourSuits

players_hand = []
players_values = [0 ,0 ,0]

dealers_hand = []
dealers_values = [0, 0, 0]

# Shuffle the deck, player takes their cards, check for blackjack, hitOrStay prompt,

def deal(num, hand):
    """ This function deals n number of cards to the hand.

    The current_deck is shuffled once.
    Then last card in the deck is removed and placed into the hand n times.
    """

    def shuffle_cards(deck):
        """Randomly shuffle the current deck """
        random.shuffle(deck)

    def random_card(deck):
        """ Remove card """
        return deck.pop()

    def add_card_to_hand(hand):
        """ Uses two functions, shuffle_cards && random_card, and adds card to hand. """
        shuffle_cards(current_deck)
        return hand.append(random_card(current_deck))

    for _ in range(num):
        add_card_to_hand(hand)

def evaluate_hand(hand, values):
    """ Get the Value of your hand, OR hard_value && soft_value if you have an Ace. """

    def ace_check(hand):
        return "A" in hand

    if ace_check(hand) is False:
        values[0] = sum(hand)
        print("Hand:", hand)
        print("Value:",  values[0])
    else: #list comprehension
        #hardvalue
        arr1 = list(hand)
        values[1] = sum([1 if (x=="A") else x for x in arr1])
        print("Hard Value:", values[1])
        #softvalue
        arr2 = list(hand)
        arr2[arr2.index("A")] = 11
        values[2] = sum([1 if (x=="A") else x for x in arr2])
        print("Soft Value:", values[2])
        print("Hand:", hand)

def blackjack_check(values, hand):
    """check if BLackjack, Bust, or Hit_or_stay"""
    def hit_or_stay():
        print("Hit or Stay?")
        response = ""
        while response.lower() not in {"hit", "stay"}:
            response = input("Please enter hit or stay: ")
        print("You chose:",response.lower())
        if response.lower() == "hit":
            deal(1, hand)
            evaluate_hand(hand, values)
            blackjack_check(values, hand)
        else:
            print("Playing dealers cards...")
            play_dealers_cards(dealers_hand, dealers_values)
            #play dealers cards
            #compare values

    if 21 in values:
        print("BlackJack! You win")
    elif ( values[0] > 21) or (values[1] > 21) :
        print("Bust! You lose")
    else:
        hit_or_stay()

def play_dealers_cards(hand, values):
    """This function comes after choosing stay.

    The dealers hand is rolled and evaluated.
    Then highest values between player and dealer are compared.  """
    def compare_values():
        """Filter out values above 21, then select highest value for both player and dealer.

        Then compare these values."""
        players_result = max(list(filter(lambda x: x < 22, players_values)))
        dealers_result = max(list(filter(lambda x: x < 22, dealers_values)))
        if players_result == dealers_result:
            print("Draw! Both player and dealer has same values")
        elif players_result > dealers_result:
            print("Player Wins!")
        elif players_result < dealers_result:
            print("Dealer Wins!")
        else:
            print("Error - Unknown winner")

    deal(2, hand)
    evaluate_hand(hand, values)
    while max(values) < 17:              #(values[0] < 17) and (values[1] < 17):
        print("Dealer has less than 17. He takes another card...")
        deal(1, hand)
        evaluate_hand(hand, values)
    print("Dealers Hand:", hand)
    if (values[0] > 21) or (values[1] > 21):
        print("Dealers Bust! You win")
    else:# compare values
        compare_values()


deal(2, players_hand)
evaluate_hand(players_hand, players_values)
blackjack_check(players_values, players_hand)
