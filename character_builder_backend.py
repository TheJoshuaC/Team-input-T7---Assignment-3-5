import sys
import random

class CharacterBuilder():
    def roll_stats():
      stats = []
      for i in range(6):
        stat = sum(sorted(random.sample(range(1, 7), 4))[1:])
        stats.append(stat)
      return stats

    def load(a,character):
        try:
            with open(a,"r") as file_object:
                pass
        except:
            pass
        else:
            with open(a,"r") as file_object:
                for line in file_object:
                    line=line.strip()
                    fields=line.split(",")
                    character.race=fields[0]
                    character.job=fields[1]
                    character.firstname=fields[2]
                    character.lastname =fields[3]
                    character.str =fields[4]
                    character.dex =fields[5]
                    character.con =fields[6]
                    character.int =fields[7]
                    character.wis =fields[8]
                    character.cha =fields[9]
                    character.alignment =fields[10]
                    character.motivation =fields[11]
                    #equip
                    character.head =fields[12]
                    character.armor =fields[13]
                    character.arms =fields[14]
                    character.legs =fields[15]
                    character.feet =fields[16]
                    character.lhand =fields[17]
                    character.rhand =fields[18]
    def save(a,character):
        theFile=open(a, "w")
        theFile.write(str(character.race)+","+str(character.job)+","+str(character.firstname)+","+str(character.lastname)+","+str(character.str)+","+str(character.dex)+","+str(character.con)+","+str(character.int)+","+str(character.wis)+","+str(character.cha)+","+str(character.alignment)+","+str(character.motivation)+","+str(character.head)+","+str(character.armor)+","+str(character.arms)+","+str(character.legs)+","+str(character.feet)+","+str(character.lhand)+","+str(character.rhand)+"\n")
        theFile.close()   

    def numcheck(x):
        if x not in [1, 2, 3, 4, 5]:
            return False
        else:
            return True
    def numcheckrace(x):
        if x not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        else:
            return True
    def numcheckclass(x):
        if x not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            return False
        else:
            return True 
    def display(x):
        race = 12
        job = 12
        firstname = 12
        lastname = 12
        stre = 12
        dex = 12
        con = 12
        inte = 12
        wis = 12
        cha = 12
        alignment = 12
        motivation = 12
        #equip
        head = 12
        armor = 12
        arms = 12
        legs = 12
        feet = 12
        lhand = 12
        rhand = 12
        column_format="{:<"+str(race)+"} {:<"+str(job)+"} {:<"+str(firstname)+"} {:<"+str(lastname)+"} {:<"+str(stre)+"} {:<"+str(dex)+"} {:<"+str(con)+"} {:<"+str(inte)+"} {:<"+str(wis)+"} {:<"+str(cha)+"} {:<"+str(alignment)+"} {:<"+str(motivation)+"}\n"
        row_text=column_format.format("-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------")
        sys.stdout.write(row_text)
        row_text=column_format.format("Race","Class","First Name","Last Name","Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma","Alignment","Motivation")
        sys.stdout.write(row_text)
        row_text=column_format.format("-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------","-----------")
        sys.stdout.write(row_text)
        row_text=column_format.format(str(x.race),str(x.job),str(x.firstname),str(x.lastname),str(x.str),str(x.dex),str(x.con),str(x.int),str(x.wis),str(x.cha),str(x.alignment),str(x.motivation))
        sys.stdout.write(row_text)
        column_format="{:<"+str(head)+"} {:<"+str(armor)+"} {:<"+str(arms)+"} {:<"+str(legs)+"} {:<"+str(feet)+"} {:<"+str(lhand)+"} {:<"+str(rhand)+"}\n"
        row_text=column_format.format("-----------","-----------","-----------","-----------","-----------","-----------","-----------")
        sys.stdout.write(row_text)
        row_text=column_format.format("Head Gear","Armor","Arms","Legs","Feet","Left hand","Right Hand")
        sys.stdout.write(row_text)
        row_text=column_format.format("-----------","-----------","-----------","-----------","-----------","-----------","-----------")
        sys.stdout.write(row_text)
        row_text=column_format.format(str(x.head),str(x.armor),str(x.arms),str(x.legs),str(x.feet),str(x.lhand),str(x.rhand))
        sys.stdout.write(row_text)

class Character():
    race = None
    job = None
    firstname = None
    lastname = None
    str = 0
    dex = 0
    con = 0
    int = 0
    wis = 0
    cha = 0
    alignment = None
    motivation = "None"
    #equip
    head = None
    armor = None
    arms = None
    legs = None
    feet = None
    lhand = None
    rhand = None

    def __init__(self,race,job,firstname,lastname,str,dex,con,int,wis,cha,alignment,motivation,head,armor,arms,legs,feet,lhand,rhand):
        self.race = race
        self.job = job
        self.firstname = firstname
        self.lastname = lastname
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.alignment = alignment
        self.motivation = motivation
        #equip
        self.head = head
        self.armor = armor
        self.arms = arms
        self.legs = legs
        self.feet = feet
        self.lhand = lhand
        self.rhand = rhand
class Job():
    name=None
    desc=None
    def __init__(self,name,desc):
        self.name=name
        self.desc=desc

class Ability():
    name = None
    desc = "None"
    def __init__(self,name,desc):
        self.name=name
        self.desc=desc


#jobs
Barbarian=Job("Barbarian","Haha axe man funny")        
