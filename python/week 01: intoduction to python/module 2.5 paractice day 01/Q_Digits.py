l = input()
n = int(l)

while n > 0:
    n = n - 1
    x = input()
    s = x[::-1]
    string =""
    for char in s:
        string += char +" "
    print(string)



