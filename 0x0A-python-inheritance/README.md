#Inheritance
syntax for a derived class definition looks like this:

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. 
DerivedClassName() creates a new instance of the class. 
Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

python has two built-in functions that work with inheritance:

Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.


#Multiple Inheritance
A class definition with multiple base classes looks like this:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
the method resolution order changes dynamically to support cooperative calls to super().
This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.
Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships 


#Benefits of inheritance are:

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Inheritance offers a simple, understandable model structure. 
Less development and maintenance expenses result from an inheritance.

#The syntax of simple inheritance in Python is as follows:
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}

#Creating a Parent Class
A parent class is a class whose properties are inherited by the child class. Let’s create a parent class called Person which has a Display method to display the person’s information.

# A Python program to demonstrate inheritance
class Person(object):

# Constructor
def __init__(self, name, id):
	self.name = name
	self.id = id

# To check if this person is an employee
def Display(self):
	print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()

#Creating a Child Class
A child class is a class that drives the properties from its parent class. Here Emp is another class that is going to inherit the properties of the Person class(base class).

class Emp(Person):

def Print(self):
	print("Emp class called")
	
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()


#output
Mayank 103
Emp class called



#Example of Inheritance in Python 
Let us see an example of simple Python inheritance in which a child class is inheriting the properties of its parent class. In this example, ‘Person’ is the parent class, and ‘Employee’ is its child class.

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class Person(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())

output
Geek1 False
Geek2 True
