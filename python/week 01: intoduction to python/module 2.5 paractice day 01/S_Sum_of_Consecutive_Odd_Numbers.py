n = int(input())
while n>0 :
    n=n-1
    sum = 0
    x = int(input())
    y = int(input())
    if y > x :
        i = x +1
        while i< y:
            if i%2 == 1 :
                sum = sum+i
            i=i+1
    else :
        j = y +1
        while j < x:
            if j%2 == 1 :
                sum = sum+j
            j=j+1
    print(sum)