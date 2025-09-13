class python:
    def __init__(self , name):
        self.name = name

    def show (self):
        print(self.name)

class addition(python):
    def learned(self):
        print("addition of numbers finished")

class inbuilt:
    def inbuilt(self):
        print("inbuilt as started")

class inbuiltvariable(python , inbuilt):
    def both(self):
        print("inbuilt variable methods started")  


class inbuiltmethod(addition , inbuiltvariable): 
    def inbuilts(self):
        print('methods as finished')   

class  problem(addition):
    def prime(self):
        print('prime number finished')     


class oops(addition , inbuilt):
    def  start(self):
        print('oops covered')                   
    
            

print("single inheritence")
c1=addition('problem solving started')
c1.show()   
c1.learned() 

print("multiple inheritence")
c2=inbuiltvariable('inbuilt variable')
c2.show()
c2.inbuilt()
c2.both()


print('multi level inheritence')
c3=inbuiltmethod('methods')
c3.learned()
c3.inbuilt()
c3.show()
c3.inbuilts()


print('hierarchical')
c4 = problem('prime')
c4.show()
c4.prime()


print('hybrid')
c5 = oops('all finished')
c5.show()
c5.inbuilt()
c5.start()




