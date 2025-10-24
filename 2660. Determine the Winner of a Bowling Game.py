# You are given two 0-indexed integer arrays player1 and player2,
# representing the number of pins that player 1 and player 2 hit in a bowling game,
# respectively.
# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.
# Assume a player hits xi pins in the ith turn. The value of the ith turn for the player is:
# 2xi if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
# Otherwise, it is xi.
# The score of the player is the sum of the values of their n turns.
# Return:
# 1 if the score of player 1 is more than the score of player 2,
# 2 if the score of player 2 is more than the score of player 1, and
# 0 in case of a draw.

from typing import List

pl1 = [1,1,1,10,10,10,10]
pl2 = [10,10,10,10,1,1,1]

def isWinner(player1: List[int], player2: List[int]) -> int:
    sum1, sum2 = 0, 0
    for i in range(len(player1)):
        if i == 0: #Работа с первым элементом
            sum1 += player1[0]
            sum2 += player2[0]
        if i == 1: #Работа со вторым элементом
            if player1[i-1] == 10:
                sum1 += player1[1] * 2
            else: sum1 += player1[1]
            if player2[i-1] == 10:
                sum2 += player2[1] * 2
            else: sum2 += player2[1]
        if i > 1:
            if player1[i-1] == 10 or player1[i-2] == 10 :
                sum1 += player1[i] * 2
            else: sum1 += player1[i]
            if player2[i - 1] == 10 or player2[i-2] == 10 :
                sum2 += player2[i] * 2
            else: sum2 += player2[i]
    if sum1 == sum2:
        return 0
    return 1 if sum1 > sum2 else 2

def test_isWinner():
    assert isWinner([5,10,3,2], [6,5,7,3]) == 1
    assert isWinner([3,5,7,6], [8,10,10,2]) == 2
    assert isWinner([2,3], [4,1]) == 0
    assert isWinner([1,1,1,10,10,10,10], [10,10,10,10,1,1,1]) == 2


if __name__ == "__main__":
    test_isWinner()
    print("OK")
    isWinner(pl1, pl2)


# Best
# sum2 = 0
#         double_turn = 0
#         for i in range(len(player1)):
#             if(double_turn > 0):
#                 double_turn -= 1
#                 sum1 += player1[i]
#             sum1 += player1[i]
#             if(player1[i] == 10):
#                 double_turn = 2
#         double_turn = 0
#         for i in range(len(player2)):
#             if(double_turn > 0):
#                 double_turn -= 1
#                 sum2 += player2[i]
#             sum2 += player2[i]
#             if(player2[i] == 10):
#                 double_turn = 2
#         if(sum1 > sum2):
#             return 1
#         elif(sum2>sum1):
#             return 2
#         else:
#             return 0
