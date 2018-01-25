import random


def db(x):
    # each has 23 playables: half creatures (two big'uns), half spells (one removal for big'un), and 17 lands
    # evo decks has two that replace lands
    # 42 = big creature, 2-4 mana, 8 = small creatures, 13 = direct damage, 33 = big creature removal, 9 = life gain
    # 66 = tutor
    if x == 3:
        non_evo_wilds_3m = [42, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 13, 9, 66, 1, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        evo_wilds_3m = [42, 10, 10, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 13, 9, 66, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        return status(evo_wilds_3m, non_evo_wilds_3m, 3)
    elif x == 2:
        non_evo_wilds_2m = [42, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 13, 9, 66, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        evo_wilds_2m = [42, 10, 10, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 13, 9, 66, 1, 1, 1, 1, 1, 1, 1, 33, 42]
        return status(evo_wilds_2m, non_evo_wilds_2m, 2)


def dice_roll():
    return random.randint(1, 20)


def mulligan(hand, mana, x):
    new_hand = []
    new_deck = x
    mana1 = 0
    mana2 = 0
    mana3 = 0
    evo = 0
    # checks hand for mana
    for card in hand:
        if card == 2:
            mana1 += 1
        elif card == 3:
            mana2 += 1
        elif card == 4:
            mana3 += 1
        elif card == 10:
            evo += 1
    if mana == 2:
        if mana1 == 0 or mana2 == 0:
            if evo != 0:
                pass
            else:
                total_draw = len(hand)-1
                for card in hand:
                    new_deck.append(card)
                    random.shuffle(new_deck)
                while total_draw > 0:
                    a = random.choice(new_deck)
                    new_deck.remove(a)
                    new_hand.append(a)
                    total_draw -= 1
                return new_hand, new_deck
    elif mana == 3:
        # checks hand for evo. if one present, check 2 mana sources for one of each
        if evo != 0:
            if mana1 != 0 and mana2 != 0:
                pass
            if mana2 != 0 and mana3 != 0:
                pass
            if mana1 != 0 and mana3 != 0:
                pass
            else:
                total_draw = len(hand)-1
                for card in hand:
                    new_deck.append(card)
                    random.shuffle(new_deck)
                while total_draw > 0:
                    a = random.choice(new_deck)
                    new_deck.remove(a)
                    new_hand.append(a)
                    total_draw -= 1
                return new_hand, new_deck
        elif mana1 == 0 or mana2 == 0 or mana3 == 0:
            total_draw = len(hand) - 1
            for card in hand:
                new_deck.append(card)
                random.shuffle(new_deck)
            while total_draw > 0:
                a = random.choice(new_deck)
                new_deck.remove(a)
                new_hand.append(a)
                total_draw -= 1
            return new_hand, new_deck
    else:
        return


def open_hand(deck, mana):
    # make mulligan function
    counter = 7
    hand = []
    lands_on_field = []
    graveyard = []
    die = dice_roll()
    while counter > 0:
        a = random.choice(deck)
        deck.remove(a)
        hand.append(a)
        counter -= 1
    # change here to alter allowed number to mulligan to
    while len(hand) > 3:
        hand_size = mulligan(hand, mana, deck)
        if hand_size is not None:
            hand = hand_size[0]
            deck = hand_size[1]
        else:
            break
    if len(hand) < 7:
        random.shuffle(deck)
    r1_stats = [hand, deck, lands_on_field, graveyard, die]
    return r1_stats


def look_for_mana(mana, deck, hand, field, graveyard, mana_stock):
    for card in hand:
        if card == 10:
            graveyard.append(card)
            hand.remove(card)
            for cards in deck:
                # puts basic on the field
                if cards == 2:
                    if mana_stock[3] < mana_stock[4] and mana_stock[0] < mana_stock[1]:
                        if mana == 2 or mana_stock[3] < mana_stock[5]:
                            field.append(cards)
                            deck.remove(cards)
                            random.shuffle(deck)
                            print("Evo used for 2.")
                            return
                elif cards == 3:
                    if mana_stock[4] < mana_stock[3] and mana_stock[1] < mana_stock[0]:
                        if mana == 2 or mana_stock[4] < mana_stock[5]:
                            field.append(cards)
                            deck.remove(cards)
                            random.shuffle(deck)
                            print("Evo used for 3.")
                            return
                elif cards == 4:
                    if mana_stock[2] < mana_stock[0] and mana_stock[2] < mana_stock[1]:
                        if mana_stock[5] < mana_stock[4] and mana_stock[5] < mana_stock[3]:
                            field.append(cards)
                            deck.remove(cards)
                            random.shuffle(deck)
                            print("Evo used for 4.")
                            return
                elif cards == 2 or cards == 3 or cards == 4:
                    field.append(cards)
                    deck.remove(cards)
                    random.shuffle(deck)
                    print("Evo used for {}".format(cards))
                    return


def play_land(mana, hand, field, mana_stock):
    for card in hand:
        if card == 2 and mana_stock[0] <= mana_stock[1]:
            if mana == 2 or mana_stock[0] <= mana_stock[2]:
                field.append(card)
                hand.remove(card)
                return
        elif card == 3 and mana_stock[1] <= mana_stock[0]:
            if mana == 2 or mana_stock[1] <= mana_stock[2]:
                field.append(card)
                hand.remove(card)
                return
        elif card == 4 and mana_stock[2] <= mana_stock[1] and mana_stock[2] <= mana_stock[0]:
            field.append(card)
            hand.remove(card)
            return
        elif card == 2 or card == 3 or card == 4:
            field.append(card)
            hand.remove(card)
            return


def check_land(mana, deck, hand, field, graveyard):
    mana_one = 0
    mana_two = 0
    mana_three = 0
    has_evo = 0
    # checks land in hand
    for counter in hand:
        if counter == 2:
            mana_one += 1
        elif counter == 3:
            mana_two += 1
        elif counter == 4:
            mana_three += 1
        elif counter == 10:
            has_evo += 1
    color2 = 0
    color3 = 0
    color4 = 0
    # checks to see which land is needed
    for lands in field:
        if lands == 2:
            color2 += 1
        elif lands == 3:
            color3 += 1
        elif lands == 4:
            color4 += 1
    if has_evo != 0:
        mana_stock = [mana_one, mana_two, mana_three, color2, color3, color4]
        look_for_mana(mana, deck, hand, field, graveyard, mana_stock)
        return check_field(hand, field, has_evo, mana)
    elif has_evo != 1:
        mana_stock = [color2, color3, color4]
        play_land(mana, hand, field, mana_stock)
        return check_field(hand, field, has_evo, mana)


def draw(deck, hand):
    a = random.choice(deck)
    deck.remove(a)
    hand.append(a)
    return [deck, hand]


def hand_check(hand, graveyard):
    # discards a 1 to take into account creatures/spells that are played during each round
    count = 0
    while len(hand) > 7:
        for cards in hand:
            count += 1
            if cards == 1:
                hand.remove(cards)
                graveyard.append(cards)
                break
            if count > 7:
                if cards == 8:
                    hand.remove(cards)
                    graveyard.append(cards)
                    break
                elif cards == 2 or cards == 3 or cards == 4:
                    hand.remove(cards)
                    graveyard.append(cards)
                    break


def check_field(hand, field, evo, mana):
    num2s = 0
    num3s = 0
    num4s = 0
    # counts the lands to see if an adequate amount of land is available to cast 'win condition' cards: 42
    for card in field:
        if card == 2:
            num2s += 1
        elif card == 3:
            num3s += 1
        elif card == 4:
            num4s += 1

    # gets available mana
    available_mana = [num2s, num3s, num4s]

    # 8 or 42 mana to cast creature cards
    for cards in hand:
        if mana == 2:
            # checks if evo was played to see if legal move can be made using mana on this turn
            if evo == 1:
                if num2s == 3 and num3s == 3:
                    pass
                if num2s == 1 and num3s == 1:
                    pass
            else:
                if num2s >= 3 and num3s >= 3:
                    if cards == 42:
                        hand.remove(cards)
                        field.append(cards)
                        available_mana[0] -= 3
                        available_mana[1] -= 3
                        break
                if num2s >= 1 and num3s >= 1:
                    if cards == 8:
                        hand.remove(cards)
                        field.append(cards)
                        available_mana[0] -= 1
                        available_mana[1] -= 1
                        break
        elif mana == 3:
            if evo != 1:
                if num2s >= 2 and num3s >= 2 and num4s >= 2:
                    if cards == 42:
                        hand.remove(cards)
                        field.append(cards)
                        available_mana[0] -= 2
                        available_mana[1] -= 2
                        available_mana[2] -= 2
                        break
                if num2s >= 1 and num3s >= 1 and num4s >= 1:
                    if cards == 8:
                        hand.remove(cards)
                        field.append(cards)
                        available_mana[0] -= 1
                        available_mana[1] -= 1
                        available_mana[2] -= 1
                        break
    manas = [num2s, num3s, num4s], available_mana
    return manas


def check_creatures(battlefield):
    damage = 0
    for card in battlefield:
        if card == 8:
            damage += 1
        elif card == 42:
            damage += 5
    return damage


def tutor(hand, deck, graveyard, untapped_mana, mana):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    for card in hand:
        if card == 66:
            hand.remove(card)
            graveyard.append(card)
            new_card1 = random.choice(deck)
            new_card2 = random.choice(deck)
            hand.append(new_card1)
            hand.append(new_card2)
            if mana == 2:
                untapped_mana[0] -= 1
                untapped_mana[1] -= 1
                print("tutored")
                return 2
            elif mana == 3:
                if land1 >= 1 and land2 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                elif land2 >= 1 and land3 >= 1:
                    untapped_mana[1] -= 1
                    untapped_mana[2] -= 1
                elif land3 >= 1 and land1 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[2] -= 1
                return 2


def direct_damage(hand, graveyard, untapped_mana, mana):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    for card in hand:
        if card == 13:
            if mana == 2:
                if land1 >= 1 and land2 >= 1:
                    graveyard.append(card)
                    hand.remove(card)
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                    return 3
            if mana == 3:
                if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                    graveyard.append(card)
                    hand.remove(card)
                    if land1 >= 1 and land2 >= 1:
                        untapped_mana[0] -= 1
                        untapped_mana[1] -= 1
                    elif land2 >= 1 and land3 >= 1:
                        untapped_mana[1] -= 1
                        untapped_mana[2] -= 1
                    elif land3 >= 1 and land1 >= 1:
                        untapped_mana[0] -= 1
                        untapped_mana[2] -= 1
                    return 3


def life_gain(hand, graveyard, untapped_mana, mana):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    for card in hand:
        if card == 9:
            hand.remove(card)
            graveyard.append(card)
            if mana == 2:
                untapped_mana[0] -= 1
                untapped_mana[1] -= 1
                return 5
            elif mana == 3:
                if land1 >= 1 and land2 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                elif land2 >= 1 and land3 >= 1:
                    untapped_mana[1] -= 1
                    untapped_mana[2] -= 1
                elif land3 >= 1 and land1 >= 1:
                    untapped_mana[0] -= 1
                    untapped_mana[2] -= 1
                return 5


def removal(hand, field, p1_graveyard, p2_graveyard, untapped_mana, mana, player):
    land1 = untapped_mana[0]
    land2 = untapped_mana[1]
    land3 = untapped_mana[2]
    for cards in hand:
        if cards == 33:
            for card in field:
                if card == 42:
                    field.remove(card)
                    hand.remove(cards)
                    if mana == 2:
                        untapped_mana[0] -= 1
                        untapped_mana[1] -= 1
                    elif mana == 3:
                        if land1 >= 1 and land2 >= 1:
                            untapped_mana[0] -= 1
                            untapped_mana[1] -= 1
                        elif land2 >= 1 and land3 >= 1:
                            untapped_mana[1] -= 1
                            untapped_mana[2] -= 1
                        elif land3 >= 1 and land1 >= 1:
                            untapped_mana[0] -= 1
                            untapped_mana[2] -= 1
                    # opposite player sent to establish who won scenarios...use to distinguish graveyards
                    if player == "P1":
                        p2_graveyard.append(card)
                        p1_graveyard.append(cards)
                    elif player == "P2":
                        p1_graveyard.append(card)
                        p2_graveyard.append(cards)
                    print("42 was removed")
                    return

def spells(av_mana, spell, mana):
    land1 = av_mana[0]
    land2 = av_mana[1]
    land3 = av_mana[2]
    if mana == 2 and land1 >= 1 and land2 >= 1:
        return spell
    elif mana == 3:
        if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
            return spell


def check_snap_shot(ss, field):
    mana_stuck = 0
    for x, y in zip(ss, ss[1:]):
        if x == y:
            mana_stuck += 1
        elif x == 0 and y == 0:
            mana_stuck += 1
    if mana_stuck > 3 and len(field) <= 4:
        print("Mana starved.")
        return 0


def upkeep(deck, hand, opp_turns, o_player, went_first):
    if len(deck) > 0 and went_first == 2:
        draw(deck, hand)
    elif len(deck) == 0:
        stats = [o_player, opp_turns]
        return stats


def main_phase(hand, deck, grave, life, opp_field, opp_grave, o_player, opp_life, av_mana, mana):
    spells(av_mana, removal(hand, opp_field, grave, opp_grave, av_mana, mana, o_player), mana)
    if life >= 3 and len(deck) > 2:
        self_inflict = spells(av_mana, tutor(hand, deck, grave, av_mana, mana), mana)
        if type(self_inflict) == int:
            life -= self_inflict
    damage = spells(av_mana, direct_damage(hand, grave, av_mana, mana), mana)
    if type(damage) == int:
        opp_life -= damage
    return


def combat_phase(field, opp_field, opp_life):
    # check creatures returns damage based on 8 or 42 (creature size)
    current_player = check_creatures(field)
    opp = check_creatures(opp_field)

    if current_player > opp:
        damage = (current_player - opp) + 1
        opp_life -= damage
        return opp_life


def main_phase2(av_mana, hand, grave, life, mana):
    gained = spells(av_mana, life_gain(hand, grave, av_mana, mana), mana)
    if type(gained) == int:
        life += gained
    hand_check(hand, grave)
    return


def play_the_game(board_state):
    p1 = board_state[0]
    p2 = board_state[1]
    mana = board_state[2]
    goes_first = board_state[3]
    p1_turns = 0
    p2_turns = 0
    p1_ss = []
    p2_ss = []
    p1_life = 20
    p2_life = 20
    # taking turns... goes_first determines who plays first
    if goes_first == 0:
        while True:
            print()
            print("Start of Round {}.".format(p1_turns + 1))
            print("Player1 Field {} Hand {} Grave {} Life Total {}".format(p1[2], p1[0], p1[3], p1_life))
            print("Player2 Field {} Hand {} Grave {} Life Total {} ".format(p2[2], p2[0], p2[3], p2_life))
            upkeep(p1[1], p1[0], p2_turns, "P2", goes_first)
            goes_first += 2
            turn_snap_shot, mana_left = check_land(mana, p1[1], p1[0], p1[2], p1[3])
            p1_ss.append(turn_snap_shot)
            m_stat = check_snap_shot(p1_ss, p1[2])
            if m_stat == 0:
                stats = ["P2", p2_turns]
                print("mana starved")
                return stats
            main_phase(p1[0], p1[1], p1[3], p1_life, p2[2], p2[3], "P2", p2_life, mana_left, mana)
            combat_phase(p1[2], p2[2], p2_life)
            main_phase2(mana_left, p1[0], p1[3], p1_life, mana)

            print("P2 turn")

            upkeep(p2[1], p2[0], p1_turns, "P1", goes_first)
            turn_snap_shot, mana_left = check_land(mana, p2[1], p2[0], p2[2], p2[3])
            p2_ss.append(turn_snap_shot)
            m_stat = check_snap_shot(p2_ss, p2[2])
            if m_stat == 0:
                stats = ["P1", p1_turns]
                print("mana starved")
                return stats
            main_phase(p2[0], p2[1], p2[3], p2_life, p1[2], p1[3], "P1", p1_life, mana_left, mana)
            combat_phase(p2[2], p1[2], p1_life)
            main_phase2(mana_left, p2[0], p2[3], p2_life, mana)
    if goes_first == 1:
        while True:
            print()
            print("Start of Round {}.".format(p1_turns + 1))
            print("Player1 Field {} Hand {} Grave {} Life Total {}".format(p1[2], p1[0], p1[3], p1_life))
            print("Player2 Field {} Hand {} Grave {} Life Total {} ".format(p2[2], p2[0], p2[3], p2_life))
            upkeep(p2[1], p2[0], p1_turns, "P1", goes_first)
            goes_first += 1
            turn_snap_shot, mana_left = check_land(mana, p2[1], p2[0], p2[2], p2[3])
            p2_ss.append(turn_snap_shot)
            m_stat = check_snap_shot(p2_ss, p2[2])
            if m_stat == 0:
                stats = ["P1", p1_turns]
                print("mana starved")
                return stats
            main_phase(p2[0], p2[1], p2[3], p2_life, p1[2], p1[3], "P1", p1_life, mana_left, mana)
            combat_phase(p2[2], p1[2], p1_life)
            main_phase2(mana_left, p2[0], p2[3], p2_life, mana)

            print("P2 turn")

            upkeep(p1[1], p1[0], p2_turns, "P2", goes_first)
            turn_snap_shot, mana_left = check_land(mana, p1[1], p1[0], p1[2], p1[3])
            p1_ss.append(turn_snap_shot)
            m_stat = check_snap_shot(p1_ss, p1[2])
            if m_stat == 0:
                stats = ["P2", p2_turns]
                print("mana starved")
                return stats
            main_phase(p1[0], p1[1], p1[3], p1_life, p2[2], p2[3], "P2", p2_life, mana_left, mana)
            combat_phase(p1[2], p2[2], p2_life)
            main_phase2(mana_left, p1[0], p1[3], p1_life, mana)



def status(deck1, deck2, mana):
    p1 = open_hand(deck1, mana)
    p2 = open_hand(deck2, mana)
    goes_first = 0
    if p1[4] > p1[4]:
        goes_first = 1

    board_state = [p1, p2, mana, goes_first]
    return play_the_game(board_state)

db(2)


# def out_of_all_games(mana):
#     evo_wilds_wins = 0
#     non_evo_wins = 0
#     ties = 0
#     evo_draw_steps = []
#     non_evo_draw_steps = []
#     games = 100000
#     while games > 0:
#         winner, turns = db(mana)
#         # appends num of draws into win condition if player won
#         if winner == "P1":
#             evo_draw_steps.append(turns)
#             evo_wilds_wins += 1
#             print("Evo wins")
#         elif winner == "P2":
#             non_evo_draw_steps.append(turns)
#             non_evo_wins += 1
#             print("Non-Evo wins")
#         games -= 1
#     evo_totes = sum(evo_draw_steps)/len(evo_draw_steps)
#     non_evo_totes = sum(non_evo_draw_steps)/len(non_evo_draw_steps)
#     print()
#     print("Stats for {} Mana Limited Deck \n".format(mana))
#     print("Evo Deck Wins {}".format(evo_wilds_wins))
#     print("Non Evo Deck Wins {}".format(non_evo_wins))
#     print("Ties to Win {}".format(ties))
#     print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(evo_totes))
#     print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(non_evo_totes))
#
# out_of_all_games(2)
# #out_of_all_games(3)

