#! /usr/bin python3

# It is considered best practice to put all imports at the top of file not mixed in or right before it is actually
# needed, even though you technically could.
import random

# Written by Tish Soulliard November 2021

# It is standard practice to write constants with all caps.  It indicates these values should never change inside the
# code.  Also, if use a tuple (a list in () instead of []) it makes it 'immutable' which means it can't be altered.
# You can't add to or remove items from the list.
STATS = ("Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma")
# This is a dictionary.  It contains Key=Value pairs.  The Key must be a unique string the value can be anything.
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
    """
    Npc Class
    This is used to store all the information and methods associated with an npc.
    """
    def __init__(self, name, race, profession):
        """
        When you call a class initiator you are creating an object.  In this case in order to create a npc object
        you need to pass a name, race and profession (aka class - but class is a python key word so you can't use it
        directly)

        :param name: The name of the NPC
        :param race: The race of the NPC
        :param profession: The class of the NPC
        """
        self.name = name
        self.race = race
        self.profession = profession
        # in order to create some random stats we will call the populate_stats function.  This function does not need
        # any information from this object so it is not a method associated with the class it is it's own function.
        self.stat = populate_stats()
        # in order to create some random bonus stats we will call __populate_bonus.  This function does use values
        # associated with the object, so it is a method of the class.
        self.bonus = self.__populate_bonus()
        self.armor_class = self.bonus['Dexterity'] + 8
        self.hit_points = self.bonus['Constitution'] + 8
        self.skills = self.__populate_skills()
        self.attitude = random.choice(ATTITUDES)
        self.appearance = random.choice(APPEARANCES)
        self.hobby = random.choice(HOBBIES)

    def __populate_bonus(self):
        """
        This will use the object's stats values to create some bonus stats.  This is a private method.  The __ at the
        start of the  method name indicates this.  It means it should not be called by any code outside of the class.
        It is just a naming convention and is not actually enforced by
        python in any way.  __ (is called dunder).

        :return: a dictonary containing the bonus stat values.
        """
        # create an empty dictionary
        bonus = {}
        # cycle through each of the stats in the STATS tuple
        for stat in STATS:
            # calculate a bonus stat value based on the provided base stat.
            bonus[stat] = (int(self.stat[stat]) // 2) - 5
        return bonus

    def __populate_skills(self):
        """
        This will use the object's bonus stat values to create some skill stats.  This is a private method.
        The __ at the start of the  method name indicates this.  It means it should not be called by any code outside
        of the class. It is just a naming convention and is not actually enforced by python in any way.
        __ (is called dunder).

        :return: a dictonary containing the skill stat values.
        """
        # create an empty dictionary
        skills = {}
        # cycle through each of the skills in SKILLS dictionary.  Since we are iterating over the .items() list it
        # provides a key and value pair at a time.
        for skill, stat in SKILLS.items():
            # calculate a skill value based on the correct bonus stat as provided by the STATS dictonary.
            skills[skill] = random.randint(1, 20) + self.bonus[stat]
        return skills

    def __repr__(self):
        """
        This is a default/built in method that all classes have, but you can overwrite.  When you over write it, the
        value you return is what will be used when you try to print the object, or try to represent it as a string.

        :return: A string representing the object.
        """
        output = f"Behold, {self.name} the {self.race} {self.profession} is here!\n"
        # if you += a string it just appends the right string to the left string.
        output += "NPC stat modifiers "
        # Cycling through each stat rather than typing them manually.
        for stat in STATS:
            sta = stat[0:3].upper()
            output += f"{sta} {self.bonus[stat]} | "
        # In this case we don't want the last '| ' that is now on the string, so we are creating a substring that starts
        # at the beginning of the output string and ends -2 spaces from the end.  In python the start number is assumed
        # to be 0 if not declared.  Also, the end number is NOT included in the resulting string (or array).
        output = output[:-2]
        output += f"\nNatural AC is {self.armor_class} and HP is {self.hit_points}\n\n"
        output += f"{self.name} has a {self.appearance} appearance and looks to be {self.attitude}\n"
        output += f"{self.name}'s hobbies include {self.hobby}\n\n"
        output += "---Skill Checks---\n\n"
        # Cycling through each of the skills in the SKILLS dictonary.  This time we don't need the value just the key.
        for skill in SKILLS.keys():
            output += f"{skill} check is {self.skills[skill]}\n"
        output += "\n"
        return output


def populate_stats():
    """
    This function does not require explicit knowledge of the object so it is  not a part of the class definition.

    :return: a dictonary containing random stats values.
    """
    stat_value = {}
    for stat in STATS:
        stat_value[stat] = random.randint(5, 14)
    return stat_value
