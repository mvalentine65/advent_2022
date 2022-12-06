class Elf:
    handle = None
    elves = []
    current = None

    @staticmethod
    def find_highest():
        Elf.elves.sort(key=lambda x: x.rations, reverse=True)
        return Elf.elves[0]

    @staticmethod
    def find_three_highest():
        Elf.elves.sort(key=lambda x: x.rations, reverse=True)
        return sum([elf.rations for elf in Elf.elves[0:3]])

    @staticmethod
    def reader():
        current = Elf()
        for line in Elf.handle:
            if line == "\n":
                current = Elf()
                Elf.elves.append(current)
            else:
                current.rations += int(line.strip())

    def __init__(self):
        self.rations = 0


if __name__ == "__main__":
    with open("input.txt") as f:
        Elf.handle = f
        Elf.reader()
        highest = Elf.find_highest()
        print(f"highest single elf: {highest.rations}")
        three_highest = Elf.find_three_highest()
        print(f"total of three highest: {three_highest}")
