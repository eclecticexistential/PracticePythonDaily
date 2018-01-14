import random


def db(x):
    # has two win condition cards, two evolving wilds, 7 of one color, 8 of another, and 21 creature/spells
    if x == 3:
        non_evo_wilds_3M = [42, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 42]
        evo_wilds_3M = [42, 10, 10, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 42]
        return status(evo_wilds_3M,non_evo_wilds_3M,3)
    elif x == 2:
        non_evo_wilds_2M = [42, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 42]
        evo_wilds_2M = [42, 10, 10, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 42]
        return status(evo_wilds_2M, non_evo_wilds_2M,2)

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
    try:
        a = random.choice(deck)
    except IndexError:
        return 1
    deck.remove(a)
    hand.append(a)
    return [deck,hand]

def hands(x):
    random.shuffle(x)
    # mixes up deck
    hand, deck, lands_on_field = open_hand(x)
    #gets opening hand of 7 cards, removes them from deck, creates field variable: an array
    return hand,deck,lands_on_field

def hand_check(hand):
    #discards a 1 to take into account creatures/spells that are played during each round
    if len(hand) > 7:
        for cards in hand:
            if cards == 1:
                hand.remove(cards)
                break

def play_land(mana, deck, hand, field):
    evo_used = 0
    for card in hand:
        #takes care of evolving wilds
        if card == 10:
            hand.remove(card)
            color2 = 0
            color3 = 0
            color4 = 0
            #checks to see which land is needed
            for lands in field:
                if lands == 2:
                    color2 += 1
                elif lands == 3:
                    color3 += 1
                elif lands == 4:
                    color4 += 1
            for cards in deck:
                #puts basic on the field
                if cards == 2:
                    if color2 > color3:
                        pass
                    elif mana == 3 and color2 > color4:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        evo_used += 1
                elif cards == 3:
                    if color3 > color2:
                        pass
                    elif mana == 3 and color3 > color4:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        evo_used += 1
                elif cards == 4:
                    if color4 > color2:
                        pass
                    elif color4 > color3:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        evo_used += 1
                elif evo_used == 1:
                    return 1

        #plays land otherwise
        elif card == 2 or card == 3 or card == 4:
            field.append(card)
            hand.remove(card)
            return 0


def check_field(hand,field):
    num2s = 0
    num3s = 0
    num4s = 0
    #counts the lands to see if an adequate amount of land is available to cast 'win condition' cards: 42
    for card in field:
        if card == 2:
            num2s += 1
        elif card == 3:
            num3s += 1
        elif card == 4:
            num4s += 1
    #8 mana total to cast "win condition" cards
    if num2s >= 4 and num3s >= 4 and num4s == 0:
        for cards in hand:
            if cards == 42:
                return "Winner!"
            else:
                break
    elif num2s >= 2 and num3s >= 2 and num4s >= 2:
        for cards in hand:
            if cards == 42:
                return "Winner!"
            else:
                break
    manas = [num2s, num3s, num4s]
    return manas


def turn(hand, deck, field, mana):
    z = remove_card_from_deck(deck, hand)
    a = play_land(mana, deck, hand, field)
    print(a)
    hand_check(hand)
    if a == 1 or z == 1:
        return hand, deck, field, mana, a
    else:
        return hand, deck, field, mana


def check_snap_shot(x,field):
    mana_stuck = 0
    for x,y in zip(x,x[1:]):
        if x == y:
            mana_stuck += 1
    if mana_stuck > 3 and len(field) < 4:
        return 0


def status(deck1, deck2, mana):
    p1_hand, p1_deck, p1_field = hands(deck1)
    p2_hand, p2_deck, p2_field = hands(deck2)

    p1_turns = 0
    p2_turns = 0
    p1_snap_shot = []
    p2_snap_shot = []
    #taking turns
    while True:
        c = turn(p1_hand, p1_deck, p1_field, mana)
        if len(c) == 5:
            p1_turns += 1
        p1_status = check_field(p1_hand, p1_field)
        if p1_status == "Winner!":
            stats = ["P1", p1_turns]
            return stats
            break
        elif p1_status != "Winner!":
            p1_snap_shot.append(p1_status)
            a = check_snap_shot(p1_snap_shot, p1_field)
            if a == 0:
                stats = ["P2", p2_turns]
                return stats
                break
        turn(p2_hand, p2_deck, p2_field, mana)
        p2_status = check_field(p2_hand, p2_field)
        if p2_status == "Winner!":
            stats = ["P2",p2_turns]
            return stats
            break
        elif p2_status != "Winner!":
            p2_snap_shot.append(p2_status)
            b = check_snap_shot(p2_snap_shot,p2_field)
            if b == 0:
                stats = ["P1", p1_turns]
                return stats
                break
        p1_turns += 1
        p2_turns += 1


def out_of_all_games(mana):
    evo_wilds_wins = 0
    non_evo_wins = 0
    ties = 0
    evo_draw_steps = []
    non_evo_wins_steps = []
    games = 100
    while games > 0:
        winner, turns = db(mana)
        #appends num of draws into win condition if player won
        if winner == "P1":
            evo_draw_steps.append(turns)
        elif winner == "P2":
            non_evo_wins_steps.append(turns)
        #counts the number of times a deck one over the other
        if len(evo_draw_steps) > len(non_evo_wins_steps):
            evo_wilds_wins += 1
        elif len(evo_draw_steps) < len(non_evo_wins_steps):
            non_evo_wins += 1
        else:
            ties += 1
        games -= 1
    print()
    print("Stats for {} Mana Limited Deck \n".format(mana))
    print("Evo Deck Wins {}".format(evo_wilds_wins))
    print("Non Evo Deck Wins {}".format(non_evo_wins))
    print("Ties to Win {}".format(ties))
    print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(evo_draw_steps)/len(evo_draw_steps)))
    print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(non_evo_wins_steps)/len(non_evo_wins_steps)))


out_of_all_games(2)
out_of_all_games(3)

#display creatures ... 4 on field == win condition
#have card to remove 42 from deck
#two or more creatures on one field vs the other

#magic api starcity,tcg for data sets
#tcg life duration price of card