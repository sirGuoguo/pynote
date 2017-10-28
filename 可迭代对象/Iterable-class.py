class A():
    # constructor
    def __init__(self):
        self.source = [1, 2, 3, 4, 5]
        self.i = -1

    # 1 getitem实现可迭代对象
    # def __getitem__(self, i):
    #     if i < len(self.source):
    #         return self.source[i]
    #     else:
    #         raise StopIteration()
    # 2 iter next实现
    def __iter__(self):
        self.i = -1 # 每一次迭代 将标量复位
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.source):
            self.i = -1 # 迭代完成后 将标量复位
            raise StopIteration()

        return self.source[self.i]

# test
from collections import Iterable, Iterator

a = A()

print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

for n in a:
    if n == 2:
        break
    print(n)

print('='*10)

for n in a:
    print(n)
