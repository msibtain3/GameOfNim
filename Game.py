from random import randint
from functools import reduce

def draw_nim_board(lst):
    pile_num = 0
    for ele in lst:
        if pile_num < 10:
            print('0',end='')
        print(str(pile_num)+': ',end='')
        pile_num += 1
        for i in range(ele):
            if i == ele-1:
                print('O')
            else:
                print('O', end='')
    print()
    return


play = True # bool to check if user wants to play again
while play:
    while True:
        # asking the user if it wants to play against human or AI
        try:
            ai = input('Play with Human or AI?\n')
            if ai.upper() == 'A' or ai.upper() == 'AI':
                ai = 'AI'
            elif ai.upper() == 'H' or ai.upper() == 'HUMAN':
                ai = "H"
            break
        except ValueError:
            print("Invalid Input")


    # Get number of random piles
    number_piles = randint(2,5)
    piles = []

    # Populating the piles with rocks
    for i in range(number_piles):
        piles.append(randint(1,2*number_piles+1))

    turn = 0

    # starting the actual game
    print("\nNOTE: THE NUMBERING OF PILES STARTS FROM ZERO\n")
    while piles:
        draw_nim_board(piles)

        # if player turn :
        if turn == 0 or (turn == 1 and ai == 'H'):
            print(f'Player {turn + 1} Turn')
            while True:
                try:
                    take_pile = int(input('Select the Pile to pick Stones from: '))
                    if take_pile < 0 or take_pile > len(piles) - 1:
                        raise ValueError
                    break
                except ValueError:
                    print(f'Pile number should be an integer between 0 and {len(piles) - 1}')
            # Choose how many stones to take from pile
            while True:
                try:
                    stones_taken = int(input('Number of stones to take: '))
                    if stones_taken < 1 or stones_taken > piles[take_pile]:
                        raise ValueError
                    break
                except ValueError:
                    print(f'Number of stones taken should be an integer between 1 and {piles[take_pile]}')

        # if AI turn:
        elif turn == 1:
            if ai == 'AI':
                print('Computer Turn')

                # XOR NIMSUM METHOD
                nim_sum = reduce(lambda x, y: x ^ y, piles)
                if nim_sum != 0:
                    # try to minimize the nim_sum value
                    for i in range(len(piles)):
                        if nim_sum ^ piles[i] < piles[i]:
                            take_pile = i
                            stones_taken = piles[i] - (nim_sum ^ piles[i])
                else:
                    take_pile = randint(0, len(piles) - 1)
                    stones_taken = randint(1, piles[take_pile])
                print(f'Computer took {stones_taken} stones from Pile {take_pile}')


        # Updating pile after deleting stones
        piles[take_pile] -= stones_taken


        # Deleting empty piles
        piles = list(filter(lambda num: num != 0, piles))
        if piles:
            turn = 1 - turn
        else:
            # returning the winner of the game

            if turn == 0 or (turn == 1 and ai == 'H'):
                print(f'Player {turn + 1} Wins')
            else:
                print('Computer Wins')

    # play again user input :
    again = input("\nDo you want to play again ? \n")
    again = again.lower()
    if again == 'n' or again == 'no':
        play = False # game ends

