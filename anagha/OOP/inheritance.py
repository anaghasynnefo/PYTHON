"""single inheritence"""

class vehicle:
    def engine(self):
        print("all vehicles have engine")
class car(vehicle):
    def fourwheel(self):
        print("car have 4 wheel")
c=car()
c.fourwheel()
c.engine()

"""multiple inheritance"""

class father:
    def drver(self):
       print("driver")

class mother:
    def cook(self):
        print("cook")

class girl(father,mother):
    def engineer(self):
        print("engineer")

g=girl()
g.engineer()
g.cook()
g.drver()

"""multi level inheritance"""

class grandpa:
      print("kashandi family")
def farmer(self):
    print("farmer")

class father:
    def driver(self):
        print("driver")
    def reader(self):
        print("reader")

class me:
    def swimming(self):
        print("swimming")
    def engineer(self):
        print("engineer")

class mechild:
    def gamer(self):
        print("gamer")

# ob=me
# ob.swimming

# ob=mechild
# ob.gamer

ob=father
ob.driver








































































































































































































































































































































































































































































































































































































































































































































