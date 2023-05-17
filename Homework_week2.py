#%% Define a well

class Well:
    def __init__(self, id, x, y, pumping_rate, casing_radius=0.1):
        self.id = id
        self.x = x
        self.y = y
        self.pumping_rate = pumping_rate 
        self.casing_radius = casing_radius
    def __str__(self):
        return f'ID: {self.id}, x coord: {self.x}, y coord: {self.y}, pumping rate: {self.pumping_rate}, casing radius:{self.casing_radius}'

#%% Add wells
vig_8 = Well(id = '01', x = 57, y = 13, pumping_rate = 39, casing_radius=0.15)
vig_12 = Well(id = '21', x = 43.4, y = 12.6, pumping_rate = 13.7, casing_radius=0.08)
vig_32 = Well(id = '02', x = 143.4, y = 212.6, pumping_rate = 33.7, casing_radius=0.12)
tes_42 = Well(id = '25', x = 243.1, y = 12.6, pumping_rate = 14.3, casing_radius=0.12)
mis_1 = Well(id = '56', x = 5143.2, y = 1122.6, pumping_rate = 24.5)
mis_2 = Well(id = '57', x = 5144.4, y = 1137.6, pumping_rate = 12.3)
piu_1 = Well(id = '81', x = 445.7, y = 212.6, pumping_rate = 6.7, casing_radius=0.08)
piu_2 = Well(id = '85', x = 424.1, y = 214.2, pumping_rate = 12.0, casing_radius=0.08)


#%%
print(vig_8)

#%% #define a wellfield

class Wellfield:
    def __init__(self):
        self._plain = []
        self._hill = []
        self._coast = []
        self._other = []
    
    def add_well(self, well, site="Other"):
        if site == "Plain":
            self._plain.append(well)
        elif site == "Hill":
            self._hill.append(well)
        elif site == "Coast":
            self._coast.append(well)
        else:
            self._other.append(well)

    def list_wells(self):
        print("'Plain' wellfield")
        for well in self._plain:
            print('\t', well)
        print("'Hill' wellfield")
        for well in self._hill:
            print('\t', well)
        print("'Coast' wellfield")
        for well in self._coast:
            print('\t', well)
        print("Remaining wells")
        for well in self._other:
            print('\t', well)



# %%
Hydrobase = Wellfield()
Hydrobase.add_well(vig_8, site = 'Plain')
Hydrobase.add_well(vig_12, site = 'Plain')
Hydrobase.add_well(vig_32, site = 'Plain')
Hydrobase.add_well(tes_42, site = 'Coast')
Hydrobase.add_well(mis_1)
Hydrobase.add_well(mis_1)
Hydrobase.add_well(piu_1, site = 'Hill')
Hydrobase.add_well(piu_2, site = 'Hill')
# %%
Hydrobase.list_wells()
# %%
