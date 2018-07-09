class MathDojo:
    def __init__(self):
        self.sum = 0

    def add(self, *ints):
        for i in ints:
            self.sum = self.sum + i

        return self

    def subtract(self, *ints):
        for i in ints:
            self.sum = self.sum - i

        return self

    def displaySum(self):
        print("Total:", self.sum)
        return self

md = MathDojo()
md.add(2).add(2, 5, 1).subtract(3, 2).displaySum()
