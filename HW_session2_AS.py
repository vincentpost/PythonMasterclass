class Well:
    def __init__(self, borefield, xcoord, ycoord, extr_rate, rad):
        self.bf = borefield
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.extr_rate = extr_rate
        self.rad = rad
    
    
    def __str__(self):
        return f"Borefield: {self.bf}, coordinates: {self.xcoord, self.ycoord}, extractrion rate: {self.extr_rate}, casing radius: {self.rad}"

#wellx = Well("Surat",145,-33,20,300)
print(Well("Surat",145,-33,20,300))


# class Wellfield:
#     def __init__(self):
#         self._wellfield = []
    
#     def add_well(self, well, borefield="Surat"):
#         if borefield == "Surat":
#             self._wellfield.append(well)
    
#     def list_wells(self):
#         print("Surat borefield")
#         for well in self._wellfield:
#             print('\t', well)
        
# w = Wellfield()
# # wellx = Well("Surat",145,-33,20,300)

# w.add_well(wellx)#I thought I had done this like the example, but apparently add_well is missing the positional argument "well". Where have I gone wrong?
# w.list_wells()