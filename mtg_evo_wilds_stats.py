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

def play_land(deck,hand,field):
    for card in hand:
        #takes care of evolving wilds
        if card == 10:
            hand.remove(card)
            color2 = 0
            color3 = 0
            #checks to see which land is needed
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
                        random.shuffle(deck)
                        return
                elif color3 > color2:
                    if cards == 2:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        return
                elif cards == 2 or cards == 3:
                    if color2 >=4 and color3 >=4:
                        field.append(cards)
                        deck.remove(cards)
                        random.shuffle(deck)
                        return
        #plays land otherwise
        elif card == 2 or card == 3:
            field.append(card)
            hand.remove(card)
            return

def check_field(hand,field):
    num2s = 0
    num3s = 0
    #counts the lands to see if an adequate amount of land is available to cast 'win condition' cards: 42
    for card in field:
        if card == 2:
            num2s += 1
        elif card == 3:
            num3s += 1
    #8 mana total to cast "win condition" cards
    if num2s >= 4 and num3s >= 4:
        for cards in hand:
            if cards == 42:
                return "Winner!"


def turn(hand, deck=None,field=None):
    counter = 0
    #counts number of draws
    wins = 0
    #when this is 1 game ends
    stuck_mana1 = 0
    stuck_mana2 = 0
    stuck_mana3 = 0
    #tallies when player is stuck with either 1,2 or 3 mana for several rounds...commonly leading to a loss IRL
    while len(deck) > 0:
        remove_card_from_deck(deck,hand)
        play_land(deck,hand,field)
        hand_check(hand)
        game_over = check_field(hand,field)
        if game_over == "Winner!":
            wins += 1
            break
        #takes into account getting mana starved
        elif game_over != "Winner!":
            if len(field) == 1:
                stuck_mana1 += 1
            elif len(field) == 2:
                stuck_mana2 += 1
            elif len(field) == 3:
                stuck_mana3 += 1
        if stuck_mana1 > 1 or stuck_mana2 > 3 or stuck_mana3 >3:
            break
        counter += 1
    return counter

def status():
    non_evo_wilds = [42, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 1, 42]
    #has two win condition cards
    evo_wilds = [42, 10, 10, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 42]
    #has two win condition cards, two evolving wilds, 7 of one color, 8 of another, and 21 creature/spells
    p1_hand, p1_deck, p1_field = hands(evo_wilds)
    p2_hand, p2_deck, p2_field = hands(non_evo_wilds)
    #taking turns
    totals_for_p1 = turn(p1_hand, deck=p1_deck,field=p1_field)
    totals_for_p2 = turn(p2_hand,deck=p2_deck,field=p2_field)
    stats = [totals_for_p1,totals_for_p2]
    return stats

def out_of_all_games():
    evo_wilds_wins = 0
    non_evo_wins = 0
    ties = 0
    evo_draw_steps = []
    non_evo_wins_steps = []
    games = 100
    while games > 0:
        p1_draws_into_win, p2_draws_into_win = status()

        evo_draw_steps.append(p1_draws_into_win)
        non_evo_wins_steps.append(p2_draws_into_win)

        if p1_draws_into_win > p2_draws_into_win:
            evo_wilds_wins += 1
        elif p1_draws_into_win < p2_draws_into_win:
            non_evo_wins += 1
        else:
            ties += 1
        games -= 1
    print("Evo Deck Wins {}".format(evo_wilds_wins))
    print("Non Evo Deck Wins {}".format(non_evo_wins))
    print("Ties {}\n".format(ties))
    print("With Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(evo_draw_steps)/len(evo_draw_steps)))
    print("Without Evolving Wilds: {} Cards Drawn Into Win Condition.".format(sum(non_evo_wins_steps)/len(non_evo_wins_steps)))


out_of_all_games()
