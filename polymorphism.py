#polymorphism which the same thing acting in different ways in different situations






#operator overloading
class marks:
    def __init__(self ,so_marks,ma_marks):
        self.so_marks=so_marks
        self.ma_marks=ma_marks
    def __add__(self,other):
        print(self.so_marks + other.so_marks) 
        print(self.ma_marks + other.ma_marks)

        

m1=marks(23,34)
m2=marks(45,43)
m1+m2
class marks1:
    def __init__(self , so_marks , ma_marks , hi_marks):
        self.so_marks = so_marks
        self.ma_marks=ma_marks
        self.hi_marks=hi_marks

mar=marks1(12,23,45)        
        
m1+mar


#method overloading
#in one class with same method with same parameter we can call the function based on parameters
#when it comes to python it won't work but can work indirectly keyword arbitary arguments
def add(*a):
    return sum(a)


print(add(2))
print(add(9,9,9))
print(add(0,5))



#method overridding
#writting same method writting in parent and child class 
#it depends on the object when it comes to polymorphism method overriding 


