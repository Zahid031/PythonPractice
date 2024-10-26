class myBird():
    def __init__(self):
        print("Bird constructor is executing")

    def whatType(self):
        print("I am a bird")
    def canFly(self):
        print("I can fly")

class Penguin(myBird):
    def __init__(self):
        super().__init__()
        print("Penguin constructor is executing")

    def whoIs(self):
        print("I am a penguin")

    def canSwim(self):
        print("Yes I can swim")

obj1=Penguin()
obj1.whatType()
obj1.canSwim()
obj1.canFly()


#polymorphism
class Animal():
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Barks")

class Cat(Animal):
    def speak(self):
        print("Mew Mew")

Animal().speak()