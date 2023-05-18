

# Define a class for a well
class Well:
    def __init__(self, name, latitude, longitude, extraction_rate, case_radius):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.have_met = False
    
    def introduce_yourself(self):
        if self.have_met:
            print('I have already introduced myself') 
        else:    
            print("Hello, my name is {self.name} and I am {self.age} years old.")
            self.have_met = True
    
    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, nationality: {self.nationality}"
    
x and y coordinates, an extraction rate and a casing radius


vincent = Person("vincent", 29, "Dutch")
vincent.introduce_yourself()
vincent.introduce_yourself()
# Define additional persons`
onno = Person("Onno", 23, "Dutch")
michael = Person("Michael", 23, "Australian")
stacey = Person("Stacey", 23, "Australian")


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




PythonMasterclass = Course()
PythonMasterclass.add_person(michael)
PythonMasterclass.add_person(stacey)
PythonMasterclass.add_person(vincent, role="instructor")
PythonMasterclass.add_person(onno, role="instructor")

PythonMasterclass.list_persons()