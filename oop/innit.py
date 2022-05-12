class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def config(self):
        print(self.cpu, self.ram, self.storage)


com1 = Computer("i7", "12gb", "256gb")

com1.config()



