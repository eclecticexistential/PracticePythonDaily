import random


def db(x):
    # has two win condition cards, two evolving wilds, 7 of one color, 8 of another, and 21 creature/spells
    if x == 3:
        non_evo_wilds_3M = [42, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        evo_wilds_3M = [42, 10, 10, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        return status(evo_wilds_3M,non_evo_wilds_3M,3)
    elif x == 2:
        non_evo_wilds_2M = [42, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        evo_wilds_2M = [42, 10, 10, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        return status(evo_wilds_2M, non_evo_wilds_2M,2)

def open_hand(x):
    #make mulligan function
    counter = 7
    hand = []
    lands_on_field = []
    graveyard = []
    while counter > 0:
        a = random.choice(x)
        x.remove(a)
        hand.append(a)
        counter -= 1
    data = [hand, x, lands_on_field, graveyard]
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
    hand, deck, lands_on_field, graveyard = open_hand(x)
    #gets opening hand of 7 cards, removes them from deck, creates field variable: an array
    return hand,deck,lands_on_field, graveyard

def hand_check(hand,graveyard):
    #discards a 1 to take into account creatures/spells that are played during each round
    if len(hand) > 7:
        for cards in hand:
            if cards == 1 or cards == 8:
                hand.remove(cards)
                graveyard.append(cards)
                break

def play_land(mana, deck, hand, field, graveyard):
    mana_one = 0
    mana_two = 0
    mana_three = 0
    for counter in hand:
        if counter == 2:
            mana_one += 1
        elif counter == 3:
            mana_two += 1
        elif counter == 4:
            mana_three += 1

    has_evo = 0
    color2 = 0
    color3 = 0
    color4 = 0
    # checks to see which land is needed
    for lands in field:
        if lands == 2: color2 += 1
        elif lands == 3: color3 += 1
        elif lands == 4: color4 += 1
    for card in hand:
        if card == 10:
            has_evo += 1
            graveyard.append(card)
            hand.remove(card)
            for cards in deck:
                # puts basic on the field
                if cards == 2:
                    if color2 > color3:
                        pass
                    elif mana == 3 and color2 > color4:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        print("Evo used for 2.")
                        return 1
                elif cards == 3:
                    if color3 > color2:
                        pass
                    elif mana == 3 and color3 > color4:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        print("Evo used for 3.")
                        return 1
                elif cards == 4:
                    if color4 > color2:
                        pass
                    elif color4 > color3:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        print("Evo used for 4.")
                        return 1
    if has_evo != 1:
            # plays land otherwise
        for card in hand:
            if mana == 2:
                if card == 2 and color2 <= color3:
                    field.append(card)
                    hand.remove(card)
                    return 0
                if card == 3 and color3 <= color2:
                    field.append(card)
                    hand.remove(card)
                    return 0
                else:
                    if card == 2:
                        if color3 != 0:
                            field.append(card)
                            hand.remove(card)
                            return 0
                    elif card == 3:
                        if color2 != 0:
                            field.append(card)
                            hand.remove(card)
                            return 0
            elif mana == 3:
                if card == 2:
                    if color2 <= color3 and color2 <= color4:
                        field.append(card)
                        hand.remove(card)
                        return 0
                if card == 3:
                    if color3 <= color2 and color3 <= color4:
                        field.append(card)
                        hand.remove(card)
                        return 0
                if card == 4:
                    if color4 <= color2 and color4 <= color3:
                        field.append(card)
                        hand.remove(card)
                        return 0
                else:
                    if card == 2 and mana_two == 0 and mana_three == 0:
                        field.append(card)
                        hand.remove(card)
                        return 0
                    elif card == 3 and mana_one == 0 and mana_three == 0:
                        field.append(card)
                        hand.remove(card)
                        return 0
                    elif card == 4 and mana_one == 0 and mana_two == 0:
                        field.append(card)
                        hand.remove(card)
                        return 0


def check_field(hand, field, mana):
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
    for cards in hand:
        if mana == 2:
            if num2s >= 3 and num3s >= 3:
                if cards == 42:
                    hand.remove(cards)
                    field.append(cards)
                    break
            if num2s >= 1 and num3s >= 1:
                if cards == 8:
                    hand.remove(cards)
                    field.append(cards)
                    break
        elif mana == 3:
            if num2s >= 2 and num3s >= 2 and num4s >= 2:
                if cards == 42:
                    hand.remove(cards)
                    field.append(cards)
                    break
            if num2s >= 1 and num3s >= 1 and num4s >= 1:
                if cards == 8:
                    hand.remove(cards)
                    field.append(cards)
                    break
    manas = [num2s, num3s, num4s]
    return manas

def check_creatures(battlefield):
    damage = 0
    for card in battlefield:
        if card == 8:
            damage += 1
        elif card == 42:
            damage += 5
    return damage

def removal(hand, lands, field, p1_graveyard, p2_graveyard, p1_deck = None, p2_deck = None):
    available_land = 0
    for land in lands:
        if land == 2 or land == 3 or land == 4:
            available_land += 1
    if p1_deck == None:
        deck = p2_deck
    elif p2_deck == None:
        deck = p1_deck
    for cards in hand:
        if cards == 33:
            if available_land > 2:
                for card in field:
                    if card == 42:
                        field.remove(card)
                        hand.remove(cards)
                        if deck == p2_deck:
                            p2_graveyard.append(card)
                            p1_graveyard.append(cards)
                        elif deck == p1_deck:
                            p1_graveyard.append(card)
                            p2_graveyard.append(cards)
                        print("42 was removed")
                        return deck,hand,field
                        break


def turn(hand, deck, field, graveyard, mana):
    remove_card_from_deck(deck, hand)
    play_land(mana, deck, hand, field, graveyard)
    c = check_field(hand, field, mana)
    hand_check(hand,graveyard)
    return hand, deck, field, c


def check_snap_shot(x,field):
    mana_stuck = 0
    for x,y in zip(x,x[1:]):
        if x == y:
            mana_stuck += 1
    if mana_stuck > 3 and len(field) <= 4:
        return 0

def define_winner():
    pass

def status(deck1, deck2, mana):
    p1_hand, p1_deck, p1_field, p1_graveyard= hands(deck1)
    p2_hand, p2_deck, p2_field, p2_graveyard = hands(deck2)

    p1_turns = 0
    p2_turns = 0
    p1_snap_shot = []
    p2_snap_shot = []
    p1_life_total = 20
    p2_life_total = 20
    #taking turns
    while True:
        print()
        print("P1_turns {}, P2_turns {}".format(p1_turns,p2_turns))
        print("Player One Field {} Cards in hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_graveyard, p1_life_total))
        print("Player Two Field {} Cards in hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_graveyard, p2_life_total))
        removal(p1_hand,p1_field, p2_field,p1_graveyard,p2_graveyard, p2_deck=p2_deck)
        p1_status = turn(p1_hand, p1_deck, p1_field, p1_graveyard, mana)
        #snap shot checks for mana starvation
        p1_snap_shot.append(p1_status[3])
        a = check_snap_shot(p1_snap_shot, p1_field)
        if a == 0:
            stats = ["P2", p2_turns]
            return stats

        removal(p2_hand, p2_field, p1_field, p1_graveyard, p2_graveyard, p1_deck=p1_deck)
        p2_status = turn(p2_hand, p2_deck, p2_field, p2_graveyard, mana)
        p2_snap_shot.append(p2_status[3])
        # snap shot checks for mana starvation
        b = check_snap_shot(p2_snap_shot,p2_field)
        if b == 0:
            stats = ["P1", p1_turns]
            return stats

        p1_creatures = check_creatures(p1_field)
        p2_creatures = check_creatures(p2_field)


        if p1_creatures > p2_creatures:
            damage = (p1_creatures - p2_creatures)+1
            p2_life_total -= damage
        elif p1_creatures < p2_creatures:
            damage = (p2_creatures - p1_creatures)+1
            p1_life_total -= damage

        if p1_life_total <= 0:
            stats = ["P2", p2_turns]
            return stats
            break
        elif p2_life_total <= 0:
            stats = ["P1", p1_turns]
            return stats
            break

        if len(p1_deck) == 0:
            stats = ["P2", p2_turns]
            return stats
        if len(p2_deck) == 0:
            stats = ["P1", p1_turns]
            return stats

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
            evo_wilds_wins += 1
            print("P1 wins")
        elif winner == "P2":
            non_evo_wins_steps.append(turns)
            non_evo_wins += 1
            print("P2 wins")
        games -= 1
    print()
    print("Stats for {} Mana Limited Deck \n".format(mana))
    print("Evo Deck Wins {}".format(evo_wilds_wins))
    print("Non Evo Deck Wins {}".format(non_evo_wins))
    print("Ties to Win {}".format(ties))
    print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(evo_draw_steps)/len(evo_draw_steps)))
    print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(non_evo_wins_steps)/len(non_evo_wins_steps)))


#out_of_all_games(2)
out_of_all_games(3)

#display creatures ... 4 on field == win condition
#have card to remove 42 from deck
#two or more creatures on one field vs the other

#magic api starcity,tcg for data sets
#tcg life duration price of card