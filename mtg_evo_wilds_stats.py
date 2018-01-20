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
        else:
            return
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


def open_hand(x, mana):
    # make mulligan function
    counter = 7
    hand = []
    lands_on_field = []
    graveyard = []
    while counter > 0:
        a = random.choice(x)
        x.remove(a)
        hand.append(a)
        counter -= 1
    # change here to alter allowed number to mulligan to
    while len(hand) > 3:
        hand_size = mulligan(hand, mana, x)
        if hand_size is not None:
            hand = hand_size[0]
            x = hand_size[1]
        else:
            break
    data = [hand, x, lands_on_field, graveyard]
    return data


def draw(deck, hand):
    try:
        a = random.choice(deck)
    except IndexError:
        return 1
    deck.remove(a)
    hand.append(a)
    return [deck, hand]


def hands(x, mana):
    random.shuffle(x)
    # mixes up deck
    hand, deck, lands_on_field, graveyard = open_hand(x, mana)
    # gets opening hand of 7 cards, removes them from deck, creates field variable: an array
    return hand, deck, lands_on_field, graveyard


def hand_check(hand, graveyard):
    # discards a 1 to take into account creatures/spells that are played during each round
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
        if lands == 2:
            color2 += 1
        elif lands == 3:
            color3 += 1
        elif lands == 4:
            color4 += 1
    for card in hand:
        if card == 10:
            has_evo += 1
            graveyard.append(card)
            hand.remove(card)
            for cards in deck:
                # puts basic on the field
                if cards == 2:
                    if color2 > color3 and mana_one > mana_two:
                        pass
                    elif mana == 3 and color2 > color4 and mana_one > mana_three:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        # print("Evo used for 2.")
                        return 1
                elif cards == 3:
                    if color3 > color2 and mana_two > mana_one:
                        pass
                    elif mana == 3 and color3 > color4 and mana_two > mana_three:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        # print("Evo used for 3.")
                        return 1
                elif cards == 4:
                    if color4 > color2 and mana_three > mana_one:
                        pass
                    elif color4 > color3 and mana_three > mana_two:
                        pass
                    else:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        # print("Evo used for 4.")
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
            if mana == 2:
                if land1 >= 1 and land2 >= 1:
                    hand.remove(card)
                    graveyard.append(card)
                    for cards in deck:
                        hand.append(cards)
                        hand.append(cards)
                        untapped_mana[0] -= 1
                        untapped_mana[1] -= 1
                        print("tutored")
                        return 2
            if mana == 3:
                if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                    hand.remove(card)
                    graveyard.append(card)
                    for cards in deck:
                        hand.append(cards)
                        hand.append(cards)
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
            if mana == 2:
                if land1 >= 1 and land2 >= 1:
                    hand.remove(card)
                    graveyard.append(card)
                    untapped_mana[0] -= 1
                    untapped_mana[1] -= 1
                    return 5
            if mana == 3:
                if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                    hand.remove(card)
                    graveyard.append(card)
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
            if mana == 2:
                if land1 >= 1 and land2 >= 1:
                    for card in field:
                        if card == 42:
                            field.remove(card)
                            hand.remove(cards)
                            untapped_mana[0] -= 1
                            untapped_mana[1] -= 1
                            # opposite player sent to establish who won scenarios...use to distinguish graveyards
                            if player == "P1":
                                p2_graveyard.append(card)
                                p1_graveyard.append(cards)
                            elif player == "P2":
                                p1_graveyard.append(card)
                                p2_graveyard.append(cards)
                            # print("42 was removed")
                            return
            if mana == 3:
                if land1 >= 1 and land2 >= 1 or land2 >= 1 and land3 >= 1 or land1 >= 1 and land3 >= 1:
                    for card in field:
                        if card == 42:
                            field.remove(card)
                            hand.remove(cards)
                            if land1 >= 1 and land2 >= 1:
                                untapped_mana[0] -= 1
                                untapped_mana[1] -= 1
                            elif land2 >= 1 and land3 >= 1:
                                untapped_mana[1] -= 1
                                untapped_mana[2] -= 1
                            elif land3 >= 1 and land1 >= 1:
                                untapped_mana[0] -= 1
                                untapped_mana[2] -= 1
                            if player == "P1":
                                p2_graveyard.append(card)
                                p1_graveyard.append(cards)
                            elif player == "P2":
                                p1_graveyard.append(card)
                                p2_graveyard.append(cards)
                            # print("42 was removed")
                            return


def turn(hand, deck, field, graveyard, mana):
    snap_shot = []
    mana_left = []
    draw(deck, hand)
    was_evo_played = play_land(mana, deck, hand, field, graveyard)
    if was_evo_played == 1:
        snap_shot, mana_left = check_field(hand, field, 1, mana)
    elif was_evo_played != 1:
        snap_shot, mana_left = check_field(hand, field, 0, mana)
    return hand, deck, field, snap_shot, mana_left


def check_snap_shot(x, field):
    mana_stuck = 0
    for x, y in zip(x, x[1:]):
        if x == y:
            mana_stuck += 1
        elif x == 0 and y == 0:
            mana_stuck += 1
    if mana_stuck > 3 and len(field) <= 4:
        # print("Mana starved.")
        return 0


def define_winner():
    pass


def take_turn(snap_shot, deck, hand, field, graveyard, opp_turns, opp_field, opp_graveyard, player, life, mana):
    current_status = turn(hand, deck, field, graveyard, mana)
    untapped_mana = current_status[4]
    snap_shot.append(current_status[3])
    mana_fed = check_snap_shot(snap_shot, field)
    if mana_fed == 0:
        stats = [player, opp_turns]
        return stats
    else:
        removal(hand, opp_field, graveyard, opp_graveyard, untapped_mana, mana, player)
        if life >= 3:
            tutor(hand, deck, graveyard, untapped_mana, mana)
        damage = direct_damage(hand, graveyard, untapped_mana, mana)
        gained = life_gain(hand, graveyard, untapped_mana, mana)
        hand_check(hand, graveyard)
        if damage == 3:
            return damage
        if gained == 5:
            return gained
        else:
            return


def combat_tricks(hand, field, life_total):
    pass


def combat_phase(p1_field, p1_life_total, p1_turns, p1_deck, p2_field, p2_life_total, p2_turns, p2_deck):
    # check creatures returns damage based on 8 or 42 (creature size)
    p1_creatures = check_creatures(p1_field)
    p2_creatures = check_creatures(p2_field)

    if p1_creatures > p2_creatures:
        damage = (p1_creatures - p2_creatures) + 1
        p2_life_total -= damage
    elif p1_creatures < p2_creatures:
        damage = (p2_creatures - p1_creatures) + 1
        p1_life_total -= damage

    if p1_life_total <= 0:
        stats = ["P2", p2_turns]
        return stats
    if p2_life_total <= 0:
        stats = ["P1", p1_turns]
        return stats
    if len(p1_deck) == 0:
        stats = ["P2", p2_turns]
        return stats
    if len(p2_deck) == 0:
        stats = ["P1", p1_turns]
        return stats
    else:
        life_status = [p1_life_total, p2_life_total]
        return life_status


def play_the_game(board_state):
    player_one = board_state[0]
    p1_hand, p1_deck, p1_field, p1_grave = player_one
    player_two = board_state[1]
    p2_hand, p2_deck, p2_field, p2_grave = player_two
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
            print("Start of Round {}.".format(p1_turns +1))
            print("Player1 Field {} Hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_grave, p1_life))
            print("Player2 Field {} Hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_grave, p2_life))

            hit = take_turn(p1_ss, p1_deck, p1_hand, p1_field, p1_grave, p2_turns, p2_field, p2_grave, "P2", p1_life, mana)
            if hit == 3:
                p2_life -= 3
            elif hit == 5:
                p1_life += 5
            elif hit == 2:
                p1_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p1_turns += 1
            else:
                return health

            hit = take_turn(p2_ss, p2_deck, p2_hand, p2_field, p2_grave, p1_turns, p1_field, p1_grave, "P1", p2_life, mana)
            if hit == 3:
                p1_life -= 3
            elif hit == 5:
                p2_life += 5
            elif hit == 2:
                p2_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p2_turns += 1
            else:
                return health
    if goes_first == 1:
        while True:
            print()
            print("Start of Round {}.".format(p1_turns + 1))
            print("Non-Evo Field {} Hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_grave, p1_life))
            print("Evo Field {} Hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_grave, p2_life))
            hit = take_turn(p2_ss, p2_deck, p2_hand, p2_field, p2_grave, p1_turns, p1_field, p1_grave, "P1", p2_life, mana)
            if hit == 3:
                p1_life -= 3
            elif hit == 5:
                p2_life += 5
            elif hit == 2:
                p2_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p2_turns += 1
            else:
                return health
            hit = take_turn(p1_ss, p1_deck, p1_hand, p1_field, p1_grave, p2_turns, p2_field, p2_grave, "P2", p2_life, mana)
            if hit == 3:
                p2_life -= 3
            elif hit == 5:
                p1_life += 5
            elif hit == 2:
                p1_life -= 2
            health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck)
            if health[0] != "P1" and health[0] != "P2":
                p1_life = health[0]
                p2_life = health[1]
                p1_turns += 1
            else:
                return health


def status(deck1, deck2, mana):
    p1_dice_roll = dice_roll()
    p2_dice_roll = dice_roll()
    goes_first = 0
    if p1_dice_roll < p2_dice_roll:
        goes_first = 1

    board_state = [hands(deck1, mana), hands(deck2, mana), mana, goes_first]
    return play_the_game(board_state)


def out_of_all_games(mana):
    evo_wilds_wins = 0
    non_evo_wins = 0
    ties = 0
    evo_draw_steps = []
    non_evo_draw_steps = []
    games = 100
    while games > 0:
        winner, turns = db(mana)
        # appends num of draws into win condition if player won
        if winner == "P1":
            evo_draw_steps.append(turns)
            evo_wilds_wins += 1
            # print("Evo wins")
        elif winner == "P2":
            non_evo_draw_steps.append(turns)
            non_evo_wins += 1
            # print("Non-Evo wins")
        games -= 1
    evo_totes = sum(evo_draw_steps)/len(evo_draw_steps)
    non_evo_totes = sum(non_evo_draw_steps)/len(non_evo_draw_steps)
    print()
    print("Stats for {} Mana Limited Deck \n".format(mana))
    print("Evo Deck Wins {}".format(evo_wilds_wins))
    print("Non Evo Deck Wins {}".format(non_evo_wins))
    print("Ties to Win {}".format(ties))
    print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(evo_totes))
    print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(non_evo_totes))


out_of_all_games(2)
#out_of_all_games(3)


# magic api starcity,tcg for data sets
# tcg life duration price of card

# lsv hypergeometric calculator
# mtgjson