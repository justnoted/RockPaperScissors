class RockPaperScissorsGame:
    def __init__(self):
        self.total_wins = 0
        self.total_losses = 0
        self.options = ['rock', 'paper', 'scissors']

    def howToPlay(self, player, computer):
        options = {
            'rock': {'rock': 'draw', 'paper': 'lose', 'scissors': 'win'},
            'paper': {'rock': 'win', 'paper': 'draw', 'scissors': 'lose'},
            'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'draw'},
        }

    result = options;