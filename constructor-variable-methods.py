class mobile:
    mobile_name = "Iphone"  #class and static variable 
    def __init__(self , model , name , price):
        self.model = model                            #instance variable
        self.name = name
        self.price = price
        print("object is created")

        #instance method
    def phone(self):
        print('phone model:',self.model)
        print('phone name :',self.name)
        print('phone price:',self.price)

        #class method
    @classmethod                            #it should be written with decorator
    def change_mobile_name(cls,Samsung):
        cls.mobile_name=Samsung  
        def change_mobile_name(cls,vivo):
         cls.mobile_name= vivo    
  


    #static method
    @staticmethod
    def describe_about_phone():
        print("The most secured mobile with unique features")    


clc1=mobile(2025,'Iphone 16',150000)
clc1.phone()                            #accessing instance method with object
clc1.change_mobile_name('Samsung')       #accessing class method with object
print(clc1.mobile_name)
mobile.phone(clc1)                      #we can access class name with instance method if we pass object
# mobile.phone()                          # we cannot access instance method with class name 
mobile.describe_about_phone()              #accessing static method with class name
clc1.describe_about_phone()                #accessing static method with object


mobile.change_mobile_name('vivo')
print(mobile.mobile_name)                   #accessing class name with class method

#mobile.name                                  # cannot access instance variable with class name
print(clc1.mobile_name)                    #accessing class variable with object
                

print(clc1.name)                           #can access instance variable with object
