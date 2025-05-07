import random
from enum import Enum
import tkinter as tk
from tkinter import ttk, messagebox

class TypeClass(Enum):
    NONE = "No Magic(Villager)"
    WIZARD = "Wizard"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    NECROMANCER = "Necromancer"
    CLERIC = "Cleric"
    PREIST = "Preist"
    MONK = "Monk"
    DRUID = "Druid"
    BARD = "Bard"
    RANGER = "Ranger"
    PALADIN = "Paladin"
    ARTIFICER = "Artificer"
    ROUGE = "Rouge"
    BARBARIAN = "Barbarian"
    FIGHTER = "Fighter"
    DUNGEONMASTER = "Dungeon Master"

class Jobs(Enum):
    SCAM = "Con Artist"
    RETAIL = "Retail Worker"
    BARISTA = "Barista"
    CASHIER = "Cashier"
    WAITER = "Waiter"
    MAID = "Maid"
    JANITOR = "Janitor"
    BAR = "Bar Tender"
    GRAVE = "Grave Digger"
    OFFICE = "Office Worker"
    FASTFOOD = "Fast Food Employee"
    LIBRARIAN = "Librarian"
    COLLEGE = "College Professor"
    ZOOKEEPER = "Zoo Keeper"
    HORSE = "Horse Racer"
    RANCHER = "Cowboy"
    HORSETAMER = "Horse Tamer"
    DRAGON = "Dragon Tamer"
    BOTANIST = "Botanist"
    SMUGGLER = "Smuggler"
    PLANTGROWER = "Marijuana and Shroom Grower"
    KNIGHT = "Knight"
    ARTIST = "Artist"
    MERCHANT = "Merchant"
    SECURITY = "Security Guard"
    CLOWN = "Circus Act"

    class PersonalityTraits(Enum):
        HAPPY = "Happy"
        DEPRESSED = "Depressed"
        ANXIOUS = "Anxious;"
        EXTROVERTED = "Extroverted"
        INTROVERTED = "Introverted"
        LAIDBACK = "Laidback"
        DETERMINED = "Determined"
        STUBBORN = "Stubborn"
        PUREHEARTED = "Pure Hearted"
        BLUNT = "Blunt"
        TRUTHFUL = "Truthful"
        CRUEL = "Cruel"
        RIZZ = "Charisma"
        MORBID = "Morbid"
        COMEDIC = "Comedic"
        SERIOUS = "Serious"
        PLAYFUL = "Playful"
        CHILDISH = "Childish"
        PRIDEFUL = "Prideful"
        ARROGANT = "Arrogant"
        MYSTERIOUS = "Mysterious."

class CharacterCreator: 
    def __init__(self, root):
        self.root = root
        self.root.title{"Fantasy Character Creator! :D"}
        self.root.geometry("800 x 700")

        self.character = {}
        self.current_trait = "",
        self.traits = ["Gender", "Age", "Height", "Skin Color", "Hair", "Has Eyes", "Eye Color", "Evebrows",
                       "Nose", "Lips", "Jawline", "Ears", "Horns", "Skin Texture", "Hands", "Wimgs", "Tail",
                       "Magic Class", "Job", "Personality", "Quirk"]
        
        self.stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma", "Stealth"]

        self.quirks = ["Snors louldy when sleeping", "Fidgets with thumbs when nervous", "Hums when thinking", 
                       "Sticks tounge out when focused", "Talks to themselves", "Collects things off the ground",
                       "Hates when people smack", "Always cold", "Always hot", "Always late", "Always early", 
                       "Over complicates things", "Laughs at the wrong times", "Bad at remembering names", 
                       "Obsessive with organizing thing", "Can't keep eye contact for long periods of time", 
                        "Always pops their joints", "Fear of heights", "Scared of the dark", "Has a sweet tooth",
                         "Judgey of others", "Sleepwalker", "Very blunt", "Nail biter", 
                         "Steals other peoples food when they aren't looking"]
