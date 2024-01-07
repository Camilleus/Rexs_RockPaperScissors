import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class Game:
    translations = {
        'tie': "Both players selected {user_action.name}. It's a tie!",
        'win': "{user_action.name} wins! {user_action.name} beats {computer_action.name}.",
        'lose': "{user_action.name} loses. {computer_action.name} beats {user_action.name}.",
    }

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.results_history = []

    def get_user_selection(self):
        while True:
            try:
                choices = [f"{action.name}[{action.value}]" for action in Action]
                choices_str = ", ".join(choices)
                selection = int(input(f"Enter a choice ({choices_str}): "))
                action = Action(selection)
                return action
            except (ValueError, IndexError):
                range_str = f"[0, {len(Action) - 1}]"
                print(f"Invalid selection. Enter a value in range {range_str}")

    def get_computer_selection(self):
        selection = random.randint(0, len(Action) - 1)
        action = Action(selection)
        return action

    def determine_winner(self, user_action, computer_action):
        if user_action == computer_action:
            print(self.translations['tie'])
            self.draws += 1
            self.results_history.append('tie')
        elif (user_action, computer_action) in [(Action.Rock, Action.Scissors), (Action.Paper, Action.Rock), (Action.Scissors, Action.Paper)]:
            print(self.translations['win'])
            self.wins += 1
            self.results_history.append('win')
        else:
            print(self.translations['lose'])
            self.losses += 1
            self.results_history.append('lose')

    def display_stats(self):
        print(f"Wins: {self.wins}, Losses: {self.losses}, Draws: {self.draws}")

    def display_history(self):
        print("Results History:")
        print(", ".join(self.results_history))

    def play(self):
        try:
            while True:
                user_action = self.get_user_selection()
                computer_action = self.get_computer_selection()
                self.determine_winner(user_action, computer_action)

                play_again = input("Play again? (y/n): ")
                if play_again.lower() != "y":
                    break
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            exit()


if __name__ == "__main__":
    game = Game()
    game.play()
    game.display_stats()
    game.display_history()
