class A(object):
    def __init__(self, name):
        self.name = name

class B(A):
    def __init__(self, age):
        self.age = age

class C(A):
    def __init__(self, addr):
        self.addr = addr

class D(B, C):
    def __init__(self, name, age, addr):
        super().__init__(age)

    def info(self):
        print(self.name, self.age, self.addr)
        
d = D('d', 17, '北京')
print(dir(d))