import math

def geometryMode():
    want2exit = False
    geometryCommands = ["back", "help", "create", "area", "perimeter", "shapes", "view"]
    twoDimensionalShapes = ["trapezoid", "isosceles trapezoid", "parallelogram", "rhombus", "rectangle", "square", "triangle"]
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
    
    class Triangle(TwoDimensionalShape):
        def __init__(self, name, a=0, b=0, c=0):
            self.exists = a > 0 and b > 0 and c > 0
            self.name = name
            self.a = a
            self.b = b
            self.c = c
            self.angleA = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
            self.angleB = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
            self.angleC = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
            self.h = a * math.sin(math.radians(self.angleC))
            # Determine what type of triangle
            if (self.angleA == 90 or self.angleB == 90 or self.angleC == 90) and (self.a == self.b or self.b == self.c or self.a == self.c):
                self.shape = "Right Isosceles Triangle"
            elif self.a == self.b == self.c:
                self.shape = "Equilateral Triangle"
            elif self.angleA == 90 or self.angleB == 90 or self.angleC == 90:
                self.shape = "Right Triangle"
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                self.shape = "Isosceles Triangle"
            elif self.angleA > 90 or self.angleB > 90 or self.angleC > 90:
                self.shape = "Obtuse Triangle"
            else:
                self.shape = "Triangle"

        def __str__(self):
            return "Dimensions of " + self.shape + " " + self.name + "\nSide a = " + str(self.a) + "\nSide b = " + str(self.b) + "\nSide c = " + str(self.c) + "\nAngle A = " + str(self.angleA) + " degrees\nAngle B = " + str(self.angleB) + " degrees\nAngle C = " + str(self.angleC) + " degrees\nHeight = " + str(self.h)

        def get_area(self):
            return self.a * self.b * math.sin(math.radians(self.angleC)) / 2

        def get_perimeter(self):
            return self.a + self.b + self.c
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
            # Make a triangle
            elif shape.lower() == twoDimensionalShapes[6]:
                shapeName = input("Enter a name for your Triangle: ")
                shapeProperties = [input("Enter side a: "), input("Enter side b: "), input("Enter side c: ")]
                print("\n")
                if all(value.replace(",", "").replace(".", "").isnumeric() for value in shapeProperties):
                    shape2add = Triangle(shapeName, float(shapeProperties[0]), float(shapeProperties[1]), float(shapeProperties[2]))
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
                print("\n" + str(myShapes[shape]))
            else:
                print("\nNo shape by that name found")
        # TODO: Add more commands
        # Command not recognized
        else:
            print("No command by that name. Try typing 'list'\n")

    return