class Car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car starting.........")


Ferrari = Car()
Ferrari.start()
