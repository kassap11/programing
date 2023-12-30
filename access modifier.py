# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:42:40 2023

@author: dell
"""

# class super ():
#     _name=None
#     _age=None
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def _display(self):
#         print("your name is "+self._name)
#         print("your age is "+self._age)
        
# class pop(super):
      # def __init__(self,name,age):           # protected access modifier
#            super.__init__(self,name,age)
           
#        def what(self):
#            print("Name: ", self._name) 
           
# oop=pop("keso",22) 
# oop.what()
    


class geek():
    __name=None
    def __init__(self,name):
        self.__name=name
        
    def dipslay(self):
        print(self.__name)
                                  #private access modifier
    def get_name(self):
        self.__name 
        
	# setter method name
    def set_name(self , name):
        self.__name = name 
    
        


      

           