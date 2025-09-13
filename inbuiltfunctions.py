list1=[1,2,3]
list1.insert (-2, [1,5,8])
print(list1)



list1=[1,2,3]
list1.insert (-2, (1,5,8))
print(list1)


list1=[1,2,3]
list1.insert (-2, 1,5,8)   #TypeError: insert expected 2 arguments, got 4
print(list1)



list1=[1,2,3]
list1.pop (2,3)  #TypeError: pop expected at most 1 argument, got 2
print(list1)

list1=[1,2,3]
res=list1.pop (2)
print(list1)
print(res)



list1=[1,2,3]
list1.remove (2)
print(list1)

list1=[1,2,3]
list1.remove (2,3)  #TypeError: list.remove() takes exactly one argument (2 given)
print(list1)


list1=[1,2,3]
list1.append (90)  
print(list1)




list1=[1,2,3]
list1.append [90]    #TypeError: 'builtin_function_or_method' object is not subscriptable
print(list1)


list1=[1,2,3,66,77,66,99]

print(list1.index(66,2,6))  #prints only first number


list1=[1,2,3,66,77,88,99]

print(list1.index(66))


list1=[1,2,3,66,77,66,99]

print(list1.index(66,-3,-7))   #ValueError: 66 is not in list