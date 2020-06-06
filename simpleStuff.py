import random
import math

commandList = ["help", "exit", "math", "dice", "palindrome", "geometry"]
geometryList = ["back"]
want2exit = False

# The following function is called for geometry functionality


def geometryMode():
    want2exit = False
    geometryCommands = ["back", "help", "create", "area", "perimeter", "shapes", "view"]
    twoDimensionalShapes = ["trapezoid", "isosceles trapezoid", "parallelogram", "rhombus", "rectangle", "square"]
    myShapes = {}
    BAD_INPUT = "Improper input. Returning to geometry menu...\n"
    BAD_SHAPE = "Dimensions create an improper shape. Returning to geometry menu...\n"

    # Define some classes for shapes
    class TwoDimensionalShape:
        def __init__(self):
            self.exists, self.shape, self.name = False, "None", ""

        def __str__(self):
            # Function to print dimensional values
            pass

        def get_area(self):
            # Function to calculate the area of the shape
            pass

        def get_perimeter(self):
            # Function to calculate the perimeter/circumference of the shape
            pass

    class Trapezoid(TwoDimensionalShape):
        def __init__(self, name, top=0, bottom=0, leg1=0, leg2=0):
            self.exists = abs(leg2 - leg1) < abs(bottom - top) < abs(leg2 + leg1) and top > 0 and bottom > 0 and leg1 > 0 and leg2 > 0
            self.shape = "Trapezoid"
            self.name = name
            self.a, self.b = min(top, bottom), max(top, bottom)
            self.c = leg1
            self.d = leg2
            self.h = (math.sqrt((-self.a + self.b + self.c + self.d) * (self.a - self.b + self.c + self.d) * (
                self.a - self.b + self.c - self.d) * (self.a - self.b - self.c + self.d)) / (2 * abs(self.b - self.a)))

        def __str__(self):
            return "Dimensions of " + self.shape + " " + self.name + ":\nBase a = " + str(self.a) + "\nBase b = " + str(self.b) + "\nSide c = " + str(self.c) + "\nSide d = " + str(self.d) + "\nHeight = " + str(self.h) + "\n"

        def get_area(self):
            return (self.a + self.b) / 2 * self.h

        def get_perimeter(self):
            return self.a + self.b + self.c + self.d

    class IsoscelesTrapezoid(Trapezoid):
        def __init__(self, name, top=0, bottom=0, height=0):
            self.exists = top > 0 and bottom > 0 and height > 0
            self.shape = "Isosceles Trapezoid"
            self.name = name
            self.a, self.b = min(top, bottom), max(top, bottom)
            self.h = height
            self.c = self.d = (math.sqrt(
                4 * self.h ** 2 + self.a ** 2 - 2 * self.a * self.b + self.b ** 2) / 2)

    class Parallelogram(Trapezoid):
        def __init__(self, name, base=0, sides=0, height=0):
            self.exists = base > 0 and sides > 0 and height > 0
            self.shape = "Parallelogram"
            self.name = name
            if height > sides:
                self.a = self.b = sides
                self.c = self.d = base
            else:
                self.a = self.b = base
                self.c = self.d = sides
            self.h = height

        def __str__(self):
            return "Dimensions of " + self.shape + " " + self.name + ":\nParallel sides a = " + str(self.a) + "\nParallel sides b = " + str(self.c) + "\nHeight = " + str(self.h) + "\n"

    class Rhombus(Parallelogram):
        def __init__(self, name, side=0, height=0):
            self.exists = side > 0 and height > 0 and side >= height
            self.shape = "Rhombus"
            self.name = name
            self.a = self.b = self.c = self.d = side
            self.h = height
        
        def __str__(self):
            return "Dimensions of " + self.shape + " " + self.name + ":\nSide length a = " + str(self.a) + "\nHeight = " + str(self.h) + "\n"
    
    class Rectangle(Parallelogram):
        def __init__(self, name, height=0, width=0):
            self.exists = height > 0 and width > 0
            self.shape = "Rectangle"
            self.name = name
            self.a = self.b = width
            self.c = self.d = self.h = height

        def __str__(self):
            return "Dimensions of " + self.shape + " " + self.name + "\nWidth = " + str(self.a) + "\nHeight = " + str(self.h) + "\n"

    class Square(Rectangle):
        def __init__(self, name, side=0):
            super().__init__(name, side, side)
            self.shape = "Square"
        
    #
    #   TODO: Add more shapes
    #

    while not want2exit:
        command = input("\nEnter a geometry command (see all with 'help', or type 'back'): ")
        print("\n")
        # Back to regular commands
        if command == geometryCommands[0]:
            secondCommand = input(
                "Are you sure you want to go back? You'll lose any shapes you've made here (yes/no): ")
            if secondCommand in ["yes", "YES", "Yes", "Y", "y"]:
                print("Returning to main commands...")
                want2exit = True
            else:
                print("Cancelled")
        # List all commands
        elif command == geometryCommands[1]:
            print("Here is a list of all geometry commands:")
            for keyword in geometryCommands:
                print(keyword)
        # Create shape command
        elif command == geometryCommands[2]:
            for item in twoDimensionalShapes:
                print(item)
            shape = input("\nWhat type of shape would you like to create? ")
            # Make a trapezoid
            if shape.lower() == twoDimensionalShapes[0]:
                shapeName = input("Enter a name for your Trapezoid: ")
                shapeProperties = [input("Enter side a: "), input("Enter side b: "), input("Enter side c: "), input("Enter side d: ")]
                print("\n")
                if all(value.replace(",", "").replace(".", "").isnumeric() for value in shapeProperties):
                    shape2add = Trapezoid(shapeName, float(shapeProperties[0]), float(shapeProperties[1]), float(shapeProperties[2]), float(shapeProperties[3]))
                    if shape2add.exists:
                        myShapes[shapeName] = shape2add
                        print(myShapes[shapeName])
                    else:
                        print(BAD_SHAPE)
                else:
                    print(BAD_INPUT)
            # Make an isosceles trapezoid
            elif shape.lower() == twoDimensionalShapes[1]:
                shapeName = input(
                    "Enter a name for your Isosceles Trapezoid: ")
                shapeProperties = [input("Enter side a: "), input("Enter side b: "), input("Enter height: ")]
                print("\n")
                if all(value.replace(",", "").replace(".", "").isnumeric() for value in shapeProperties):
                    shape2add = IsoscelesTrapezoid(shapeName, float(shapeProperties[0]), float(shapeProperties[1]), float(shapeProperties[2]))
                    if shape2add.exists:
                        myShapes[shapeName] = shape2add
                        print(myShapes[shapeName])
                    else:
                        print(BAD_SHAPE)
                else:
                    print(BAD_INPUT)

            # Make a parallelogram
            elif shape.lower() == twoDimensionalShapes[2]:
                shapeName = input(
                    "Enter a name for your Parallelogram: ")
                shapeProperties = [input("Enter side a: "), input("Enter side b: "), input("Enter height: ")]
                print("\n")
                if all(value.replace(",", "").replace(".", "").isnumeric() for value in shapeProperties):
                    shape2add = Parallelogram(shapeName, float(shapeProperties[0]), float(shapeProperties[1]), float(shapeProperties[2]))
                    if shape2add.exists:
                        myShapes[shapeName] = shape2add
                        print(myShapes[shapeName])
                    else:
                        print(BAD_SHAPE)
                else:
                    print(BAD_INPUT)
            # Make a rhombus
            elif shape.lower() == twoDimensionalShapes[3]:
                shapeName = input("Enter a name for your Rhombus: ")
                shapeProperties = [input("Enter side length: "), input("Enter height: ")]
                print("\n")
                if all(value.replace(",", "").replace(".", "").isnumeric() for value in shapeProperties):
                    shape2add = Rhombus(shapeName, float(shapeProperties[0]), float(shapeProperties[1]))
                    if shape2add.exists:
                        myShapes[shapeName] = shape2add
                        print(myShapes[shapeName])
                    else:
                        print(BAD_SHAPE)
                else:
                    print(BAD_INPUT)
            # Make a rectangle
            elif shape.lower() == twoDimensionalShapes[4]:
                shapeName = input("Enter a name for your Rectangle: ")
                shapeProperties = [input("Enter width: "), input("Enter height: ")]
                print("\n")
                if all(value.replace(",", "").replace(".", "").isnumeric() for value in shapeProperties):
                    shape2add = Rectangle(shapeName, float(shapeProperties[0]), float(shapeProperties[1]))
                    if shape2add.exists:
                        myShapes[shapeName] = shape2add
                        print(myShapes[shapeName])
                    else:
                        print(BAD_SHAPE)
                else:
                    print(BAD_INPUT)
            # Make a square
            elif shape.lower() == twoDimensionalShapes[5]:
                shapeName = input("Enter a name for your Square: ")
                shapeProperties = [input("Enter side length: ")]
                print("\n")
                if all(value.replace(",", "").replace(".", "").isnumeric() for value in shapeProperties):
                    shape2add = Square(shapeName, float(shapeProperties[0]))
                    if shape2add.exists:
                        myShapes[shapeName] = shape2add
                        print(myShapes[shapeName])
                    else:
                        print(BAD_SHAPE)
                else:
                    print(BAD_INPUT)
            # No proper shape entered
            else:
                print(BAD_INPUT)
        # Area command
        elif command == geometryCommands[3]:
            for item in myShapes: print(item + " (" + myShapes[item].shape + ")")
            shape = input("\nWhich shape would you like to get the area of? ")
            if shape in myShapes:
                print("Area = " + str(myShapes[shape].get_area()) + "\n")
            else:
                print("Shape not found.\n")
        # Perimeter command
        elif command == geometryCommands[4]:
            for item in myShapes: print(item + " (" + myShapes[item].shape + ")")
            shape = input("\nWhich shape would you like to get the perimeter/circumference of? ")
            if shape in myShapes:
                print("Perimeter = " + str(myShapes[shape].get_perimeter()) + "\n")
            else:
                print("Shape not found.\n")
        # Shapes command (lists all current shapes)
        elif command == geometryCommands[5]:
            print("Current shapes:")
            for item in myShapes: print(item + " (" + myShapes[item].shape + ")")
        # View command (see dimensions of a shape)
        elif command == geometryCommands[6]:
            for item in myShapes: print(item + " (" + myShapes[item].shape + ")")
            shape = input("\nWhich shape would you like to see the dimensions of? ")
            if shape in myShapes:
                print("\n" + myShapes[shape])
            else:
                print("\nNo shape by that name found")
        # TODO: Add more commands
        # Command not recognized
        else:
            print("No command by that name. Try typing 'list'\n")

    return


# Here is the main function
while not want2exit:
    command = input("Please enter a command (or type 'help'): ")
    print("\n")
    if command in commandList:
        # Help command
        if command == commandList[0]:
            print("Here is a list of all commands:")
            for keyword in commandList:
                print(keyword)
        # Exit command
        elif command == commandList[1]:
            print("Exiting program...")
            want2exit = True
        # Math command
        elif command == commandList[2]:
            maths = input(
                "Enter an equation in the form [number] [operation] [number]: ").strip().split()
            if len(maths) == 3:
                try:
                    if maths[1] == "+":
                        print(maths[0] + " " + maths[1] + " " + maths[2] +
                              " = " + str(float(maths[0]) + float(maths[2])))
                    elif maths[1] == "-":
                        print(maths[0] + " " + maths[1] + " " + maths[2] +
                              " = " + str(float(maths[0]) - float(maths[2])))
                    elif maths[1] == "*":
                        print(maths[0] + " " + maths[1] + " " + maths[2] +
                              " = " + str(float(maths[0]) * float(maths[2])))
                    elif maths[1] == "/":
                        print(maths[0] + " " + maths[1] + " " + maths[2] +
                              " = " + str(float(maths[0]) / float(maths[2])))
                    elif maths[1] == "%":
                        print(maths[0] + " " + maths[1] + " " + maths[2] +
                              " = " + str(float(maths[0]) % float(maths[2])))
                    elif maths[1] == "\\":
                        print(maths[0] + " " + maths[1] + " " + maths[2] +
                              " = " + str(float(maths[0]) // float(maths[2])))
                    else:
                        print("Invalid input")
                except:
                    print("Invalid input")
            else:
                print("Invalid operation")
        # Dice command
        elif command == commandList[3]:
            sides = input("How many sides on your dice? ")
            try:
                print("You rolled a " + str(random.randint(1, int(sides))))
            except:
                print("A dice cannot have " + sides + " sides!")
        # Palindrome command
        elif command == commandList[4]:
            word = input("Enter a word: ")
            backWord = word[::-1]
            if word == backWord:
                print(word + " is a palindrome")
            else:
                print(word + " is not a palindrome")
        # Geometry command
        elif command == commandList[5]:
            print("Entering geometry mode...")
            geometryMode()
        # TODO: Add more commands here
        # This line should technically never run but just in case it's here
        else:
            print("Something happened that shouldn't have happened...?")
    else:
        print("Command not found")
    print("\n")
