'''
Data - Queue
10935 - Throwing cards away I
Given is an ordered deck of n cards numbered 1 to n with card 1 at the top and card n at the bottom. The following operation is performed as long as there are at least two cards in the deck: Throw away the top card and move the card that is now on the top of the deck to the bottom of the deck.  Your task is to find the sequence of discarded cards and the last, remaining card.
'''
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            cards = []
            discard = []
            for i in range(1, n + 1):
                cards.append(i)
            while len(cards) > 1:
                discard.append(cards.pop(0))
                cards.append(cards.pop(0))
            print("Discarded cards:", end = "")
            if n > 1:
                print("", discard[0], end = "")
            for i in range(1, len(discard)):
                print(',' ,discard[i], end = "")
            print()
            print("Remaining card:", cards[0])
        except(EOFError):
            break
