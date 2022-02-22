class Result:

    num1,num2,res = 0,0,0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def printNums(self):
        print(f'First number is {self.num1}')
        print(f'Second number is {self.num2}')
        print(f'Their sum is {self.calculate()}')

    def calculate(self):
        self.res = self.num1 + self.num2
        return self.res

obj = Result(5,5)
obj.printNums()

'''
O/P:
First number is 5
Second number is 5
Their sum is 10
'''

