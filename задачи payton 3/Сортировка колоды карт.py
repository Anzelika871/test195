import random
def quick_sort_deck(deck):
    if len(deck) < 4:
        return sorted(deck)
    main = random.choice(deck)
    left_deck = []
    right_deck = []
    middle_deck = []
    for card in deck:
        if card < main:
            left_deck.append(card)
        elif card > main:
            right_deck.append(card)
        else:
            middle_deck.append(card)
    sorted_left = quick_sort_deck(left_deck)
    sorted_right = quick_sort_deck(right_deck)
    return sorted_left + middle_deck + sorted_right
print("Введите значения карт через пробел:")
cards = list(map(int, input().split()))
new_cards = quick_sort_deck(cards)
print(f"Отсортированная колода: {new_cards}")