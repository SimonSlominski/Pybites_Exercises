

class Roll:

    def __init__(self, name):
        self.name = name

    def defeat_rules(self, p2_roll):
        wins = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }

        if p2_roll.name == wins[self.name]:
            return True
        else:
            return False


class Player:

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

