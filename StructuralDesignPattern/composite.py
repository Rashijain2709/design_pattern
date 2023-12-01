class Equipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class Composite:
    def __init__(self, name: str):
        self.name = name
        self.iteams = []

    def add(self, equipment: Equipment):
        self.iteams.append(equipment)
        return self

    @property
    def price(self):
        return sum(w.price for w in self.iteams)

    @price.setter
    def price(self, value):
        self.price = value

if __name__ == '__main__':
    computer = Composite("PC")
    memory = Composite("Memory")
    processor = Equipment("Processor", 1000)
    hard_drive = Equipment("Hard Drive", 250)
    rom = Equipment("Read only memory", 100)
    ram = Equipment("Random access memory", 75)

    mem = memory.add(rom).add(ram)
    pc = computer.add(processor).add(hard_drive).add(memory)

    print(pc.price)
    print(mem.price)






