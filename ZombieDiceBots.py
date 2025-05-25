import zombiedice
import randomprint
print("Name:Omkar")
print("USN:1AY24AI079")
print("Section:O")
class RandomBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        while True:
            roll = zombiedice.roll()
            if roll is None:
                break
            if random.random() < 0.5:
                break

class StopAfter2BrainsBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        while True:
            roll = zombiedice.roll()
            if roll is None:
                break
            for d in roll:
                if d['brain']:
                    brains += 1
            if brains >= 2:
                break

class StopAfterShotgunBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        while True:
            roll = zombiedice.roll()
            if roll is None:
                break
            for d in roll:
                if d['shotgun']:
                    shotguns += 1
            if shotguns >= 1:
                break

class RiskyBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0
        while shotguns < 2:
            roll = zombiedice.roll()
            if roll is None:
                break
            for d in roll:
                brains += d['brain']
                shotguns += d['shotgun']

class RollMax4TimesBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        rolls = 0
        while rolls < 4:
            roll = zombiedice.roll()
            if roll is None:
                break
            rolls += 1
