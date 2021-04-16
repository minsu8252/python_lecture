class Calculator:
    def __init__(self , num = 0):  #초기화 하는 과정
        self.result = num

    def add(self, num):
        self.result += num
        return self.result