class well:
    def __init__(self, borefield, xcoord, ycoord, extr_rate, rad):
        self.bf = borefield
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.extr_rate = extr_rate
        self.rad = rad
    
    
    def __str__(self):
        return f"Borefield: {self.bf}, coordinates: {self.xcoord, self.ycoord}, extractrion rate: {self.extr_rate}, casing radius: {self.rad}"

# wellx = well("Surat",145,-33,20,300)
# print(wellx)

class wellfield:
    def __init__(self):
        self._wellfield = []
    
    def add_well(self, well):
        if borefield == "Surat":
            self._wellfield.append(well)
    
    def list_wells(self):
        print("Surat borefield")
        for well in self._wellfield:
            print('\t', well)
        

wellx = well("Surat",145,-33,20,300)
wellfield.add_well(wellx)
wellfield.list_wells()