import random

from flask import Flask, render_template, request, flash, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'Game'

class RockPaperScissorsGame:
    def __init__(self):
        self.totalwins = 0
        self.totallosses = 0
        self.options = ['rock', 'paper', 'scissors', 'jarrett']
        self.playerchoice = None
        self.computerchoice = None

    def setplayerchoice(self, choice):
        self.playerchoice = choice

    def setcomputerchoice(self):
        self.computerchoice = random.choice(self.options)

    def getwinner(self):
        if self.playerchoice == self.computerchoice:
            return "It's a tie!"

        winconditions = {
            'rock': ['scissors', 'jarrett'],
            'paper': ['rock'],
            'scissors': ['paper'],
            'jarrett': ['paper','scissors']
        }

        if self.computerchoice in winconditions[self.playerchoice]:
            self.totalwins += 1
            return "You win!"
        else:
            self.totallosses += 1
            return "You lose!"

game = RockPaperScissorsGame()
#Test2
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/game')
def game_page():
    return render_template('game.html')


@app.route('/play')
def play(choice):
    game.setplayerchoice(choice)
    game.setcomputerchoice()

    session['player_choice'] = game.playerchoice
    session['computer_choice'] = game.computerchoice
    result = game.getwinner()
    session['result'] = result
    session['totalwins'] = game.totalwins
    session['totallosses'] = game.totallosses

    return redirect(url_for('results'))


@app.route('/results')
def results():
    player_choice = session.get('playerchoice')
    computer_choice = session.get('computerchoice')
    result = session.get('result')
    total_wins = session.get('totalwins')
    total_losses = session.get('totallosses')

    return render_template('results.html', player_choice=player_choice,
                           computer_choice=computer_choice, result=result,
                           total_wins=total_wins, total_losses=total_losses)


@app.route('/reset')
def reset():
    game.total_wins = 0
    game.total_losses = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()