import sys
from character_builder_backend import CharacterBuilder
from character_builder_backend import Character

class CharacterBuilderUi():
    def main():
        menuExit = False
        fileLoaded = False
        character=Character(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        while menuExit == False:
            sys.stdout.write("Menu \n===\n1. Load file \n2. Display character stats\n3. Redo Stats\n4. Save to file\n5. Exit\nChoice: ")
            numberInput=int(sys.stdin.readline().strip())
            if CharacterBuilder.numcheck(numberInput) == False:
                sys.stdout.write(str(numberInput)+" is not a valid input \n")
            if numberInput == 1:
                sys.stdout.write("What character do you wish to load or create? ")
                requestedFile=sys.stdin.readline().strip("\n")
                CharacterBuilder.load(requestedFile,character)
                sys.stdout.write("loaded "+requestedFile+"\n")
                fileLoaded = True
            if numberInput == 2:
                CharacterBuilder.display(character)
            if numberInput == 3:
                character=Character(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                sys.stdout.write("Pick a race:\n1. Dwarf \n2. Elf \n3. Halfling \n4. Human \n5. Dragonborn \n6. Gnome \n7. Half-Elf \n8. Half-Orc \n9. Tiefling \n")
                numberInputrace=int(sys.stdin.readline().strip())
                if CharacterBuilder.numcheckrace(numberInputrace) == False:
                    sys.stdout.write(str(numberInputrace)+" is not a valid input \n")
                    numberInputrace=(sys.stdin.readline().strip("\n"))
                else:
                    if numberInputrace == 1:
                        character.race="Dwarf"
                        character.con=2
                        character.wis=1
                    if numberInputrace == 2:
                        character.race="Elf"
                        character.dex=2
                        character.wis=1                    
                    if numberInputrace == 3:
                        character.race="Halfling"
                        character.dex=2
                        character.cha=1
                    if numberInputrace == 4:
                        character.race="Human"
                        character.str=1
                        character.dex=1
                        character.con=1
                        character.int=1
                        character.wis=1
                        character.cha=1
                    if numberInputrace == 5:
                        character.race="Dragonborn"
                        character.str=2
                        character.cha=1
                    if numberInputrace == 6:
                        character.race="Gnome"
                        character.int=2
                        character.con=1
                    if numberInputrace == 7:
                        character.race="Half-Elf"
                        character.cha=2
                        character.wis=1
                        character.int=1
                    if numberInputrace == 8:
                        character.race="Half Orc"
                        character.str=2
                        character.con=1
                    if numberInputrace == 9:
                        character.race="Tiefling"
                        character.int=1
                        character.cha=2
                    sys.stdout.write("Pick a class:\n1. Barbarian \n2. Bard \n3. Cleric \n4. Druid \n5. Fighter \n6. Monk \n7. Paladin \n8. Ranger \n9. Rogue \n10. Sorcerer \n11. Warlock \n12. Wizard \n")
                    numberInputclass=int(sys.stdin.readline().strip())
                    if CharacterBuilder.numcheckclass(numberInputclass) == False:
                        sys.stdout.write(str(numberInputclass)+" is not a valid input \n")
                        numberInputclass=(sys.stdin.readline().strip("\n"))
                    else:
                        if numberInputclass == 1:
                            character.job="Barbarian"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand=None
                            character.rhand="Iron club"
                        if numberInputclass == 2:
                            character.job="Bard"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand=None
                            character.rhand="Wooden Bow"
                        if numberInputclass == 3:
                            character.job="Cleric"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand=None
                            character.rhand="Iron club"
                        if numberInputclass == 4:
                            character.job="Druid"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand=None
                            character.rhand="Iron club"
                        if numberInputclass == 5:
                            character.job="Fighter"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand=None
                            character.rhand="Iron club"
                        if numberInputclass == 6:
                            character.job="Monk"
                            character.head=None
                            character.armor="Simple Robes"
                            character.arms=None
                            character.legs=None
                            character.feet="Sandals"
                            character.lhand=None
                            character.rhand="Shortsword"
                        if numberInputclass == 7:
                            character.job="Paladin"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand=None
                            character.rhand="Iron club"
                        if numberInputclass == 8:
                            character.job="Ranger"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand="Shield"
                            character.rhand="Iron club"
                        if numberInputclass == 9:
                            character.job="Rogue"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand="Dagger"
                            character.rhand="Crossbow"
                        if numberInputclass == 10:
                            character.job="Sorcerer"
                            character.head=None
                            character.armor="Simple Robes"
                            character.arms=None
                            character.legs=None
                            character.feet=None
                            character.lhand=None
                            character.rhand="Wooden Quaterstaff"
                        if numberInputclass == 11:
                            character.job="Warlock"
                            character.head="Leather Helmet"
                            character.armor="Fur Armor"
                            character.arms="Fur Bracers"
                            character.legs="Fur Pants"
                            character.feet="Fur Boots"
                            character.lhand=None
                            character.rhand="Iron club"
                        if numberInputclass == 12:
                            character.job="Wizard"
                            character.head=None
                            character.armor="Simple Robes"
                            character.arms=None
                            character.legs=None
                            character.feet=None
                            character.lhand=None
                            character.rhand="Wooden Quaterstaff"
                    sys.stdout.write("First name:")
                    character.firstname=str(sys.stdin.readline().strip())
                    sys.stdout.write("Last name:")
                    character.lastname=str(sys.stdin.readline().strip())
                    sys.stdout.write("Now it's time to roll your stats. you will recieve 6 numbers, allocate them to your stats when prompted. Feel free to adjust your rolls *slightly* if you feel fate did you dirty\n")
                    print(CharacterBuilder.roll_stats())
                    sys.stdout.write("\nStrength:")
                    number=int(sys.stdin.readline().strip())
                    character.str += number
                    sys.stdout.write("\nDexterity:")
                    number=int(sys.stdin.readline().strip())
                    character.dex += number
                    sys.stdout.write("\nConstitution:")
                    number=int(sys.stdin.readline().strip())
                    character.con += number
                    sys.stdout.write("\nIntelligence:")
                    number=int(sys.stdin.readline().strip())
                    character.int += number
                    sys.stdout.write("\nWisdom:")
                    number=int(sys.stdin.readline().strip())
                    character.wis += number
                    sys.stdout.write("\nCharisma:")
                    number=int(sys.stdin.readline().strip())
                    character.cha += number
                    sys.stdout.write("What is your characters alignment?")
                    character.alignment=str(sys.stdin.readline().strip())
                    sys.stdout.write("In one sentence, what is your characters motivation?")
                    character.motivation=str(sys.stdin.readline().strip())                    

                                     
            if numberInput == 4:
                if fileLoaded == False:
                    sys.stdout.write("Load a file first! \n")
                else:
                    sys.stdout.write("Saving to "+str(requestedFile)+"\n")
                    CharacterBuilder.save(requestedFile,character)
            if numberInput == 5:
                break
CharacterBuilderUi.main()
