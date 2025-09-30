import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("This method should be implemented by subclasses.")

class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                pos = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if board.update(pos, self.symbol):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is making a move...")
        available = [i for i in range(1, 10) if board.is_empty(i)]
        pos = random.choice(available)
        board.update(pos, self.symbol)

class Board:
    def __init__(self):
        self.__grid = [" " for _ in range(9)]

    def display(self):
        print(self)

    def update(self, position, symbol):
        if 1 <= position <= 9 and self.__grid[position-1] == " ":
            self.__grid[position-1] = symbol
            return True
        return False

    def is_empty(self, position):
        return self.__grid[position-1] == " "

    def check_winner(self):
        g = self.__grid
        lines = [g[0:3], g[3:6], g[6:9], g[0:9:3], g[1:9:3], g[2:9:3], g[0:9:4], g[2:7:2]]
        for line in lines:
            if line[0] != " " and line[0] == line[1] == line[2]:
                return line[0]
        return None

    def is_full(self):
        return all(cell != " " for cell in self.__grid)

    def __str__(self):
        g = self.__grid
        return (f" {g[0]} | {g[1]} | {g[2]} \n---+---+---\n"
                f" {g[3]} | {g[4]} | {g[5]} \n---+---+---\n"
                f" {g[6]} | {g[7]} | {g[8]} ")

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()
        self.current_turn = 0

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        print("\nTic-Tac-Toe Game Start!\n")
        self.board.display()
        while True:
            player = self.players[self.current_turn]
            player.make_move(self.board)
            self.board.display()
            winner = self.board.check_winner()
            if winner:
                print(f"\nCongratulations! {player.name} ({player.symbol}) wins!")
                break
            if self.board.is_full():
                print("\nIt's a draw!")
                break
            self.switch_turns()

def main():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Do you want to play with a friend (1) or vs computer (2)? ")
    while mode not in ("1", "2"):
        mode = input("Please enter 1 (friend) or 2 (computer): ")
    if mode == "1":
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        p1 = HumanPlayer(name1, "X")
        p2 = HumanPlayer(name2, "O")
    else:
        name1 = input("Enter your name: ")
        p1 = HumanPlayer(name1, "X")
        p2 = ComputerPlayer("Computer", "O")
    game = Game(p1, p2)
    game.play()

if __name__ == "__main__":
    main()
