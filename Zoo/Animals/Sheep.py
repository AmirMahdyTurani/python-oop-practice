from Zoo.abcClass.Animal import Animal  # import Animal


class Sheep(Animal):  # create sheep class
    def playSound(self):  # implement play sound method
        return "Baaaaaah!!!..."

    def __init__(self, name):  # implement sheep constructor
        super().__init__(name)  # implement Animal Constructor
