# -*- coding: utf-8 -*-
from __future__ import print_function
theBord = [i+1 for i in range(9)]
def printBoard(board):
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(theBord[3 * i + j], end = '|')
            else:
                print(theBord[3 * i + j])
        if i < 2:
            print('-+-+-')
    return
def getWinner(board):
    winner = ''
    if theBord[0] == theBord[1] == theBord[2]:
        winner = theBord[0]
    if theBord[3] == theBord[4] == theBord[5]:
        winner = theBord[3]
    if theBord[6] == theBord[7] == theBord[8]:
        winner = theBord[6]
    if theBord[0] == theBord[3] == theBord[6]:
        winner = theBord[0]
    if theBord[1] == theBord[4] == theBord[7]:
        winner = theBord[1]
    if theBord[2] == theBord[5] == theBord[8]:
        winner = theBord[2]
    if theBord[0] == theBord[4] == theBord[8]:
        winner = theBord[0]
    if theBord[2] == theBord[4] == theBord[6]:
        winner = theBord[2]
    return winner
def begin():
    print('每格的标号如下，X先行，O随后，交替进行。')
    printBoard(theBord)
    turn = 'X'
    for i in range(9):
        print('请' + turn + '选一格落子：')
        move = input()
        theBord[move-1] = turn
        printBoard(theBord)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if getWinner(theBord) != '':
            print('\n' + getWinner(theBord) + '赢了！')
            break
    if getWinner(theBord) == '':
        print('\n平局！')
    return
begin()
exit()