import random
from enum import IntEnum
import json
from datetime import datetime


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
        self.stats_history = []

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
            result = 'tie'
            self.draws += 1
        elif (user_action, computer_action) in [(Action.Rock, Action.Scissors), (Action.Paper, Action.Rock), (Action.Scissors, Action.Paper)]:
            result = 'win'
            self.wins += 1
        else:
            result = 'lose'
            self.losses += 1

        series_wins = self.calculate_series_wins(result)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.results_history.append({'timestamp': timestamp, 'result': result, 'series_wins': series_wins})
        self.stats_history.append({'timestamp': timestamp, 'wins': self.wins, 'losses': self.losses, 'draws': self.draws})

    def calculate_series_wins(self, result):
        # One Day I will do that
        return 0

    def display_stats(self):
        print(f"Wins: {self.wins}, Losses: {self.losses}, Draws: {self.draws}")

    def display_history(self):
        print("Results History:")
        for entry in self.results_history:
            print(entry)

        print("\nStats History:")
        for entry in self.stats_history:
            print(entry)

    def save_history_to_json(self):
        data = {
            'results_history': self.results_history,
            'stats_history': self.stats_history
        }

        with open('history.json', 'w') as file:
            json.dump(data, file, indent=4)

    def play(self):
        try:
            while True:
                user_action = self.get_user_selection()
                computer_action = self.get_computer_selection()
                self.determine_winner(user_action, computer_action)

                play_again = input("Play again? (y/n): ")
                if play_again.lower() != "y":
                    self.save_history_to_json()
                    break
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            self.save_history_to_json()
            exit()


if __name__ == "__main__":
    game = Game()
    game.play()
    game.display_stats()
    game.display_history()
