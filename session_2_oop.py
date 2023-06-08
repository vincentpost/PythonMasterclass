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
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    
    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# %% [markdown]
# With the class `Person` now defined, we can create an instance of it. That means that we will initialize it as an object that has actual data. The resulting class instance is called `vincent` and the code looks like we're calling a function. In fact, we are because Python understands that it needs to call the `__init__` functions with the arguments that we pass in the parentheses behind `Person`. Once the class instance exists, its methods can be called, in this case we ask Vincent to introduce himself. Note that, as mentioned previously, there is no need to worry about that `self` argument, neither when initializing `Person`, nor when calling `introduce_yourself`.

# %%
vincent = Person("Vincent", 29, "Dutch")
vincent.introduce_yourself()

# %% [markdown]
# Besides `__init__` there are a few other special class methods, for example `__str__`. This method can be defined to provide an elegant string representation of the class. The code cell below copies the class definition from before, but adds the `__str__` method. As can be seen, it returns a string with information about the class property values.

# %%
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    
    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, nationality: {self.nationality}"

# %% [markdown]
# Let's see what happens when we initialize `vincent` based on the new class definition and then combine it with a `print` statement

# %%
vincent = Person("Vincent", 29, "Dutch")
print(vincent)

# %% [markdown]
# ***Exercise 1***: In the code cell below, add a property to the class that keeps track if a person already introduced themself. *Hint*: add the variable to the `__init__` method and modify the value in the `__introduce_yourself` method.

# %%
# Modify the code below
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    
    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, nationality: {self.nationality}"

# %% [markdown]
# There can be as many instances of the class as we want, so we can define multiple instances, which all follow the blueprint of `Person`, but each have different properties.

# %%
# Define additional persons`
onno = Person("Onno", 23, "Dutch")
michael = Person("Michael", 23, "Australian")
stacey = Person("Stacey", 23, "Australian")

# %% [markdown]
# This is useful when we also have a class that defines a course, which is defined in the code cell below. The `__init__` method for this class works a little different than before. No arguments are provided when `Course` is initialized. All the `__init__` method does is create two properties (`_attendees` and `_instructors`) which are empty lists. So directly after initialization, these lists are still empty, and they will only be populated when the class method `add_person` gets called. The leading underscore is there because there is a convention in Python that if a variable is not supposed to be used outside the class, its name receives a leading underscore. That is not to say that a user can't see or change it (there is nothing that prevents them from doing this) but at least they've been warned not to touch it, as otherwise unexpected behaviour might occur.
# 
# The `add_person` method expects an instance of the `Person` class and takes a keyword argument `role`, which the user can provide to indicate if a person is an attendee or an instructor. Depending on the value of `role`, the `Person` instance will get added to either the list `_attendees` or `_instructors`.
# 
# The method `list_persons` prints the attendees and the instructors to the screen, thereby making use of the fact that we added a `__str__` method to the `Person` class.

# %%
class Course:
    def __init__(self):
        self._attendees = []
        self._instructors = []
    
    def add_person(self, person, role="attendee"):
        if role == "attendee":
            self._attendees.append(person)
        elif role == "instructor":
            self._instructors.append(person)

    def list_persons(self):
        print("Attendees")
        for person in self._attendees:
            print('\t', person)
        print("Instructors")
        for person in self._instructors:
            print('\t', person)

# %% [markdown]
# We can now initialize `Course` and call the resulting object `PythonMasterclass`. Since we already defined multiple persons earlier, we can add them to the course and indicate their roles.

# %%
PythonMasterclass = Course()
PythonMasterclass.add_person(michael)
PythonMasterclass.add_person(stacey)
PythonMasterclass.add_person(vincent, role="instructor")
PythonMasterclass.add_person(onno, role="instructor")

# %% [markdown]
# Now let's see who are in this course

# %%
PythonMasterclass.list_persons()

# %% [markdown]
# ### Inheritance (*bonus material*)
# 
# One of the strengths of object-oriented programming is that you can mould classes after other classes. This means that you can create a class with generic attributes and methods, and derive classes that inherit these but add specific properties and behaviour. Continuing with the course example above, we could have used the `Person` class to derive separate classes for attendees and instructors. They'd all be persons, but an attendee requires different attributes (for example, a record of their homework completions) than an instructor.
# 
# A class that derives from another class is called a child class, and the original class is the parent. Let's define two new classes `Attendee` and `Instructor`, which derives from `Person`. For `Attendee` we add a new property which is a list that contains the session numbers for which the homework assignments were submitted. For `Instructor` we add a property that describes their expertise. 
# 
# Note that for `Attendee` the definition of the `__init__` method is identical to the `Person` class. Because the `Person` class used the function arguments to assign values to the class properties we must call that same method to make sure that this gets done. This is why the first line of code in the `__init__` method for `Attendee` uses the function `super()` to call the parent class' `__init__` method. The second line defines a new property `_homework_completed` for the `Attendee` class.
# 
# For `Instructor` the `__init__` method accepts one additional argument `expertise`. The properties that are also in `Person` are set by calling `super().__init__`, the new `_expertise` property is set using the value of the `expertise` argument.

# %%
class Attendee(Person):
    def __init__(self, name, age, nationality):
        super().__init__(name, age, nationality)
        self._homework_completed = []

class Instructor(Person):
    def __init__(self, name, age, nationality, expertise):
        super().__init__(name, age, nationality)
        self._expertise = expertise

# %% [markdown]
# With these classes defined, we can also change the way the `Course` class works. Rather than having to pass `role` as a keyword argument, we can let the method decide to which of the two lists, `_attendees` or `_instructors`, the person needs to be assigned. For this purpose, Python has the function `isinstance`, which checks if a variable is an instance of a certain class.

# %%
class Course:
    def __init__(self):
        self._attendees = []
        self._instructors = []
    
    def add_person(self, person):
        if isinstance(person, Attendee):
            self._attendees.append(person)
        elif isinstance(person, Instructor):
            self._instructors.append(person)

    def list_persons(self):
        print("Attendees")
        for person in self._attendees:
            print('\t', person)
        print("Instructors")
        for person in self._instructors:
            print('\t', person)

# %% [markdown]
# The code cell below demonstrates how the new classes are used

# %%
# Define the instructors
vincent = Instructor("Vincent", 29, "Dutch", ["Python", "groundwater"])
onno = Instructor("Onno", 23, "Dutch", ["Python", "groundwater"])
# Define the attendees
michael = Attendee("Michael", 23, "Australian")
stacey = Attendee("Stacey", 23, "Australian")

# Initialize an instance of Course
PythonMasterclass = Course()

# Add the instructors and the attendees
PythonMasterclass.add_person(vincent)
PythonMasterclass.add_person(onno)
PythonMasterclass.add_person(michael)
PythonMasterclass.add_person(stacey)

# List everyone in the class
PythonMasterclass.list_persons()

# %% [markdown]
# ***Exercise 2***: Add a check to the `add_person` method that prevents instructors who don't have any Python expertise from being added to the course.
# 
# *Hint*: You can check if the word 'Python' occurs in the `_expertise` property (which is a list ) of the `Instructor` class instance with the following code: `'Python' in 'person._expertise'`

# %%
class Course:
    def __init__(self):
        self._attendees = []
        self._instructors = []
    
    def add_person(self, person):
        if isinstance(person, Attendee):
            self._attendees.append(person)
        elif isinstance(person, Instructor):
            self._instructors.append(person)

    # Note that the list_persons method was omitted for brevity

# %% [markdown]
# ***Exercise 3***: We can only add a single person each time, which gets a little annoying when there are many people in the course. Modify the definition of the `add_person` method in the code cell below to add multiple persons at the same time. 
# 
# *Hint*: You can pass a `list` as a function argument.

# %%
class Course:
    def __init__(self):
        self._attendees = []
        self._instructors = []
    
    def add_person(self, person):
        if isinstance(person, Attendee):
            self._attendees.append(person)
        elif isinstance(person, Instructor):
            self._instructors.append(person)

    def list_persons(self):
        print("Attendees")
        for person in self._attendees:
            print('\t', person)
        print("Instructors")
        for person in self._instructors:
            print('\t', person)


