# class parent():
#     def __init__(self):
#         self.value="i am a parent"
        
#     def show(self):
#         print(self.value)
# class child(parent):
#     def __init__(self):
#         self.value="i am a child"
        
#     def show(self):                   
#         print(self.value)
                            #this is overriding#
# q1=parent()
# q1.show()
# q2=child()
# q2.show()        


def product(x,y):
    p=x*y
    print(p)
    
def product(x,y,z):
    p=x*y*z
    print(p)    
    
#product(8,8)  
product(8,8,8) 

def add(a=None,b=None):
    if a !=None and b==None:
        print (a)                   #the solution od overloading
    else:
        print(a+b)
        
add(2,2)
add(3)        

from multipledispatch import dispatch
@dispatch(int,int,int)
def prod(x,y,z):
    w=x*y*z
    print(w)
    
@dispatch(float,float,float)
def prod(x,y,z):
    w=x*y*z
    print(w)
    
        
prod(2, 3, 2) # this will give output of 12

# calling product method with 3 arguments but all float
prod(2.2, 3.4, 2.3)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    