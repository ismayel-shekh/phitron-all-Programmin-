# object/hashtable/Overlap with set
#{key: value, key:val,key:value}
person ={'name': 'kala pakhi','address' : 'kaliaput','age':23,'job':'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada paki'
del person['age']
# del person
for item in person.items():
    print(item)
# print(person)
for key,value in person.items():
    print(key,value)