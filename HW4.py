import random


class Card:
    def __init__(self, rank):
        self.rank = rank
        self.face = False

    def __str__(self):
        return (str(self.rank))


class Deck:
    def __init__(self, cards) -> None:
        self.deck = cards

    def add(self, card):
        self.deck.append(card)

    def deal(self):
        return self.deck.pop(0)

    def shuffle(self):
        random.shuffle(self.deck)

    def cards_num(self):
        return len(self.deck)

    def __str__(self):
        x = []
        for a in self.deck:
            x.append(a.rank)
        return str(x)


class Game:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cardsFacedUp = 0
        self.cardsFacedDown = rows * columns
        self.board = []
        self.populateBoard()

    def isGameOver(self):
        return self.cardsFacedDown == 0

    def play(self):
        while not self.isGameOver():
            try:
                first_coordinate = input(
                    "Enter the  Coordinates of first card:"
                ).split()
                second_coordinate = input(
                    "Enter the co-ordinates for second card:"
                ).split()
                first_card = self.board[int(first_coordinate[0]) - 1][
                    int(first_coordinate[1]) - 1
                ]
                second_card = self.board[int(second_coordinate[0]) - 1][
                    int(second_coordinate[1]) - 1
                ]
                if first_card.rank == second_card.rank:
                    first_card.face = True
                    second_card.face = True
                    self.cardsFacedDown -= 2
                    self.cardsFacedUp += 2
                else:
                    print(
                        f"Not an identical pair. Found {first_card} at {tuple(first_coordinate)} and {second_card} at {tuple(second_coordinate)}"
                    )
                self.displayBoard()
            except Exception:
                print("Error! You  have to enter co-ordinates in the form of x y")
                continue
        
        print("Game over, You did it.")

    def populateBoard(self):
        x = []
        row = []
        deck = Deck([])

        for a in range(1, self.rows * self.columns // 2 + 1):
            card1 = Card(a)
            card2 = Card(a)
            x.append(card1)
            x.append(card2)
            deck.add(card1)
            deck.add(card2)
        deck.shuffle()
        for b in range(self.rows):
            column = []
            for c in range(self.columns):
                column.append(deck.deal())
            row.append(column)
        self.board = row

        self.displayBoard()

    def displayBoard(self):
        for a in self.board:
            for b in a:
                print(b, end=" ") if b.face else print("*", end=" ")
            print()


def main():
    while True:
        # Force user to enter valid value for number of rows
        while True:
            rows = input("Enter number of rows ")
            if rows.isdigit() and (1 <= int(rows) <= 9):
                rows = int(rows)
                break
            else:
                print("    ***Number of rows must be between 1 and 9! Try again.***")
                # Adding *** and indenting error message makes it easier for the user to see

        # Force user to enter valid value for number of columns
        while True:
            columns = input("Enter number of columns ")
            if columns.isdigit() and (1 <= int(columns) <= 9):
                columns = int(columns)
                break
            else:
                print("    ***Number of columns must be between 1 and 9! Try again.***")

        if rows * columns % 2 == 0:
            break
        else:
            print("    ***The value of rows X columns must be even. Try again.***")

    game = Game(rows, columns)
    game.play()


if __name__ == "__main__":
    main()
