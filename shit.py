class Student: 
    name = ""
    def setName(self, name):
        self.name = name
    def displayName(self):
        print(self.name)

dantwix = Student()
dantwix.setName("danya")
dantwix.displayName()