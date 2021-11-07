#! /usr/bin python3

import random

# Written by Tish Soulliard November 2021

STATS = ("Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma")
SKILLS = {'Acrobatics': 'Dexterity',
          'Athletics': 'Strength',
          'Arcana': 'Intelligence',
          'History': 'Intelligence',
          'Medicine': 'Wisdom',
          'Survival': 'Wisdom',
          'Animal Handling': "Wisdom",
          'Stealth': 'Dexterity',
          'Slight of Hand': 'Dexterity',
          'Intimidation': 'Charisma',
          'Persuasion': 'Charisma',
          'Deception': 'Charisma',
          'Perception': 'Wisdom',
          'Religion': 'Intelligence',
          'Investigation': 'Intelligence',
          'Insight': 'Wisdom',
          'Nature': 'Wisdom',
          'Performance': 'Charisma'
          }
ATTITUDES = ('friendly', 'calm', 'sad', 'tired', 'sick', 'excited', 'upset', 'anxious')
APPEARANCES = ('well groomed', 'disheveled', 'fashionable', 'out of date', 'rural')
HOBBIES = ('painting', 'writing', 'music', 'fishing', 'tinkering', 'research', 'building', 'having pets', 'baking',
           'gambling', 'drinking', 'going to temple', 'swimming', 'riding', 'dancing', 'singing', 'going for walks',
           'sparring')


class Npc:
    def __init__(self, name, race, profession):
        self.name = name
        self.race = race
        self.profession = profession
        self.stat = populate_stats()
        self.bonus = self.__populate_bonus()
        self.armor_class = self.bonus['Dexterity'] + 8
        self.hit_points = self.bonus['Constitution'] + 8
        self.skills = self.__populate_skills()
        self.attitude = random.choice(ATTITUDES)
        self.appearance = random.choice(APPEARANCES)
        self.hobby = random.choice(HOBBIES)

    def __populate_bonus(self):
        bonus = {}
        for stat in STATS:
            bonus[stat] = (int(self.stat[stat]) // 2) - 5
        return bonus

    def __populate_skills(self):
        skills = {}
        for skill, stat in SKILLS.items():
            skills[skill] = random.randint(1, 20) + self.bonus[stat]
        return skills

    def __repr__(self):
        output = f"Behold, {self.name} the {self.race} {self.profession} is here!\n"
        output += "NPC stat modifiers "
        for stat in STATS:
            sta = stat[0:3].upper()
            output += f"{sta} {self.bonus[stat]} | "
        output = output[:-2]
        output += f"\nNatural AC is {self.armor_class} and HP is {self.hit_points}\n\n"
        output += f"{self.name} has a {self.appearance} appearance and looks to be {self.attitude}\n"
        output += f"{self.name}'s hobbies include {self.hobby}\n\n"
        output += "---Skill Checks---\n\n"
        for skill in SKILLS.keys():
            output += f"{skill} check is {self.skills[skill]}\n"
        output += "\n"
        return output


def populate_stats():
    stat_value = {}
    for stat in STATS:
        stat_value[stat] = random.randint(5, 14)
    return stat_value
