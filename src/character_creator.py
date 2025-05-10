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
    PLANTGROWER = "Marijuana And Shroom Grower"
    KNIGHT = "Knight"
    ARTIST = "Artist"
    MERCHANT = "Merchant"
    SECURITY = "Security Guard"
    CLOWN = "Circus Act"

class PersonalityTraits(Enum):
    HAPPY = "Happy"
    DEPRESSED = "Depressed"
    ANXIOUS = "Anxious"
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
    MYSTERIOUS = "Mysterious"

class CharacterCreator: 
    def __init__(self, root):
        self.root = root
        self.root.title("Fantasy Character Creator! :D") 
        self.root.geometry("800x700")

        self.character = {}
        self.current_trait = ""
        self.traits = ["Gender", "Age", "Height", "Skin Color", "Hair", "Has Eyes", "Eye Color", "Eyebrows",
                       "Nose", "Lips", "Jawline", "Ears", "Horns", "Skin Texture", "Hands", "Wings", "Tail",
                       "Magic Class", "Job", "Personality", "Quirk"]
        
        self.stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma", "Stealth"]

        self.quirks = ["Snores Louldy When Sleeping", "Fidgets With Thumbs When Nervous", 
                       "Hums When Thinking", "Sticks Tounge Out When Focused", "Talks To Themselves", 
                       "Collects Things Off The Ground", "Hates When People Smack", "Always Cold", 
                       "Always Hot", "Always Late", "Always Early", "Over Complicates Things", 
                       "Laughs At The Wrong Time", "Bad At Remembering Names", 
                       "Obsessive With Organizing Things","Can't Keep Eye Contact For Long Periods Of Time", 
                       "Always Pop Their Joints", "Fear Of Heights", "Scared Of The Dark", 
                       "Has A Sweet Tooth", "Judgey Of Others", "Sleepwalker", "Very Blunt", "Nail Biter", 
                       "Steals Other Peoples Food When They Aren't Looking"]
        
        self.create_widgets()
        self.next_trait()
    
    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding= "20") #The main frame
        self.main_frame.pack(fill= tk.BOTH, expand= True)

        #The TITLE 
        ttk.Label(self.main_frame, text= "Fantasy Character Creator! :D", 
                  font= ("Arial", 16, "bold")).pack(pady= 10)

        #Displaying Traits
        self.trait_frame = ttk.LabelFrame(self.main_frame, text= "Character Trait")
        self.trait_frame.pack(fill= tk.X, pady= 10)

        self.trait_name_label = ttk.Label(self.trait_frame, text= "", font= ("Arial", 12))
        self.trait_name_label.pack(pady= 5)

        self.trait_value_label = ttk.Label(self.trait_frame, text= "", font= ("Arial", 14, "bold"))
        self.trait_value_label.pack(pady= 10)

        #DA Buttons for UI
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady= 20)

        self.regenerate_button = ttk.Button(self.button_frame, text= "Re-Roll Trait!", 
                                            command= self.reroll_trait)
        self.regenerate_button.pack(side= tk.LEFT, padx= 10)

        self.accept_button = ttk.Button(self.button_frame, text= "Accept Trait", command= self.accept_trait)
        self.accept_button.pack(side= tk.LEFT, padx= 10)

        #Progression of Character Traits
        self.progress_label = ttk.Label(self.main_frame, 
                                        text= f"Progress: 0/{len(self.traits)} Traits Completed!")
        self.progress_label.pack(pady= 10)

        #The Character Display
        self.character_frame = ttk.LabelFrame(self.main_frame, text= "Your Character!")
        self.stats_frame = ttk.LabelFrame(self.main_frame, text= "Character Stats!")
        self.quirk_frame = ttk.LabelFrame(self.main_frame, text= "Character Quirk")

        #Restart Button to create a new character!

        self.start_over_button = ttk.Button(self.main_frame, text= "Create Another Character!", 
                                            command=self.restart_character)
    
    def close_app(self):
        self.root.destroy()

    def character_skin_tone(self):
        colors = ["Pale Blue", "Caramel", "Fair Skinned", "Milky", "Mocha", "Olive", "Tan", "Pale Pink",
                  "Light Gray", "Light Green", "Light Red", "Dark Blue", "Lavender", "Pale Orange",
                  "Dark Blue", "Galaxy", "Rainbow", "Pale Blue Fading To Black At The Tips",
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
        shape = ["Diamond", "Heart-Shaped", "Square", "Round", "Oval", "Triangular", "Oblong", "Narrow"]
        return random.choice(shape)
        
    def character_ears(self):
        size = ["Small", "Medium", "Large"]
        shape = ["Square", "Pointed", "Narrow", "Free-Lobe", "Attached-Lobe", "Elven", "Dwarf", "Gnome",
                 "Kender", "Half-Elf", "Orc", "Half-Orc", "Draconic", "Twilight-Elf", "Aquatic"]
        return f"{random.choice(size)}, {random.choice(shape)}"
    
    def character_horns(self):
        if random.random() < 0.25:
            size = ["Small", "Medium", "Large"]
            type = ["Draconic", "Antler", "Goat", "Markhor", "Pronghorn", "Orix", "Jacob-Sheep", "Chousingha",
                    "Bharal", "Hartebeest", "Spike", "Muskox", "Gnu", "Tur", "Gazelle", "Ibex", "Moose",
                    "Mule-Deer", "Bull", "Long", "Fallow-Deer", "Unicorn", "Sheep", "Mouflon", "Water-Buffalo"
                    "2 Sets Of", "3 Sets Of"]
            return f"{random.choice(size)}, {random.choice(type)} Horns"
        return "None"
    
    def character_wings(self):
        if random.random() < .25: #25% chance for wings :D
            size = ["Small", "Medium", "Large", "Massive"]
            type = ["Crystal", "Withered", "Dragon", "Bat", "Butterfly", "Moth", "Dragonfly", "Angel", "Bird",
                    "Insect", "Leathery", "Furry", "Flower", "Plant", "Rock", "Water", "Cloud", "Galaxy", 
                    "Star", "Flame", "Beetle", "Futuristic", "Translucent", "Metal", "3 Pairs Of Angel Wings", 
                    "2 Pairs Of Angel Wings" ]
            return f"{random.choice(size)} Wings ({random.choice(type)})"
        return "None"
    
    def character_skin_texture(self):
        texture = ["Clear", "Acne", "Scars", "Freckles", "Birthmarks", "Fur", "Scales", "Tattoos", "Moles", 
                   "Vitiligo"]
        return random.choice(texture)
    
    def character_hands(self):
        fingers = ["4 Fingers", "5 Fingers", "6 Fingers"]
        type = ["Thick", "Short", "Long", "Slender", "Calloused", "Elegant", "Clawed", "Stubby"]
        return f"{random.choice(fingers)}, {random.choice(type)}"
    
    def character_tail(self):
        if random.random() < .25:
            size = ["Small", "Medium", "Large"]
            type = ["Feathered", "Scaled", "Shark", "Layered", "Deer", "Goldfish", "Cat", "Dog", "Lion", 
                    "Scorpion", "Morning-Star", "Club", "Dagger", "Horse", "Snake", "Split", "Axolotl", "Gator"]
            return f"{random.choice(size)}, {random.choice(type)} Tail"
        return "None"
    
    def character_magic_class(self):
        return random.choice(list(TypeClass)).value
    
    def character_job(self):
        return random.choice(list(Jobs)).value
    
    def character_personality(self):
        return random.choice(list(PersonalityTraits)).value
    
    def character_gender(self):
        return random.choice(["Male", "Female", "Nonbinary"])
    
    def character_age(self):
        return random.randint(18, 100)
    
    def character_height(self):
        feet = random.randint(3, 6)
        inches = random.randint(3, 5) if feet < 6 else random.randint(4, 9)
        return f"{feet}'{inches}\""
    
    def character_quirk(self):
        return random.choice(self.quirks)
    
    def generate_trait(self, trait_name):
        character_map = {"Gender": self.character_gender,"Age": self.character_age, 
                         "Height": self.character_height, "Skin Color": self.character_skin_tone, 
                         "Hair": self.character_hair, "Has Eyes": self.character_has_eyes, 
                         "Eyebrows": self.character_eyebrows, 
                         "Nose": self.character_nose, "Lips": self.character_lips, 
                         "Jawline": self.character_jawline, "Ears": self.character_ears,
                         "Horns": self.character_horns, "Skin Texture": self.character_skin_texture,
                         "Hands": self.character_hands, "Wings": self.character_wings, 
                         "Tail": self.character_tail, "Magic Class": self.character_magic_class, 
                         "Job": self.character_job, "Personality": self.character_personality,
                         "Quirk": self.character_quirk}
        return character_map[trait_name]()
    
    def next_trait(self):
        if not self.traits:
            self.display_character()
            return
        
        self.current_trait = self.traits.pop(0)

        #skip hair color if character bald D:
        if self.current_trait == "Hair" and "Bald" in self.character.get("Hair", ""):
            self.next_trait()
            return 
        
        #skips eye color if character has no eyes D:
        if self.current_trait == "Eye Color" and self.character.get("Has Eyes", "Yes") == "No":
            self.next_trait()
            return
        
        self.trait_name_label.config(text= self.current_trait)
        self.trait_value = self.generate_trait(self.current_trait)
        self.trait_value_label.config(text= self.trait_value)

        completed = len(self.character)
        total_traits = completed + len(self.traits)
        self.progress_label.config(text= f"Progress: {completed}/{total_traits} Traits Completed")

    def reroll_trait(self):
        self.trait_value = self.generate_trait(self.current_trait)
        self.trait_value_label.config(text= self.trait_value)

    def accept_trait(self):
        self.character[self.current_trait] = self.trait_value
        self.next_trait()

    def character_stats(self):
        return {stat: random.randint(1,20) for stat in self.stats}

    def display_character(self):
        #hides traits selected 
        self.trait_frame.pack_forget()
        self.button_frame.pack_forget()
        self.progress_label.pack_forget()

        #generates character stats
        self.character_numbers = self.character_stats()

        #character display
        self.character_frame.pack(fill= tk.BOTH, expand= True, pady= 5)
        self.stats_frame.pack(fill= tk.BOTH, expand= True, pady= 5)
        self.quirk_frame.pack(fill= tk.BOTH, expand= True, pady= 5)
        
        #clears everything to display stats for character  
        for widget in self.character_frame.winfo_children():
            widget.destroy()

        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        for widget in self.quirk_frame.winfo_children():
            widget.destroy() 

        #add character traits and skips hair color if character is bald
        
        for trait, value in self.character.items():
            if trait == "Hair":
                if "Bald" in value:
                    ttk.Label(self.character_frame, text= "Hair: Bald", 
                          font= ("Arial", 11)).pack(anchor= tk.W, padx= 20, pady= 2)
           
                else:
                    ttk.Label(self.character_frame, text= f"Hair: {value}", 
                              font= ("Arial", 11)).pack(anchor= tk.W, padx= 20, pady= 2)
            elif trait == "Eye Color":
                if self.character.get("Has Eyes") == "No":
                    continue 
            elif trait != "Quirk":
                ttk.Label(self.stats_frame, text= f"{trait}: {value}", 
                          font= ("Arial", 11)).pack(anchor= tk.W, padx= 20, pady= 2)

         #adds in the stats for character ex.) Chrisma 20
     
        for stat, value in self.character_numbers.items():
            ttk.Label(self.stats_frame, text= f"{stat}: {value}", 
                      font= ("Arial", 11)).pack(anchor= tk.W, padx= 20, pady= 2)
            
            #adds character quriks in diff formatting to make it different 
            
            quirk = self.character.get("Quirk", "No Notable Quirks")
            ttk.Label(self.quirk_frame, text= f"Quirk: {quirk}", font= ("Arial", 11, "italic"),
                      foreground= "blue").pack(anchor= tk.W, padx= 20, pady= 2)
           
            #start over button for artist
            self.start_over_button.pack(pady= 20)

            messagebox.showinfo(
                "Character Complete! :D", 
                "Your Character Has Been Created!\n\nClick 'Create Another Character' To Restart!")
            
    def restart_character(self):
        #complete reset of traits
        self.character_frame.pack_forget()
        self.stats_frame.pack_forget()
        self.quirk_frame.pack_forget()
        self.start_over_button.pack_forget()

        self.character = {}
        self.traits = ["Gender", "Age", "Height", "Skin Color", "Hair", "Has Eyes", "Eye Color", "Eyebrows",
                       "Nose", "Lips", "Jawline", "Ears", "Horns", "Skin Texture", "Hands", "Wings", "Tail",
                       "Magic Class", "Job", "Personality", "Quirk"]
       
        #shows trait selection for viewer
        self.trait_frame.pack(fill= tk.X, pady= 10)
        self.button_frame.pack(pady= 20)
        self.progress_label.pack(pady= 10)

        self.next_trait()

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterCreator(root)
    root.mainloop()