### How to make Dictionary ###

dic = {'name':'Hoon', 'phone':'01012345678', 'birth':'1018'}
a = {1:'hi'}
b = {'a': [1, 2, 3]}


### Add, Delete pair ###

a = {1:'a'}
# print(a) : {1: 'a'}

a[2] = 'b'
#print(a) : {1: 'a', 2: 'b'}

a['name'] = 'Hoon'
# print(a) : {1: 'a', 2: 'b', 'name': 'Hoon'}

a[3] = [1, 2, 3]
# print(a) : {1: 'a', 2: 'b', 3: [1, 2, 3], 'name': 'Hoon'}

a['a'] = [2, 2]
# print(a) : {'a': [2, 2], 1: 'a', 2: 'b', 3: [1, 2, 3], 'name': 'Hoon'}

del a['a']
# print(a) : {1: 'a', 2: 'b', 3: [1, 2, 3], 'name': 'Hoon'}


### Usage ###

grade = {'pey':10, 'julliet':99}
# print(grade['pey']) : 10
# print(grade['julliet']) : 99

# a = {[1,2] : 'hi'} : (error)


### Methods ###

dic = {'name':'Hoon', 'phone':'01012345678', 'birth':'1018'}

k = dic.keys() # return List // dict_keys object (python3)
# print(k) : ['phone', 'name', 'birth']
# print(k) with Python3 : dict_keys(['birth', 'name', 'phone'])

# list(dic.keys()) with Python3 : ['phone', 'name', 'birth']

for i in dic.keys():
	print(i)

# name
# birth
# phone

item = dic.items() # return List (Python2), dict_items object(Python3)
# print(item) : dict_items([('phone', '01012345678'), ('birth', '1018'), ('name', 'Hoon')])

n = dic.get('name')
# print(n) : 'Hoon'

f = dic.get('none')
# print(f) : None

m = dic.get('name', 'bar')
# print(m) : 'Hoon'

m = dic.get('none', 'bar')
# print(m) : 'bar'

TF = 'name' in dic
# print(TF) : True 

TF = 'email' in dic
# print(TF) : False

dic.clear()
# print(dic) : {}






