class University:
    """A class representing a university.

    Attributes:
        university_name (str): A class variable shared by all instances, representing the university name.
        student_name (str): An instance variable representing the name of the student.
    """

    university_name = "VIT University"  # Class variable - shared by all objects

    def __init__(self, student_name):
        self.student_name = student_name  # Instance variable - specific for each instance


s1 = University("Mehul")
s2 = University("Gupta")

print(s1.university_name)
print(s2.university_name)

# Changing class variable affects all instances
University.university_name = "IIT Delhi"
print(s1.university_name)
print(s2.university_name)

# We can specify for each instance separately as well
s1.university_name = "IIT Bombay"
print(s1.university_name)
print(s2.university_name)
