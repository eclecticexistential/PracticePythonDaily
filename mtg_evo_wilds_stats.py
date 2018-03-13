import math
import random


class Mana:
    def __init__(self, land_type=1, num_lands=17, evo=0):
        if land_type < 1:
            raise ValueError("Only super secret decks can run with no mana.")
        self.land_type = land_type
        self.num_lands = num_lands
        self.evo = evo
        self.mana = []
        self.totals = math.floor(num_lands / land_type)
        m_types = [2, 3, 4, 5, 6]
        for z in range(evo):
            self.mana.append(10)
        for y in range(self.land_type):
            for x in range(self.totals-1):
                self.mana.append(m_types[y])
        while len(self.mana) != num_lands:
            rando = random.randint(0, self.land_type-1)
            self.mana.append(m_types[rando])

    def __iter__(self):
        for lands in self.mana:
            yield lands


class Spells:
    def __init__(self, removal=4, life_gain=1, tutor=2, draw_cards=1, combat_tricks=4):
        self.total_spells = {33: removal, 9: life_gain, 66: tutor, 42: draw_cards, 13: combat_tricks}
        if removal < 0 or life_gain < 0 or tutor < 0 or draw_cards < 0:
            raise ValueError("You're going to need a positive number of spells.")
        self.removal = removal
        self.life_gain = life_gain
        self.tutor = tutor
        self.draw_cards = draw_cards
        self.combat_tricks = combat_tricks
        self.spells = []
        for value in self.total_spells:
            for _ in range(self.total_spells[value]):
                self.spells.append(value)

    def __iter__(self):
        for spells in self.spells:
            yield spells


class Creatures:
    def __init__(self, lil=9, bombs=2):
        if lil < 5 or bombs < 1:
            raise ValueError("You're going to need some creatures")
        self.lil = lil
        self.bombs = bombs
        self.total_creatures = {8: lil, 88: bombs}
        self.creatures = []
        for value in self.total_creatures:
            for _ in range(self.total_creatures[value]):
                self.creatures.append(value)

    def __iter__(self):
        for creatures in self.creatures:
            yield creatures


class Deck:
    def __init__(self, total_cards=40, mana=Mana(), spells=Spells(), creatures=Creatures()):
        if total_cards < 40:
            raise ValueError("40 is the lowest card amount in all formats.")
        self.total_cards = total_cards
        self.mana = mana
        self.spells = spells
        self.creatures = creatures
        self.cards = []
        self.cards.extend(mana)
        self.cards.extend(spells)
        self.cards.extend(creatures)

        if len(self.cards) < self.total_cards:
            raise ValueError("Check total card count.")

    def __iter__(self):
        random.shuffle(self.cards)
        for card in self.cards:
            yield card


def dice():
    return random.randint(1, 20)


class Hand:
    def __init__(self, deck, cc=7):
        self.cc = cc
        self.hand = []
        self.deck = deck
        try:
            for _ in range(self.cc):
                for card in self.deck:
                    self.hand.append(card)
                    break
        except TypeError:
            print("Dunno yet.")

    def __iter__(self):
        for card in self.hand:
            yield card


def create_deck(cards, type_mana, evos=0):
    if evos != 0:
        evo = Deck(cards, Mana(land_type=type_mana, evo=evos))
        return evo
    elif evos == 0:
        non_evo = Deck(cards, Mana(land_type=type_mana))
        return non_evo


def create_hand(deck, cc):
    new_hand = Hand(deck, cc)
    return list(new_hand)


def mulligan(deck, mana, cc):
    shuffled = random.shuffle(list(deck))
    smaller_hand = create_hand(shuffled, cc)
    return check_hand(smaller_hand, mana, shuffled)


def check_hand(hand, mana, deck):
    a = hand.count(2)
    b = hand.count(3)
    c = hand.count(4)
    evo = hand.count(10)
    cc = len(hand)
    if cc < 3:
        return False
    if mana == 1:
        if a < 2:
            cc -= 1
            return mulligan(deck, mana, cc)
    if mana == 2:
        if a == 0 or b == 0:
            if evo > 0:
                return hand
            else:
                cc -= 1
                return mulligan(deck, mana, cc)
        else:
            return hand
    if mana == 3:
        if evo > 0:
            if a > 0 and b > 0 or a > 0 and c > 0 or b > 0 and c > 0:
                return hand
            else:
                cc -= 1
                return mulligan(deck, mana, cc)
        elif evo == 0:
            if a > 0 and b > 0 and c > 0:
                return hand
            else:
                cc -= 1
                return mulligan(deck, mana, cc)


def open_hand(cards, typemana, evos=0):
    this_deck = create_deck(cards, typemana, evos)
    a_hand = create_hand(this_deck, 7)
    manad = check_hand(a_hand, typemana, this_deck)
    if manad:
        curr_deck = list(this_deck)
        for card in manad:
            if card in curr_deck:
                curr_deck.remove(card)
        return [curr_deck, manad]
    else:
        return False


def draw(deck, hand):
    try:
        a = random.choice(deck)
    except IndexError:
        return 1
    deck.remove(a)
    hand.append(a)
    return [deck, hand]


def establish_field(cc, type_mana, evos=0):
    try:
        player_stats = open_hand(cc, type_mana, evos)
        field = []
        player_stats.append(field)
        graveyard = []
        player_stats.append(graveyard)
        return player_stats
    except AttributeError:
        return False


def hand_check(hand, graveyard):
    # discards a 1 to take into account creatures/spells that are played during each round
    if len(hand) > 7:
        for cards in hand:
            if cards == 9 or cards == 8:
                hand.remove(cards)
                graveyard.append(cards)
                break


def play_land(mana, deck, hand, field, graveyard):
    d = field.count(2)
    e = field.count(3)
    f = field.count(4)
    if mana == 1:
        field.append(2)
        hand.remove(2)
    elif mana == 2:
        if d > e:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 3 in deck:
                    deck.remove(3)
                    field.append(3)
                    return deck, hand, field, graveyard
            elif 3 in hand:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard
        elif e > d:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 2 in deck:
                    deck.remove(2)
                    field.append(2)
                    return deck, hand, field, graveyard
            elif 2 in hand:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard
        elif d == e:
            a = dice()
            if a <= 10:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard
            else:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard
    elif mana == 3:
        if d > e and e < f:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 3 in deck:
                    deck.remove(3)
                    field.append(3)
                    return deck, hand, field, graveyard
            elif 3 in hand:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard
        elif e > d and d < f:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 2 in deck:
                    deck.remove(2)
                    field.append(2)
                    return deck, hand, field, graveyard
            elif 2 in hand:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard
        elif f < d and f < e:
            if 10 in hand:
                graveyard.append(10)
                hand.remove(10)
                if 4 in deck:
                    deck.remove(4)
                    field.append(4)
                    return deck, hand, field, graveyard
            elif 4 in hand:
                field.append(4)
                hand.remove(4)
                return deck, hand, field, graveyard
        elif d == e and e == f:
            a = dice()
            a += 1
            if a <= 7:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard
            elif a > 14:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard
            else:
                field.append(4)
                hand.remove(4)
                return deck, hand, field, graveyard


def check_field(hand, field, evo, mana):
    a = field.count(2)
    b = field.count(3)
    c = field.count(4)

    # gets available mana
    available_mana = [a, b, c]

    if mana == 2:
        # checks if evo was played to see if legal move can be made using mana on this turn
        if evo == 1 and a == 1 and b == 1 or a == 3 and b == 3:
            pass
        if a >= 3 and b >= 3:
                if 42 in hand:
                    hand.remove(42)
                    field.append(42)
                    available_mana[0] -= 3
                    available_mana[1] -= 3
                    return available_mana
        if a >= 1 and a >= 1:
            if 8 in hand:
                hand.remove(8)
                field.append(8)
                available_mana[0] -= 1
                available_mana[1] -= 1
                return available_mana
    elif mana == 3:
        if evo == 1 and a == 1 and b == 1 and c == 1 or a == 3 and b == 3 and c == 3:
            pass
        if a >= 2 and b >= 2 and c >= 2:
            if 42 in hand:
                hand.remove(42)
                field.append(42)
                available_mana[0] -= 2
                available_mana[1] -= 2
                available_mana[2] -= 2
                return available_mana
        if num2s >= 1 and num3s >= 1 and num4s >= 1:
            if 8 in hand:
                hand.remove(8)
                field.append(8)
                available_mana[0] -= 1
                available_mana[1] -= 1
                available_mana[2] -= 1
                return available_mana


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
                        # print("tutored")
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
            # print()
            # print("Start of Round {}.".format(p1_turns +1))
            # print("Player1 Field {} Hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_grave, p1_life))
            # print("Player2 Field {} Hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_grave, p2_life))

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
            # print()
            # print("Start of Round {}.".format(p1_turns + 1))
            # print("Non-Evo Field {} Hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_grave, p1_life))
            # print("Evo Field {} Hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_grave, p2_life))
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


def out_of_all_games(mana, evo):
    evo_wilds_wins = 0
    non_evo_wins = 0
    ties = 0
    evo_draw_steps = []
    non_evo_draw_steps = []
    games = 100
    while games > 0:
        winner, turns = db(mana, evo)
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


# out_of_all_games(2, 2)
# out_of_all_games(3, 3)


# magic api starcity,tcg for data sets
# tcg life duration price of card

# lsv hypergeometric calculator
# mtgjson