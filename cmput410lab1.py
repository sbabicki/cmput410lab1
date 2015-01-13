class Student:
    
    courseMarks = {}
    name = ""
    family = ""
    
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        
    def average(self):
        return round(sum(self.courseMarks.values())/len(self.courseMarks), 2)
    
# initialize student
c = Student("John", "Smith")

# add courses
c.addCourseMark("CMPUT 100", 3.7)
c.addCourseMark("CMPUT 101", 2.3)
c.addCourseMark("CMPUT 102", 3.3)

print "\nStudent's Name: " + c.name + " " + c.family
print "\nStudent's Average: %d \n" %(c.average())
print "Student's Mark Summary: "
print c.courseMarks