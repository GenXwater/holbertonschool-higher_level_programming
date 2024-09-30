#!/usr/bin/python3
"""
This module defines a Student class with JSON serialization capabilities.
"""


class Student:
    """
    Defines a student with first_name, last_name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with the provided attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings only the specified attributes ar included
        Otherwise, all attributes are included.
        """
        if isinstance(attrs, list):
            stud_dict = {}
            for item in attrs:
                if isinstance(item, str):
                    if item == "first_name":
                        stud_dict["first_name"] = self.first_name
                    elif item == "last_name":
                        stud_dict["last_name"] = self.last_name
                    elif item == "age":
                        stud_dict["age"] = self.age
            return stud_dict
        else:
            return self.__dict__
