# Object-Oriented Programming (OOP) in Python: A Summary

## General
This document provides a summary of key Object-Oriented Programming (OOP) concepts in Python, covering classes, objects, attributes, and methods.

### 1. **What is OOP?**
Object-Oriented Programming (OOP) is a programming paradigm where data and behavior are encapsulated within "objects" based on defined "classes."

### 2. **“First-class everything”**
In Python, everything is treated as an object, including functions, classes, and even primitive data types. This allows functions and objects to be passed as arguments, stored in variables, and returned from other functions.

### 3. **What is a class?**
A **class** is a blueprint for creating objects. It defines attributes (data) and methods (behavior) that its instances will have.

### 4. **What is an object and an instance?**
An **object** is a specific instance of a class. When a class is instantiated, it creates an object with its own state and behaviors.

### 5. **Difference between a class and an object or instance**
- A **class** is the blueprint or template.
- An **object** (or instance) is a concrete realization of that class.

### 6. **What is an attribute?**
An **attribute** is a variable associated with a class or instance. Attributes store the state or data of an object.

### 7. **Public, Protected, and Private attributes**
- **Public**: Accessible from anywhere.
- **Protected** (`_attribute`): Intended for internal use in the class or subclass but still accessible.
- **Private** (`__attribute`): Restricted to be used within the class itself.

### 8. **What is `self`?**
`self` is a reference to the current instance of the class. It allows access to instance attributes and methods from within the class.

### 9. **What is a method?**
A **method** is a function defined inside a class that operates on objects of that class.

### 10. **What is the special `__init__` method?**
`__init__` is the constructor method called when a new instance of a class is created. It initializes the instance’s attributes.

### 11. **Data Abstraction, Encapsulation, and Information Hiding**
- **Abstraction**: Showing only necessary details.
- **Encapsulation**: Bundling data and methods into a single unit (class).
- **Information Hiding**: Restricting direct access to certain parts of an object (via private attributes).

### 12. **What is a property?**
A **property** allows methods to be accessed like attributes, using the `@property` decorator. It is useful for controlling access to instance attributes.

### 13. **Difference between an attribute and a property**
- **Attribute**: A variable that holds data directly.
- **Property**: A method that acts like an attribute, often used to manage access to attributes.

### 14. **Pythonic way to write getters and setters**
Use the `@property` decorator for the getter, and `@attribute_name.setter` for the setter. This avoids the need for explicit getter/setter methods.

```python
@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    self._name = value
