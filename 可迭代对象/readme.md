# 实现可迭代对象

在Python中，序列类型的数据可以使用for...in遍历，以及其他Iterable对象和Iterator。

当然，我们自己也可以实现可迭代的对象。通常有两种方式

## 第1种 实现getitem方法

```py
def __getitem__(self, i):
    if i < len(self.source):
        return self.source[i]
    else:
        raise StopIteration()
```

getitem方法实现根据索引获取序列的值，直到抛出“StopIteration()”错误。

## 第2种 实现iter和next方法

iter方法返回一个迭代对象，一般为对象本身；next方法不断的返回一个新值，直到抛出“StopIteration()”错误。

```py
def __iter__(self):
    self.i = -1 # 每一次迭代 将标量复位
    return self

def __next__(self):
    self.i += 1
    if self.i >= len(self.source):
        self.i = -1 # 迭代完成后 将标量复位
        raise StopIteration()

    return self.source[self.i]
```