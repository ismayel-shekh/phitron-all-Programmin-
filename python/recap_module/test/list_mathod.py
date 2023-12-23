number = [1, 5, 9, 5, 6, 7]
number.append(100)
print(number)
number.insert(2,50)
print(number)
number.remove(100)
print(number)
if 10 in number:
    number.remove(10)
print(number)
last = number.pop()
print(last,number)
if 10 in number:
    index = number.index(10)
    print(index)
sorted = number.sort()
print(number)
number.reverse()
print(number)