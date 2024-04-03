#Python - Classes and Objects
A class creates a new type where objects are instances of the class.
Variables that belong to an object or class are referred to as fields.
Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class. This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.
Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.




Classes
The simplest class possible is shown in the following example (save as oop_simplestclass.py).

class Person:
    pass  # An empty block

p = Person()
print(p)
Output:

$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>



How It Works

We create a new class using the class statement and the name of the class. This is followed by an indented block of statements which form the body of the class. In this case, we have an empty block which is indicated using the pass statement.

Next, we create an object/instance of this class using the name of the class followed by a pair of parentheses. (We will learn more about instantiation in the next section). For our verification, we confirm the type of the variable by simply printing it. It tells us that we have an instance of the Person class in the __main__ module.

Notice that the address of the computer memory where your object is stored is also printed. The address will have a different value on your computer since Python can store the object wherever it finds space.


Methods
We have already discussed that classes/objects can have methods just like functions except that we have an extra self variable. We will now see an example (save as oop_method.py).

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
                                                                
