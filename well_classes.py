# libraries
import numpy as np
import pandas as pd

# Classes

class well:
    def __init__(self, x, y, exrate, cas_rad):
        self.coords = (x,y)
        self.exrate = exrate
        self.cas_rad = cas_rad

    def __str__(self):
        return f"Well properties\n (x, y):{self.coords[0],self.coords[1]}\n Ex-rate:{self.exrate}\n Casing radius:{self.cas_rad}"


class wellField:
    def __init__(self, name):
        self.field = []
        self.well_cnt = 0
        self.name = name

    def addWell(self, well):
        self.field.append(well)
        self.well_cnt = self.well_cnt + 1

    def listWells(self):
        l = [n.__str__() for n in self.field]
        return "\n\n".join(l)

    def __str__(self):
        return f"Well field contains {self.well_cnt} wells."
