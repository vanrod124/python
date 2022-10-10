#Randomly generate a 6 × 6 list of assorted characters such that there are exactly two of each character.

import random


def main():
    # create a list of ascii characters
    asciiList = [chr(i) for i in range(33, 127)]
    # create a list of 6x6 characters
    gameList = [[0 for i in range(6)] for j in range(6)]

    # randomly select 18 characters from the ascii list * 2
    randomList = random.sample(asciiList, 18) * 2
    # shuffle the list
    random.shuffle(randomList)

    # assign the characters to the game list
    for i in range(6):
        for j in range(6):
            gameList[i][j] = randomList.pop()

    # print the game list
    for i in range(6):
        for j in range(6):
            print(gameList[i][j], end=' ')
        print()


#create a option that will opt user to produce again the game. do not end the program if the user wants to play again.
if __name__ == '__main__':
    main()
    while True:
        print("Do you want to play again? (Y/N)")
        playAgain = input()
        if playAgain == "Y":
            main()
        else:
            break
            


            


