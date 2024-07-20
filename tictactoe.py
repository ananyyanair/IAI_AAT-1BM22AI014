#!/bin/python3

import math
import os
import random
import re
import sys

def checkwinner(board, player):
    winconditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player] * 3 in winconditions
def findbestmove(player, board):
    opponent = 'X' if player == 'O' else 'O'
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r] = board[r][:c] + player + board[r][c+1:]
                if checkwinner(board, player):
                    return r, c
                board[r] = board[r][:c] + '_' + board[r][c+1:]

                board[r] = board[r][:c] + opponent + board[r][c+1:]
                if checkwinner(board, opponent):
                    board[r] = board[r][:c] + '_' + board[r][c+1:]
                    return r, c
                board[r] = board[r][:c] + '_' + board[r][c+1:]
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                return r, c
def nextmove(player, board):
    r, c = findbestmove(player, board)
    print(r, c)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    player = first_multiple_input[0] 
    board = [input().rstrip() for _ in range(3)]  

    nextmove(player, board)
