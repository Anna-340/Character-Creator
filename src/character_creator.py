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
        self.root.title("Fantasy Character Creator! :D") 
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
        
        self.create_widgets()
        self.next_trait()
    
    def create_widgets(self):

        self.main_frame = ttk.Frame(self.root, padding= "20") #The main frame
        self.main_frame.pack(fill= tk.BOTH, expand= True)

        #The TITLE 
        ttk.Label(self.main_frame, text= "Fantasy Character Creator! :D", font= ("Arial", 16, "bold")).pack(pady= 10)

        #Displaying Traits
        self.trait_frame = ttk.LabelFrame(self.main_frame, text= "Character Trait")
        self.trait_frame.pack(fill= tk.X, pady= 10)

        self.trait_name_label = ttk.Label(self.trait_frame, text= "", front= ("Arial", 12))
        self.trait_name_label.pack(pady= 5)

        self.trait_value_label = ttk.Label(self.trait_frame, text= "", font= ("Arial", 14, "bold"))
        self.trait_value_label.pack(pady= 10)

        #DA Buttons for UI
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady= 20)

        self.regenerate_button = ttk.Button(self.button_frame, text= "Re-roll Trait!", command=self.regenerate_trait)
        self.regenerate_button.pack(side= tk.LEFT, padx= 10)

        #Progression of Character Traits
        self.progress_label = ttk.Label(self.main_frame, text= f"Progress; 0/{len(self.traits)} traits completed")
        self.progress_label.pack(pady= 10)

        #The Character Display
        self.character_frame = ttk.LabelFrame(self.main_frame, text= "Your Character!")
        self.stats_frame = ttk.LabelFrame(self.main_frame, text= "Character Stats!")
        self.quirk_frame = ttk.LabelFrame(self.main_frame, text= "Character Quirk")

        #Restart Button to create a new character!

        self.start_over_button = ttk.Button(self.main_frame, text= "Create Another Character!", command=self.start_over)
        
    def character_skin_tone(self):
        colors = ["Pale Blue", "Caramel", "Fair Skinned", "Milky", "Mocha", "Olive", "Tan", "Pale Pink",
                  "Light Gray", "Light Green", "Light Red", "Dark Blue", "Lavender", "Pale Orange",
                  "Dark Blue", "Galaxy", "Rainbow", "Pale Blue Fading to Black at the Tips",
                  "Turquoise", "Albaster", "Aubrun"]
        return random.choice(colors)
    
    def character_hair(self):
        colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink","Strawberry Blond", "White", 
                  "Black", "Raisin", "Liberty", "Chestnut", "Silver", "Dark Brown", "Golden Brown", "Blond",
                   "Sunset", "Honey", "Rose"]
        length = ["Bald", "Ear Tip Length", "Shoulder-Length", "Upper-Back", "Lower-Back", "Knee-Length", 
                  "Body-Length", "Short", "Medium", "Long"]
        return f"{random.choice(colors)}, {random.choice(length)}"
    
    def character_eye_color(self):
        colors = ["Brown", "Green", "Blue", "Completely Black", "Completely White", "Hazel", "Amber", "Gray",
                  "Violet", "Gold", "Silver", "Agate", "Heterochromia"]
        return random.choice(colors)
    
    def character_has_eyes(self):
        return random.choice(["Yes", "No"])
    
    def character_eyebrows(self):
        thickness = ["Thin", "Medium", "Thick", "Bushy"]
        shape = ["Arched", "Steep Arch", "S-Shaped", "Rounded", "Straight",
                     "Slit", "Soft Angled", "Curved Round", "Upward", "Tapered" "Natural"]
        return f"{random.choice(thickness)}, {random.choice(shape)}"
    
    def character_nose(self):
        shape = ["Aquiline", "Fleshy", "Straight", "Button", "Snub", "Hawk", "Roman", "Nubian", "Flat",
                  "Turned-up"]
        return random.choice(shape)
    
    def character_lips(self):
        lip_thickness = ["Thin", "Medium", "Full", "Very Full"]
        shape = ["Oval", "Wide", "Heart-Shaped", "Bow-Shaped", "Round", "Cupid's Bow", "Downward-Turned"]
        return f"{random.choice(lip_thickness)}, {random.choice(shape)}"
    
    def character_jawline(self):
        shape = ["Diamond", "Heart-Shaped", "Square", "Round", "Oval", "Triangular", "Oblong", "Narrow",]
        return random.choice(shape)
        
    def character_ears(self):
        size = ["Small", "Medium", "Large"]
        shape = ["Square", "Pointed", "Narrow", "Free-Lobe", "Attached-Lobe", "Elven", "Dwarf", "Gnome",
                 "Kender", "Half-Elf", "Orc", "Half-Orc", "Draconic", "Twilight-Elf", "Aquatic"]
        return f"{random.choice(size)}, {random.choice(shape)}"
    
    def character_horns(self):
        if random.random() < 0.25:
            number = random.randint(1, 4)
            size = ["Small", "Medium", "Large"]
            type = ["Draconic", "Antler", "Goat", "Markhor", "Pronghorn", "Orix", "Jacob-Sheep", "Chousingha",
                    "Bharal", "Hartebeest", "Spike", "Muskox", "Gnu", "Tur", "Gazelle", "Ibex", "Moose",
                    "Mule-Deer", "Bull", "Long", "Fallow-Deer", "Unicorn", "Sheep", "Mouflon", "Water-Buffalo"]
            return f"{number} {random.choice(size)}, {random.choice(type)} Horns"
        return "None"
    
    def character_wings(self):
        if random.random() > .25:
            size = ["Small", "Medium", "Large", "Massive"]
            type = ["Crystal", "Withered", "Dragon", "Bat", "Butterfly", "Moth", "Dragonfly", "Angel", "Bird",
                    "Insect", "Leathery", "Furry", "Flower", "Plant", "Rock", "Water", "Cloud", "Galaxy", 
                    "Star", "Flame", "Beetle", "Futuristic", "Translucent", "Metal", "3 Pairs of Angel Wings", 
                    "2 Pairs of Angel Wings" ]
            return f"{size} {random.choice(size)} Wings ({random.choice(type)})"
        return "None"
    
    def character_skin_texture(self):
        texture = ["Clear", "Acne", "Scars", "Freckles", "Birthmarks", "Fur", "Scales", "Tattoos", "Moles", 
                   "Vitiligo"]
        return random.choice(texture)
    
    def character_hands(self):
        fingers = [ "4 Fingers", "5 Fingers", "6 Fingers"]
        type = ["Thick", "Short", "Long", "Slender", "Calloused", "Elegant", "Clawed", "Stubby"]
        return f"{random.choice(fingers)}, {random.choice(type)}"