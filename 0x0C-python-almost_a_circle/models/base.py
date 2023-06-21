#!/usr/bin/python3

""" This module contains aBase class
"""
import json
import csv
import turtle


class Base:
    """
    A base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ An instance of base class created
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To represent in json format"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Return the object of json_string"""
        if not json_string or json_string == '':
            return list()
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json strings to json file"""
        new = []
        filename = cls.__name__ + ".json"

        if not list_objs or list_objs == None:
            new = new
        else:
            for item in list_objs:
                rep = item.to_dictionary()
                new.append(rep)

        json_data = cls.to_json_string(new)

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_data)

    @classmethod
    def create(cls, **dictionary):
        """ return the set attribute
        of class instance
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Invalid class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ laod from json file and return the list
        of all insatance with their attribute
        """
        filename = cls.__name__ + ".json"
        new = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                read = file.read()
        except FileNotFoundError:
            return new
        my_list = cls.from_json_string(read)
        for item in my_list:
            dict_rep = cls.create(**item)
            new.append(dict_rep)

        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save a python file into csv file"""

        if cls.__name__ == "Rectangle":
            fieldname = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldname = ["id", "size", "x", "y"]

        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldname)
            csv_writer.writeheader()
            for item in list_objs:
                rep = item.to_dictionary()
                csv_writer.writerow(rep)

    @classmethod
    def load_from_file_csv(cls):
        """ load and instantiate from csv file"""

        filename = cls.__name__ + ".csv"
        new = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":

                        row["id"] = int(row["id"])
                        row["width"] = int(row["width"])
                        row["height"] = int(row["height"])
                        row["x"] = int(row["x"])
                        row["y"] = int(row["y"])
                    elif cls.__name__ == "Square":
                        row["id"] = int(row["id"])
                        row["size"] = int(row["size"])
                        row["x"] = int(row["x"])
                        row["y"] = int(row["y"])
                    obj = cls.create(**row)
                    new.append(obj)
        except FileNotFoundError:
            pass
        return new

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ create a turtle object"""
        my_turtle = turtle.Turtle()

        my_turtle.speed(1)

        # Set up the turtle window
        window = turtle.Screen()
        window.bgcolor("white")

        # Draw rectangles
        for rectangle in list_rectangles:
            x = rectangle.x
            y = rectangle.y
            width = rectangle.width
            height = rectangle.height

            # Move to the starting position of the rectangle
            my_turtle.penup()
            my_turtle.goto(x, y)
            my_turtle.pendown()

            # Draw the rectangle
            for _ in range(2):
                my_turtle.forward(width)
                my_turtle.right(90)
                my_turtle.forward(height)
                my_turtle.right(90)

        # Draw squares
        for square in list_squares:
            x = square.x
            y = square.y
            size = square.size

            # Move to the starting position of the square
            my_turtle.penup()
            my_turtle.goto(x, y)
            my_turtle.pendown()

            # Draw the square
            for _ in range(4):
                my_turtle.forward(size)
                my_turtle.right(90)

        # Keep the window open until it is closed manually
        turtle.done()
