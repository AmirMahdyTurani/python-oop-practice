from Zoo.Animals.Sheep import Sheep  # import sheep class
from Zoo.Animals.Sparrow import Sparrow  # import Sparrow Class

print("In the name Of God")
'''
Created
by
Amirmahdy
Turani
'''

#################################################

mySheep = Sheep("bbii")  # create sheep object
print(mySheep.getName())  # get mySheep's name
print(mySheep.playSound())  # mySheep is playing sound
print(mySheep.eat("Grass"))  # mySheep is eating
print(mySheep)  # print mySheep Object

################################################
print("#########################################")
################################################

mySparrow = Sparrow("Jicko")  # create Sparrow object
print(mySparrow.getName())  # get mySparrow's name
print(mySparrow.playSound())  # mySparrow is playing sound
print(mySparrow.eat("Seed"))  # mySparrow is eating
print(mySparrow.fly(1000))  # mySparrow is flying
print(mySparrow)  # print mySparrow Object
