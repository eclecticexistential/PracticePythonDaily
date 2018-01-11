import random

def open_hand(x):
    counter = 7
    hand = []
    lands_on_field = []
    while counter > 0:
        a = random.choice(x)
        x.remove(a)
        hand.append(a)
        counter -= 1
    data = [hand, x, lands_on_field]
    return data

def remove_card_from_deck(deck,hand):
    a = random.choice(deck)
    deck.remove(a)
    hand.append(a)
    return [deck,hand]

def hands():
    non_evo_wilds = [42, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    evo_wilds = [42, 10, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    random.shuffle(evo_wilds)
    random.shuffle(non_evo_wilds)
    # mixes up deck
    player1 = open_hand(evo_wilds)
    player2 = open_hand(non_evo_wilds)
    data = [player1[0],player1[1],player1[2],player2[0],player2[1],player2[2]]
    return data

def hand_check(hand):
    if len(hand) > 7:
        for cards in hand:
            if cards == 1:
                hand.remove(cards)
                break

def play_land(deck,hand,field):
    for card in hand:
        #takes care of evolving wilds
        if card == 10:
            hand.remove(card)
            color2 = 0
            color3 = 0
            for lands in field:
                if lands == 2:
                    color2+= 1
                elif lands == 3:
                    color3+= 1
            for cards in deck:
                #puts basic on the field
                if color2 > color3:
                    if cards == 3:
                        field.append(cards)
                        deck.remove(cards)
                        return
                elif color3 > color2:
                    if cards == 2:
                        field.append(cards)
                        deck.remove(cards)
                        return
                elif cards == 2 or cards == 3:
                    field.append(cards)
                    deck.remove(cards)
                    return
        #plays land otherwise
        elif card == 2 or card == 3:
            field.append(card)
            hand.remove(card)
            return

def check_field(hand,field):
    num2s = 0
    num3s = 0
    for card in field:
        if card == 2:
            num2s += 1
        elif card == 3:
            num3s += 1
    if num2s >= 3 and num3s >= 3:
        for cards in hand:
            if cards == 42:
                return "Winner!"


def turn(hand, deck=None,field=None):
    counter = 0
    wins = 0
    while len(deck) > 0:
        remove_card_from_deck(deck,hand)
        play_land(deck,hand,field)
        hand_check(hand)
        game_over = check_field(hand,field)
        if game_over == "Winner!":
            wins += 1
            break
        counter += 1
    return counter

def status():
    data_set = hands()
    #unpacking player 1 stats
    p1_hand = data_set[0]
    p1_deck = data_set[1]
    p1_field = data_set[2]
    #taking turn
    totals_for_p1 = turn(p1_hand, deck=p1_deck,field=p1_field)
    #unpacking player 2 stats
    p2_hand = data_set[3]
    p2_deck = data_set[4]
    p2_field = data_set[5]
    #taking turn
    totals_for_p2 = turn(p2_hand,deck=p2_deck,field=p2_field)
    stats = [totals_for_p1,totals_for_p2]
    return stats


def out_of_all_games():
    evo_wilds_wins = 0
    non_evo_wins = 0
    ties = 0
    evo_draw_steps = []
    non_evo_wins_steps = []
    games = 10000
    while games > 0:
        a = status()
        evo_draw_steps.append(a[0])
        non_evo_wins_steps.append(a[1])
        if a[0] > a[1]:
            evo_wilds_wins += 1
        elif a[0] < a[1]:
            non_evo_wins += 1
        else:
            ties += 1
        games -= 1
    print("Evo wins {}".format(evo_wilds_wins))
    print("Non Evo wins {}".format(non_evo_wins))
    print("Ties {}\n".format(ties))
    print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(evo_draw_steps)/len(evo_draw_steps)))
    print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(non_evo_wins_steps)/len(non_evo_wins_steps)))


out_of_all_games()