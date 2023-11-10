class Base:
    def method(self):
        print('base')

class A(Base):
    def method(self):
        print('A')
        super().method()

class B(Base):
    def method(self):
        print('B')
        super.method()

class C(A, B):
    def method(self):
        print('C')
        super().method()

print([class_.__name__ for class_ in C.__mro__])