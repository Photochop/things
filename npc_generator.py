#! /usr/bin python3

from character import npc_class


# Re-written by Tish Soulliard November 2021


def main():
    print('NPC GENERATOR\n')

    create_npc = True
    npc_list = []
    while create_npc:
        char_name = input('NPC name? ')
        char_race = input('What race is the npc? ')
        char_class = input('What profession does the npc have? ')

        npc = npc_class.Npc(char_name, char_race, char_class)
        print(f"\n{npc}")
        npc_list.append(npc)

        restart = input('Make another NPC? ').lower()
        if not (restart == "yes" or restart == "y"):
            create_npc = False

    write = input('Would you like to write the characters to a file?').lower()
    if write == "yes" or write == "y":
        filename = input("Filename?")
        with open(filename, "w") as outfile:
            for npc in npc_list:
                outfile.write(f"{npc}")


main()
