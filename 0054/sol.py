from collections import Counter

hands = open('input').read().strip().splitlines()

def are_first_chars_consecutive(cards):
    order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    first_chars = [card[0] for card in cards]

    indices = [order.index(char) for char in first_chars]

    if sorted(indices) == [0, 9, 10, 11, 12]:
        return True

    return sorted(indices) == list(range(min(indices), max(indices) + 1))

def are_all_same_suit(cards):
    return all(len(s) > 1 and s[1] == cards[0][1] for s in cards)

def are_three_of_a_kind(cards):
    first_chars = [card[0] for card in cards]
    return any(count == 3 for count in Counter(first_chars).values())

def is_full_house(cards):
    return sorted(Counter(card[0] for card in cards).values()) == [2, 3]

def is_two_pair(cards):
    return sorted(Counter(card[0] for card in cards).values()) == [1, 2, 2]

def is_pair(cards):
    return sorted(Counter(card[0] for card in cards).values()) == [1, 1, 1, 2]

def get_scores(players, printing=True):
    scores = []
    for i, p in enumerate(players):
        straight = are_first_chars_consecutive(p) 
        flush = are_all_same_suit(p)
        full = is_full_house(p)
        three = are_three_of_a_kind(p)
        two_pair = is_two_pair(p)
        pair = is_pair(p)

        if straight and flush:
            if printing: print(f"Player {i+1} has a straight-flush: {sorted(p)}\n")
            scores.append(7)
        elif straight:
            if printing: print(f"Player {i+1} has a straight: {sorted(p)}\n")
            scores.append(6)
        elif flush:
            if printing: print(f"Player {i+1} has a flush: {sorted(p)}\n")
            scores.append(5)
        elif full:
            if printing: print(f"Player {i+1} has a full house: {sorted(p)}\n")
            scores.append(4)
        elif three:
            if printing: print(f"Player {i+1} has three of a kind: {sorted(p)}\n")
            scores.append(3)
        elif two_pair:
            if printing: print(f"Player {i+1} has two pair: {sorted(p)}\n")
            scores.append(2)
        elif pair:
            if printing: print(f"Player {i+1} has a pair: {sorted(p)}\n")
            scores.append(1)
        else:
            if printing: print(f"Player {i+1} has a high card: {sorted(p)}\n")
            scores.append(0)
    return scores

def solve():
    i = 0
    wins_p1, wins_p2 = 0, 0
    ties = 0
    for hand in hands:
        p1 = [x for x in hand.split(' ')[:5]]
        p2 = [x for x in hand.split(' ')[5:]]

        players = [p1, p2]

        scores = get_scores(players, False)
        print(scores)
        if scores[0] > scores[1]:
            wins_p1 += 1
        elif scores[0] < scores[1]:
            wins_p2 += 1
        else:
            ties += 1
        i += 1
    return wins_p1, wins_p2, ties

print(solve())
