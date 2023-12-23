s = 'hello'
# s[0] = 'b'
for ch in s:
    print(ch,end=" ")
b ="python"
print("king",b.capitalize())
print(b.upper())
text ="hello, world"
src = "world"
index = text.find(src)
if index != -1:
    print(f"the result '{src}' was found at index '{index}'")
else:
    print("not found")
# print(index)
#count
text="piiithhhooon"
print(text.count('i'))
from collections import Counter
print(Counter(text))
from collections import Counter as ctr
print(ctr(text))
a = ['pitron']
print(a[0])
print(*a)
a =['a', 'b']
print(*a)
c =[['a','b'],['c']]
for prs in c:
    for val in prs:
        print(val)
    # print(*prs)
my_list =[1,2,3,4,5]
my_list.insert(1,10)
my_list.pop(1)
my_list.remove(1)
print(my_list)
my_list ={1:'pyhton',2:'hero'}
it = my_list.items();
for pr in it:
    for val in pr:
        print(val)
for key,val in it:
    print(key,val)                                                                                                                                                                                       