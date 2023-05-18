
# %%

# Import libraries

import matplotlib.pyplot as plt
import numpy as np

# Define the well class
class Well:
    def __init__(self, x0, y0, Q, rw):
        self._x0 = float(x0); 
        self._y0 = float(y0)
        self._rw = rw; 
        self._rwsq = rw ** 2
        self._Q = Q
    def print_well_info(self):
        return " (x_coord, y_coord, Q, rw) >> " + str((self._x0, self._y0, self._Q, self._rw))
    def head(self, x, y, T):
        rsq = (x - self._x0) ** 2 + (y - self._y0) ** 2
        rsq[rsq < self._rwsq] = self._rwsq
        return self._Q / (4 * np.pi * T) * np.log(rsq / self._rwsq)

print("Class: Well defined successfully !")    

# Define the WellField class
class WellField:
    """_summary_
    """    
    def __init__(self, wells, T):
        self._transmissivity = T
        self._wells = wells

    def plot(self, x, y):
        h = np.zeros_like(x)
        for w in self._wells: 
            h = h + w.head(x, y, self._transmissivity)

        fig, ax = plt.subplots()
        cf = ax.contourf(x, y, h)
        cs = ax.contour(x, y, h, 10, colors='w')
        ax.clabel(cs)
        ax.axis("scaled")
        plt.colorbar(cf)
        ax.set_title("Head")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")

print("Class: Well Field defined successfully !")    

# %%
#################################################################
#                                               Create an example
#################################################################
print("defining a new case....")
print("Please wait....")

# Create four instances of the class Well
w1 = Well(-105, -100, 100, .1)
w2 = Well( 110, -100, 100, .1)
w3 = Well( 117, 100, 100, .1)
w4 = Well(-92, 100, 100, .1)

# interrogate the wells:
print(r'well 1 : ' + str(w1.print_well_info()))
print(r'well 2 : ' + str(w2.print_well_info()))
print(r'well 3 : ' + str(w3.print_well_info()))
print(r'well 4 : ' + str(w4.print_well_info()))

# %%
print("Initializing WellField...")

# Define a set of grid points for which to calculate the heads of a WellField
x, y = np.meshgrid(np.linspace(-250, 250, 101), np.linspace(-250, 250, 101))

# Initialize the WellField object

print("Generating 2D plot with  WellField...")

wf = WellField(wells=[w1, w2, w3, w4], T=100)
wf.plot(x, y)

# Needed in VSC to show the figure
plt.show()
# %%
