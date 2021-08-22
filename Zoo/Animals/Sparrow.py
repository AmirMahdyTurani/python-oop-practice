from Zoo.abcClass.Bird import Bird  # import Bird


class Sparrow(Bird):  # create Sparrow Class
    def fly(self, height):  # implement fly method
        return f"The {self._name} flies at a height of {height} cm..."

    def __init__(self, name):  # implement constructor
        super().__init__(name)  # implement Bird's Constructor

    def playSound(self):  # implement playSound method
        return "Jick Jick Jick..."
