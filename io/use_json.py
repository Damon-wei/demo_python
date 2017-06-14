import json

d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
print('json:',json_str)
f = open('json_str.txt','w')
json.dump(d,f)
f.close()

ff = open('json_str.txt','r')
dd = json.load(ff)
ff.close()
print('dict:',dd)

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return{
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob',20,88)
print(s)
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象
#print(json.dumps(s,default=student2dict))
json_str = json.dumps(s,default=lambda obj: obj.__dict__)
print(json_str)

# JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
stu = json.loads(json_str,object_hook=dict2student)
print(stu)