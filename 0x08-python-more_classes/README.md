#Python - More Classes and Objects

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type int which translates to saying that variables that store integers are variables which are instances (objects) of the int class.


The self
Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.


Classes
The simplest class possible is shown in the following example (save as oop_simplestclass.py).

class Person:
    pass  # An empty block

p = Person()
print(p)
Output:

$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>

Methods
We have already discussed that classes/objects can have methods just like functions except that we have an extra self variable. We will now see an example (save as oop_method.py).

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
Output:

$ python oop_method.py
Hello, how are you?


