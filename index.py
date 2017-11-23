class Test:
    staticVariable = 10

    def __init__(self):
        self.__var1 = 'private'
        self.var2 = 'public'

    def getVar(self):
        return self.__var1

    def __gopon(self):
        print('gopon called')

    def open(self):
        self.__gopon()

    def staticMethod():
        print('static call')


tst = Test()
print(tst.var2)
tst.open()
print(Test.staticMethod())
print(Test.staticVariable)
tst._Test__gopon()
# print(tst.var1) #error
# x = tst.__dict__
print(tst._Test__var1)  # alternative way of accessing private variable
