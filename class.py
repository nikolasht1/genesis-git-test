class Bird:
    #This is constructor
    def __init__(self, name):
        #dynamic attributes
        self.message = "I'm object of Bird class"
        self.name = name

     #Static attributes
     name = "Bird"

# Objects of our class initialisation
bird1 = Bird("Sparrow")
bird2 = Bird("Penguin")


# 1st obj
print("I am", bird1.name)
print(bird1.message)
# 2nd obj
print("I am", bird2.name)
print(bird2.message)

print("Here is our static attribute:", Bird.name)

