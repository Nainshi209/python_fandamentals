class Animal:
    def __init__(self,behavior,color,species):
        self.behavior =behavior
        self.color = color
        self.species =species
        self.new_behavior = "chill"


    def character(self):
        self.new_behavior = self.behavior
        print(f"the {self.color} {self.species} is now moving at {self.new_behavior}")

animal1 = Animal("faithful","black","dog")
animal2 = Animal("bold","orange","tiger")

animal1.character()
animal2.character()
