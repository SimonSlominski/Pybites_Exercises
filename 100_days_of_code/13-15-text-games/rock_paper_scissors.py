from rock_paper_scissors_classes import Player, Roll
import random


def print_intro():
    print('---------------------------')
    print('*** Rock Paper Scissors ***')
    print('---------------------------')


def available_rolls():
    paper = Roll('paper')
    rock = Roll('rock')
    scissors = Roll('scissors')
    rolls = [paper, rock, scissors]
    return rolls


def get_player_name():
    name = input('Enter your name').capitalize()
    return name


def get_player_roll():
    inp = input("Choose a roll: [r]ock, [p]aper, [s]cissors")

    if inp == 'r':
        return Roll('rock')
    elif inp == 'p':
        return Roll('paper')
    elif inp == 's':
        return Roll('scissors')

    # choices = ['r', 'p', 's']
    #
    # if inp not in choices:
    #     print("")

def game(player1, player2, rolls):
    count = 0
    while count < 3:
        print(f"Round {count+1} ")
        p1_roll = get_player_roll()
        p2_roll = random.choice(rolls)

        print(f'Player 1 throw: {p1_roll.name}')
        print(f'Computer throw: {p2_roll.name}')

        # Check for tie
        if p1_roll.name == p2_roll.name:
            print('Tie! The round will be repeated')
            continue

        # Check for winner
        p1_win = p1_roll.defeat_rules(p2_roll)

        # Display winner for this round
        if p1_win:
            print(f'{player1.name} wind this round with {p1_roll.name} defeating {p2_roll.name}')
            player1.score += 1

        else:
            print(f'{player2.name} wins this round with {p2_roll.name} defeating {p1_roll.name}')
            player2.score += 1

        count += 1

        # Pick the winner
        if player1.score == 2:
            print(f"{player1.name} is the winner by winning {player1.score} to {player2.score}")
            break

        if player2.score == 2:
            print(f"{player2.name} is the winner by winning {player2.score} to {player1.score}")
            break


def main():
    print_intro()

    rolls = available_rolls()

    name = get_player_name()

    player1 = Player(name)
    player2 = Player("BAYMAX")

    game(player1, player2, rolls)


if __name__ == '__main__':
    main()
