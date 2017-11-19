# def tester(name, age):
#     print(name, age)

# tester('guoguo', 18)

# tester(age=18, name='guo')

def tester(name, *t, age=19, **kw):
    print(name, t, age, kw)

# tester('guo', age=17, uid=1,title='tt')

def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1)