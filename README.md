# OrbitoN-Game
Mid-Term Project

## Introduction
Orbito is a commercial abstract board game for two players. It is a specific case of an  m, n, k  game with  m = n = k = 4 , where the positions form two orbits. Players take turns alternately moving one of their opponent’s pieces and then placing one of their own pieces in a free position. At the end of each turn, all pieces rotate one position counterclockwise within their respective orbits.

The first player to achieve  k = 4  consecutive pieces of their color—horizontally, vertically, or diagonally—at the end of a turn wins the game. In this project, you will develop an adapted version of the game with  n  orbits and without the ability to move the opponent’s pieces.

In this project my aim was to recreat this game (with some minor changes) and built a bot to play against us.

This minor changes include:
- The board can have 2 to 5 orbits, meaning it can range form a 4x4 to a 10x10.
- k is iqual to orbit times 2
- The board rotates as normal

In this project, our professor challenged us to use Abstract Data Types (ADTs), which I did—making the process of completing the project significantly more challenging.
## Objective/Gameplay
To start the game, you need to call the function `orbito()` in the file, passing three arguments:
- n -> int, number of orbits that the board has.
- modo -> str, difficulty of the bot: 'facil', 'normal' or '2' (this last one is for 2 player mode)
- jog -> str, 'X' or '0'

Once you’ve set this up, simply run the program.

The player using ‘X’ always starts the game. The program will then prompt you to enter the position where you want to play. The positions are implied on the board and to enter it you first write the line and then the column, example:

```
Escolha uma posicao: a1
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [X]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
```

The 'X' appears on the position B2 because the board rotates right after each player turn.

:)











