
import random


def main():

    asciiList = [chr(i) for i in range(33, 127)]

    gameList = [[0 for i in range(6)] for j in range(6)]


    randomList = random.sample(asciiList, 18) * 2

    random.shuffle(randomList)


    for i in range(6):
        for j in range(6):
            gameList[i][j] = randomList.pop()


    for i in range(6):
        for j in range(6):
            print(gameList[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
    while True:
        print("Do you want to play again? (Y/N)")
        playAgain = input()
        if playAgain == "Y":
            main()
        else:
            break
            


            


