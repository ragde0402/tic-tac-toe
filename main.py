from random import sample, choice

class player():

    def __init__(self, num):
        self.name = f"player {num}"
        self.fields = []
        self.sign = "X"
        self.auto = False

    def choose_sign(self):
        self.new_sign = input(f"{self.name} what sign do you want to be? X or O.").upper()
        self.sign = self.new_sign


class game():

    def __init__(self):
        self.board = {"A": {1: " ", 2: " ", 3: " "},
                      "B": {1: " ", 2: " ", 3: " "},
                      "C": {1: " ", 2: " ", 3: " "}}
        self.player1 = player(1)
        self.player2 = player(2)
        self.list_of_players = sample([self.player1, self.player2], 2)
        self.win = {1: ["A1", "A2", "A3"],
                    2: ["B1", "B2", "B3"],
                    3: ["C1", "C2", "C3"],
                    4: ["C1", "B1", "A1"],
                    5: ["C2", "B2", "A2"],
                    6: ["C3", "B3", "A3"],
                    7: ["A1", "B2", "C3"],
                    8: ["C1", "B2", "A3"],
        }
        self.all_fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.round = 0
        self.winner = False

    def creating_players_in_game(self):
        self.num = input("How many players? 1 or 2.")
        if self.num == "1":
            self.player2.auto = True
            self.player2.name = "Computer"
        elif self.num == "2":
            pass
        else:
            print("Pick 1 or 2.")
            self.creating_players_in_game()
        self.player1.choose_sign()
        if self.player1.sign == self.player2.sign:
            self.player2.sign = "O"

    def turn(self, player):
        self.round += 1
        if player.auto == False:
            self.field = input(f"{player.name} select a field(e.g. A1): ").upper()
            self.pick = [a for a in self.field]
        else:
            self.field = choice(self.all_fields)
            self.pick = [a for a in self.field]
        try:
            if self.board[self.pick[0]][int(self.pick[1])] == " ":
                self.board[self.pick[0]][int(self.pick[1])] = player.sign
            else:
                self.turn(player)
        except KeyError:
            self.turn(player)
        else:
            player.fields.append(self.field)

    def end_game(self):
        for player in self.list_of_players:
            for comb in self.win:
                if len(list(set(self.win[comb]).intersection(player.fields))) == 3:
                    self.winner = True
                    print(f"{player.name} win.")
                    return True

        if self.round == 9:
            print("Game tied.")
            self.winner = True
            return True

        print("Next round")

def printing_board(class_):
    print(f"A   {class_.board['A'][1]} | {class_.board['A'][2]} | {class_.board['A'][3]}\n   ------------\n"
              f"B   {class_.board['B'][1]} | {class_.board['B'][2]} | {class_.board['B'][3]}\n   ------------\n"
              f"C   {class_.board['C'][1]} | {class_.board['C'][2]} | {class_.board['C'][3]}")

game = game()
game.creating_players_in_game()

while not game.winner:
    for x in range(2):
        printing_board(game)
        game.turn(game.list_of_players[x])
        if game.end_game():
            printing_board(game)
            break
