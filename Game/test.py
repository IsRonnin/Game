ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
         "Elite", "Conqueror", "Champion", "Master", "Greatest"]


class Warrior():
    def __init__(self):
        self.experience = 100
        if self.experience > 10000:
            self.experience = 10000
        self.experience = 100
        self.level = self.experience // 100
        self.rank = ranks[self.level // 10]
        self.achievements = []

    def __call__(self, *args, **kwargs):
        print(self.experience)
        print(self.level)
        print(self.rank)
        print(self.achievements)

    def training(self, d):
        print(d)
        description = d[0]
        expa = d[1]
        level = d[2]
        if level > self.level:
            return "Not strong enough"
        self.experience += expa
        self.level = self.experience // 100
        if self.level > 100:
            self.level = 100
            self.experience = 10000
        self.rank = ranks[self.level // 10]
        self.achievements.append(description)
        return description

    def battle(self, o_lvl):
        print(o_lvl)
        if o_lvl not in range(1, 101):
            return "Invalid level"
        if o_lvl // 10 > self.level // 10 and o_lvl >= self.level + 5:
            return "You've been defeated"
        if o_lvl >= self.level + 1:
            self.experience += 20 * (o_lvl-self.level) * (o_lvl-self.level)
            self.level = self.experience // 100
            if self.level > 100:
                self.level = 100
                self.experience = 10000
            self.rank = ranks[self.level // 10]
            return "An intense fight"
        if o_lvl == self.level:
            self.experience += 10
            self.level = self.experience // 100
            if self.level > 100:
                self.level = 100
                self.experience = 10000
            self.rank = ranks[self.level // 10]
            return "A good fight"
        if o_lvl == self.level - 1:
            self.experience += 5
            self.level = self.experience // 100
            if self.level > 100:
                self.level = 100
                self.experience = 10000
            self.rank = ranks[self.level // 10]
            return "A good fight"
        if o_lvl <= self.level - 2:
            return "Easy fight"