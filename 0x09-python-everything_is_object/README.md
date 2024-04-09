#Mutable Data
Adding state to data is a central ingredient of a paradigm called object-oriented programming.
The Object Metaphor
functions performed operations and data were operated upon.
functions could be manipulated as data, but could also be called to perform computation.
A date is a kind of object.
>>> from datetime import date.
The name date is bound to a class. As we have seen, a class represents a kind of value. Individual dates are called instances of that class


Sequence Objects
Instances of primitive built-in values such as numbers are immutable. The values themselves cannot change over the course of program execution. Lists on the other hand are mutable.
>>> chinese = ['coin', 'string', 'myriad']  # A list literal
>>> suits = chinese                         # Two names refer to the same list
