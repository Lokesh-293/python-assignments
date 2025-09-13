# #functions scope
# # 4 types 
# # local scope which can access values inside the function 
# # global scope which can access any where.
# # enclosed scope ,where the outer the variable can be called in the inner function 
def outer():
    str='lo'
    def inner():
        print(str)



# #  the variables which exist by default in python called built-in scope.

# # when one variable is given as global and local ,so the preference is given to local for same variable name called global shadowing

user_name = 'lokii'
def first_function():
    user_name = 'lokiii'
    def second_function():
        user_name = 'lokiiii'
        print(user_name)          #preference to local scope
    second_function()
    print(user_name)
first_function()
print(user_name)       


user_name = 'lokii'
def first_function():
    user_name = 'lokiii'
    def second_function():
        print(user_name)          #prefernce to enclosed scope
    second_function()
    print(user_name)
first_function()
print(user_name)       


user_name = 'lokii'
def first_function():
    
    def second_function():
        
        print(user_name)          #preference to global scope
    second_function()
    print(user_name)
first_function()
print(user_name)       


# calling a global vavriable inside the function
# globals()['num1']=90


# nonlocal scope which we call the variable which is enclosed scope

num=1
def first_check():
    num=10
    def second_check():
        num1=100
        def third_check():
            num=1000
            nonlocal num1       #first priority is nearest local variable
        print(num1)
        third_check()
        print(num)
    second_check()
    print(num)
first_check()
print(num)        