# %% [markdown]
# # Object-oriented programming
# 
# One of the main strenghts of Python is that it supports object-oriented programming (OOP), although it is not unique in that sense: most codes are built around that concept these days. When writing complex programs, or when developing Python packages or libraries, an object-oriented approach is the way to go. An object has unique properties and behaviour. Its properties are defined through *attributes* and the *methods* of an object determine its behaviour. Once an object is defined, you can use it mulitple times in your program, which has the obvious advantage that you don't have to repeat the same code over and over again. By letting objects interact with each other, you define how your program works.
# 
# When you are not used to this type of programming, OOP may seem like an abstract concept, and it is best explained by showing examples. But before we can do that, we have to talk about functions first.

# %% [markdown]
# ## Classes
# 
# In Python classes form the blueprint for the structure and behaviour of objects. A class has properties (also called attributes) and methods, as shown in the code cell below. The definition of a class starts (not surprisingly) with the word `class`, which is followed by its name (and a colon to end the code line). 
# 
# All code that defines the class is indented. In the example below, two functions are defined as part of the class (and therefore they should rather be called methods). The first one is `__init__`, which is the method that gets executed when an object gets initialized (more on that later). It can be seen that there are four arguments: `self`, `name`, `age` and `nationality`. The argument `self` is a bit of a special one. It occurs because the object needs to know about its own existence in the computer memory. A user doesn't have to worry about `self`, the argument gets passed to the function invisibly by Python, so as far as the user is concerned, there are really only three arguments for the function (`name`, `age` and `nationality`).
# 
# Within the `__init__` method, the arguments are used to set the properties of the class. These are `_name`, `_age` and `_nationality`. Because the are preceded by `self`, we know that they are properties of the class.
# 
# The second method is a simple function that prints a message to the screen depending on the state (i.e. the values of the properties) of the object. Notice that the word `self` appears once more as an argument, simply because Python requires it because we are defining a class. In practice, the function gets called without any arguments, as will be demonstrated in the next code cell.
# %%

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

#%%
# Define the well class
class Well:
    def __init__(self, x0, y0, Q, rw):
        self._x0 = float(x0); 
        self._y0 = float(y0)
        self._casrad = rw; 
        self._rwsq = rw ** 2
        self._Q = Q
    def __str__(self):
        return " [x_coord, y_coord, extraction rate(Q), casing radius (rw)] >> " + str((self._x0, self._y0, self._Q, self._casrad))
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
print(r'well 1 : ' + str(w1))
print(r'well 2 : ' + str(w2))
print(r'well 3 : ' + str(w3))
print(r'well 4 : ' + str(w4))

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
