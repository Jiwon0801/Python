class Calculator:

    PI = 3.14159 # static field

    @staticmethod
    def plus(a,b):
        return a+b
    @staticmethod
    def minus(a,b):
        return a-b

    @staticmethod
    def multiply(a,b):
        return a*b

    @staticmethod
    def divide(a,b):
        return a/b

    @classmethod
    def area(cls, r):
        return r*r*cls.PI


        



"""
    이 모듈은 테스트입니다.
    모듈을 배우고 있습니다.
        :
        :
"""

if __name__ == '__main__':
    print("{0} + {1} = {2}".format(7,4, Calculator.plus(7,4)))
    print("{0} - {1} = {2}".format(7,4, Calculator.minus(7,4)))
    print("{0} * {1} = {2}".format(7,4, Calculator.multiply(7,4)))
    print("{0}".format(Calculator.PI))
    print("{0}".format(Calculator.area(5)))

    print('자체 실행')
else:
    print('모듈 실행')


