#list -> []
#tuple -> ()
#set -> {}
# set is unique items collection no duplicate
num = [12, 45, 36,6,9,55]
num_set = set(num)
print(num_set)
# num_set[5] = 40
num_set.add(100)
num_set.remove(55)
print(num_set)
A = {1,5,2,6}
B = {1,6,4,5}
print(A & B)
print(A | B) #AUB