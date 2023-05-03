# Turn the script from session 1 into a function

def describe_person(name):
    if name == "Vincent":
        print("Vincent is one of the instructors of the Python Masterclass")
    elif name == "Anushree":
        print("Anushree is the AWS support person during the Python Masterclass")
    else:
        print("Name is unknown, not sure what message to print for this person.")

# Call the function
describe_person("Vincent")

# To add: function with keyword argument
# To add: function with docstring

# Define a class for a single person

class Person:
    def __init__(self, name, age, nationality) -> None:
        self._name = name
        self._age = age
        self._nationality = nationality
    
    def introduce_yourself(self):
        print(f"Hello, my name is {self._name} and I am {self._age} years old.")
    
    def __str__(self):
        return f"Name: {self._name}, age: {self._age}, nationality: {self._nationality}"

# Define a person and let them introduce themself
vincent = Person("Vincent", 23, "Dutch")
vincent.introduce_yourself()

# Define a course with multiple persons
class Course:
    def __init__(self) -> None:
        self._attendees = []
        self._instructors = []
    
    def add_person(self, person, role="attendee"):
        if not isinstance(person, Person):
            raise TypeError("argument 'person' must be of type 'Person'")
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


# Define additional persons
onno = Person("Onno", 23, "Dutch")
michael = Person("Michael", 23, "Australian")
stacey = Person("Stacey", 23, "Australian")

# Add them to the course
PythonMasterclass = Course()
PythonMasterclass.add_person(michael)
PythonMasterclass.add_person(stacey)
PythonMasterclass.add_person(vincent, role="instructor")
PythonMasterclass.add_person(onno, role="instructor")

PythonMasterclass.list_persons()

# Enforce a TypeError
PythonMasterclass.add_person(1)

