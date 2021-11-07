#! /usr/bin python3

# the npc_class file that contains the Npc class I created is inside the character directory.  So character is the name
# of the module and then npc_class is a feature of the module that you can import.  If you had just imported character
# then when you try to create the npc object you would have to do it like this
# npc = character.npc_class.Npc(char_name, char_race, char_class)

from character import npc_class

# Re-written by Tish Soulliard November 2021


def main():
    print('NPC GENERATOR\n')

    # Setting a boolean that will controll the while loop which is used for creating new npc objects.
    create_npc = True
    # Creating an empty list to store all the npc objects that are created.
    npc_list = []
    while create_npc:
        char_name = input('NPC name? ')
        char_race = input('What race is the npc? ')
        char_class = input('What profession does the npc have? ')

        # Creating the npc object based on the given name, race, and class
        npc = npc_class.Npc(char_name, char_race, char_class)
        # Print to screen the npc object - this comes from the __repr__ method
        print(f"\n{npc}")
        # Add this npc to the npc_list list, for use later if we want.
        npc_list.append(npc)

        make_another = input('Make another NPC? ').lower()
        if not (make_another == "yes" or make_another == "y"):
            # if make_another is not yes or y then create_npc will be set to False which will break us out of the while
            # loop.
            create_npc = False

    # I added this section to show you a few more things.
    # Ask if you want to save the npc's you've created to a file.
    write = input('Would you like to write the character(s) to a file?').lower()
    if write == "yes" or write == "y":
        # If they do want to save, ask what filename.
        filename = input("Filename?")
        # if you use with open, then when you break out of the with scope it will automatically close the file, you
        # don't need to do it manually, so when possible this is considered a best practice.
        # When python opens a file with 'w' it will overwrite any pre-existing file with that name.  I have not written
        # any sort of check, so be careful what you name the file.
        with open(filename, "w") as outfile:
            # cycle through each created npc object and write it to the file.
            for npc in npc_list:
                outfile.write(f"{npc}")


main()
