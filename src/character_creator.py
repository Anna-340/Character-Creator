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
    


