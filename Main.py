import random

from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Game'


class RockPaperScissorsGame:
    def __init__(self):
        self.totalwins = 0
        self.totallosses = 0
        self.options = ['rock', 'paper', 'scissors', 'jarrett']
        self.playerchoice = ""
        self.computerchoice = ""

    def setplayerchoice(self, choice):
        self.playerchoice = choice + ".png"

    def setcomputerchoice(self):
        self.computerchoice = random.choice(self.options)

    def getwinner(self):
        if self.playerchoice == self.computerchoice:
            return "It's a tie!"

        winconditions = {
            'rock': ['scissors', 'jarrett'],
            'paper': ['rock'],
            'scissors': ['paper'],
            'jarrett': ['paper', 'scissors']
        }

        if self.computerchoice in winconditions[self.playerchoice]:
            self.totalwins += 1
            return "You win!"
        else:
            self.totallosses += 1
            return "You lose!"


game = RockPaperScissorsGame()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/results')
def results():
    id_value = request.args.get('id')
    game.setplayerchoice(id_value)
    game.setcomputerchoice()

    session['playerchoice'] = game.playerchoice
    session['computerchoice'] = game.computerchoice
    session['result'] = game.getwinner()
    session['totalwins'] = game.totalwins
    session['totallosses'] = game.totallosses

    return render_template('results.html', ret_val=id_value)


@app.route('/reset')
def reset():
    game.totalwins = 0
    game.totallosses = 0
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
