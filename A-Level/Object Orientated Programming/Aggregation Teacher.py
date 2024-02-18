class Department():

    def setDeptName(self, name):
        self.name = name

    def getDeptName(self):
        return self.name


class Teacher():

    def __init__(self, department):
        self.department = department

    def setTeacherName(self, name_teacher):
        self.name_teacher = name_teacher

    def getTeacherName(self):
        return self.name_teacher


english = Department()
english.setDeptName("English")
purple = Teacher(english)
purple.setTeacherName("Mr Purple")

print(purple.getTeacherName())
print(purple.department.getDeptName())