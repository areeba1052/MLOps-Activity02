class StudentsInMLOps:
    def __init__(self):
        self.total_students = 0
        self.class_name = "MLOps Essentials"

    def enrollStudents(self, count):
        self.total_students += count

    def dropStudents(self, count):
        self.total_students -= count
        if self.total_students < 0:
            self.total_students = 0

    def getTotalStrength(self):
        return self.total_students

    def getClassName(self):
        return self.class_name
