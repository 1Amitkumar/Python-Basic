class MyClass1():

    def method1(self):
        print("method1 method called")


class MyClass2():

    def method2(self):
        print("method2 method called")


class ChildClass(MyClass1, MyClass2):

    def child_method(self):
        print("child method")


c = ChildClass()
c.method1()
c.method2()
