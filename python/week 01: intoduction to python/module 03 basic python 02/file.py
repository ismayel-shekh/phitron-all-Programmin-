# .csv comma sepnrated Value 
#text text file
with open('massage.txt','w') as file:
    file.write('I love you, python!')
with open('massage.txt','a') as file:
    file.write('I love you')
with open('massage.txt','r') as file:
    test = file.read();
    print(test)
