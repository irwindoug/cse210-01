class TicTacToe:
    def __init__(self) -> None:
        self.board = list(range(1,10))
        self.player = "X"

    def draw(self) -> None:
        print(("%s | %s | %s\n- + - + -\n%s | %s | %s\n- + - + -\n%s | %s | %s") %
                (self.board[0], self.board[1], self.board[2],
                self.board[3], self.board[4], self.board[5],
                self.board[6], self.board[7], self.board[8]))

    def play(self) -> None:
        choice = int(input(f"{self.player}'s turn to choose a square (1-9): "))-1
        self.update(choice)
    
    def update(self, choice) -> None:
        # Fill square
        self.board[choice] = self.player
        # Switch Players
        if self.player =="O": self.player ="X"
        else: self.player = "O"

    def check_for_win(self) -> bool:
        return  (self.board[0] == self.board[1] == self.board[2] or 
                self.board[3] == self.board[4] == self.board[5] or 
                self.board[6] == self.board[7] == self.board[8] or 
                self.board[0] == self.board[3] == self.board[6] or 
                self.board[1] == self.board[4] == self.board[7] or 
                self.board[2] == self.board[5] == self.board[8] or 
                self.board[0] == self.board[4] == self.board[8] or 
                self.board[2] == self.board[4] == self.board[6])

    def check_for_draw(self) -> bool:
        for i in range(9):
            if (self.board[i] != 'X' and self.board[i] != 'O'): return False
