# %%
# Define a class for a well
class Well:
    def __init__(self, name, type, latitude, longitude, extraction_rate, case_radius):
        self.name = name
        self.type = type
        self.latitude = latitude #degrees
        self.longitude = longitude #degrees
        self.extraction_rate = extraction_rate #m/s
        self.case_radius = case_radius #m
    
    def __str__(self):
        return f"Name: {self.name}, type: {self.type},, location: {self.latitude}, {self.longitude}, extraction rate: {self.extraction_rate} m/s, case radius: {self.case_radius} m"

well_1 = Well("well_1", "well", -34.92866, 138.59863, 1, 0.1)
well_2 = Well("well_2", "well", -34.92866, 138.59863, 1, 0.1)
well_3 = Well("well_3", "well", -34.92866, 138.59863, 1, 0.1)
well_4 = Well("well_4", "well", -34.92866, 138.59863, 1, 0.1)


class Well_field:
    def __init__(self):
        self._well_field = []
    
    def add_wells(self, well):
        if type == "well":
            self._wells.append(well)

    def list_wells(self):
        print("well")
        for well in self._wells:
            print('\t', well)



welldata = Well_field()
welldata.add_wells(well_1)
welldata.add_wells(well_2)
welldata.add_wells(well_3)
welldata.add_wells(well_4)

welldata.list_wells()



# %%
# Define a class for a well
class Well:
    def __init__(self, name, type, latitude, longitude, extraction_rate, case_radius):
        self.name = name
        self.type = type
        self.latitude = latitude #degrees
        self.longitude = longitude #degrees
        self.extraction_rate = extraction_rate #m/s
        self.case_radius = case_radius #m
    
    def __str__(self):
        return f"Name: {self.name}, type: {self.type},, location: {self.latitude}, {self.longitude}, extraction rate: {self.extraction_rate} m/s, case radius: {self.case_radius} m"

well_1 = Well("well_1", "well", -34.92866, 138.59863, 1, 0.01)
well_2 = Well("well_2", "well", -34.92866, 138.59863, 1, 0.01)
well_3 = Well("well_3", "well", -34.92866, 138.59863, 1, 0.01)
well_4 = Well("well_4", "well", -34.92866, 138.59863, 1, 0.01)
spring = Well("spring", "spring", -34.92866, 138.59863, 1, 0.01)

class Well_field:
    def __init__(self):
        self._well_field = []
        self._spring = []
    
    def add_wells(self, well):
        if type == "well":
            self._wells.append(well)
        elif type == "spring":
            self._springs.append(well)

    def list_wells(self):
        print("Wells")
        for well in self._wells:
            print('\t', well)
        print("Springs")
        for well in self._springs:
            print('\t', well)


welldata = Well_field()
welldata.add_wells(well_1)
welldata.add_wells(well_2)
welldata.add_wells(well_3)
welldata.add_wells(well_4)

welldata.list_wells()


# %%
# Modify the code below
class Person:
    def __init__(self, name, age, nationality):
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

# Define additional persons`
vincent = Person("Vincent", 29, "Dutch")
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
# %%
