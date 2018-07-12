class MathDojo:
    def __init__(self):
        # self.value = value
        self.sum=0
    def add(self, *values):
        # sum=0
        for i in values:
            self.sum = self.sum + i 
        # print(self.sum)
        # self.value = self.value + sum
        # # print(self.value)
        # return self.value
        return self
    def subtract(self, *values):
        for i in values:
            self.sum = self.sum - i
        return self
    def result(self):
        print(self.sum)
        return self
# test=MathDojo()
# test.add(20,2,1)
# print(cheese)
x=MathDojo()
x.add(2).add(2,5,1).subtract(3,2).result()
# print(x) # should print 5