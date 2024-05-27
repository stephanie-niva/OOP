class Animal:
    def __init(self,name):
        def move(self):
            pass
        def make_noise(self):
            pass
        
class Cat(Animal):
    def move(self):
        print ("The cat is walking")

    def make_noise(self):
        print("meew")


class Bird(Animal):
    def move(self):
        print ("The bird is flying")

    def make_noise(self):
        print("chirp")

class Fish(Animal):
    def move(self):
        print("The fish is swimming")
    def make_noise(self):
        print("Boope")


cat =Cat("cat")
cat.make_noise