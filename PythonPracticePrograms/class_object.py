class Animal:
    
    def eat(self):
        print("I can eat")

class Dog():
    
        def eat(self):
            print("I can eat Bones")

class Puppy(Dog, Animal): # As per MRO - Method resolution order left most class is called 
    pass

abc = Puppy()
abc.eat()