import random
import re
from icecream import install

install()


# we need to make this dynamic and pretty
def printLeaderBoard(a, b):
    print("======Leader Boaroad =========")
    print(f"====Player A || Player B=====")
    print("==============================")


def registerPlayers():
    playerA = input("What is your name? ")
    playerB = input("What is your name? ")
    printLeaderBoard(playerA, playerB)
    return (playerA, playerB)


def throwDice():
    return random.choice([1, 2, 3, 4, 5, 6])


def extendedSum(a):
    aa = sum(a)
    if aa % 2 == 0:
        return aa + 10
    else:
        return aa + 5


def playGame(a, b):

    for i in range(1, 13):
        input(f"Player A throw your {i} dice")
        a.append(throwDice())

        ic(a)
        input(f"Player B throw your {i} dice")
        b.append(throwDice())
        ic(b)

    if extendedSum(a) > extendedSum(b):
        return (
            "A has won with: "
            + str(extendedSum(a))
            + ", and B scored: "
            + str(extendedSum(b))
        )
    elif extendedSum(a) < extendedSum(b):
        return (
            "B has won with: "
            + str(extendedSum(b))
            + ", and A  scored: "
            + str(extendedSum(a))
        )
    else:
        while extendedSum(a) == extendedSum(b):
            a.append(throwDice())
            b.append(throwDice())
        if extendedSum(a) > extendedSum(b):
            return (
                "A has won with: "
                + str(extendedSum(a))
                + ", and B scored: "
                + str(extendedSum(b))
            )
        else:
            return (
                "B has won with: "
                + str(extendedSum(b))
                + ", and A  scored: "
                + str(extendedSum(a))
            )


if __name__ == "__main__":
    registerPlayers()
    ic(playGame(a=[], b=[]))
