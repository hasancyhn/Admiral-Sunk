# Admiral-Sunk
Single player admiral sunk game.

Admiral Sunk Game
Write a Python program for a single-player battleship game, following the rules outlined below.

Game Rules:

The game board is a square matrix of size mxm (minimum 10x10).
The game board will be created using the list data type.
The fleet consists of ships with sizes of 1, 2, 3, and 4 squares (units).
Ships are placed on the game board vertically or horizontally (each ship is considered independently, meaning one ship can be vertical while another is horizontal).
Ships will be randomly placed on the game board, and the orientations (vertical or horizontal) will also be random.
After the ships are placed on the game board, the user can view the game board in 2 modes (both modes must be provided).
1- Hidden mode: The user will not know the locations of the ships.
2- Open mode: The ship locations will be visible on the game board.
Unopened cells on the game board will be represented by "?". Missed shots (where no ship part was hit) will be represented by "*". Hit shots (where a ship part was hit) will be represented by "x".
The user will be provided with messages for each shot. If the shot hits, the message will be "Congratulations! You hit a ship." If the shot misses, the message will be "Unfortunately, you missed." Additionally, if a ship is fully hit, an additional message will be displayed: "Congratulations! You sunk a ship."
After each shot, the game board will be updated (the console can be cleared and the new state of the game board can be printed).
If a previously targeted location is selected again, the user will be informed to choose another location.
The user will be given a number of shots equal to one-third of the game board size. For example, for a 10x10 (100) game board, the number of shots will be 100/3 = 33.
The game will end in two ways. If the user uses all their shots and fails to sink all the ships, the message "Unfortunately, you lost." will be displayed. In the other case, if all the ships are sunk before the user runs out of shots, their score will be calculated and the message "Congratulations! You won the game with 12 points." will be displayed. The game score is calculated by subtracting the number of shots made from the total number of shots.
After the game ends, the user will be given the option to play a new game or exit.
