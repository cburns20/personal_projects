class chili:

    def __init__(self, name, look, taste, flavor, aroma, heat):
        self.name = name
        self.look = look
        self.taste = taste
        self.flavor = flavor
        self.aroma = aroma
        self.heat = heat
    
    def __str__(self): 
        return (f"Chili {self.name} Score:\n Look:{self.look}\n Taste:{self.taste}\n Flavor:{self.flavor}\n Aroma:{self.aroma}\n Heat:{self.heat}\n")
    
    def total(self):
        return(self.look + self.taste + self.flavor + self.aroma + self.heat)
    