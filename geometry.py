import math

# Define some classes for shapes


class TwoDimensionalShape:
    def __init__(self):
        self.exists, self.shape, self.name = False, "", ""

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
        self.exists = abs(leg2 - leg1) < abs(bottom - top) < abs(leg2 +
                                                                 leg1) and top > 0 and bottom > 0 and leg1 > 0 and leg2 > 0
        self.shape = "Trapezoid"
        self.name = name
        self.a, self.b = min(top, bottom), max(top, bottom)
        self.c = leg1
        self.d = leg2
        self.h = (math.sqrt((-self.a + self.b + self.c + self.d) * (self.a - self.b + self.c + self.d) *
                            (self.a - self.b + self.c - self.d) * (self.a - self.b - self.c + self.d)) / (2 * abs(self.b - self.a)))

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
        self.angleA = math.degrees(
            math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
        self.angleB = math.degrees(
            math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
        self.angleC = math.degrees(
            math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
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


class Ellipse(TwoDimensionalShape):
    def __init__(self, name, radius1=0, radius2=0):
        self.exists = radius1 > 0 and radius2 > 0
        self.name = name
        self.r1 = radius1
        self.r2 = radius2
        if radius1 == radius2:
            self.shape = "Circle"
        else:
            self.shape = "Ellipse"

    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nRadius 1 = " + str(self.r1) + "\nRadius 2 = " + str(self.r2)

    def get_area(self):
        # Note that if r1==r2, formula evaluates to pi * r ** 2
        return math.pi * self.r1 * self.r2

    def get_perimeter(self):
        # Note that if r1==r2, h=0 and the below formula simplifies to 2r(pi)
        h = ((self.r1 - self.r2) ** 2) / ((self.r1 + self.r2) ** 2)
        return math.pi * (self.r1 + self.r2) * (1 + ((3 * h) / (10 + math.sqrt(4 - (3 * h)))))


class Circle(Ellipse):
    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nRadius = " + str(self.r1)


geometryCommands = ["back", "help", "create",
                    "area", "perimeter", "shapes", "view"]
twoDimensionalShapes = ["trapezoid", "isosceles trapezoid",
                        "parallelogram", "rhombus", "rectangle", "square", "triangle", "ellipse", "circle"]
myShapes = {}
BAD_INPUT = "Improper input. Returning to geometry menu...\n"
BAD_SHAPE = "Dimensions create an improper shape. Returning to geometry menu...\n"


def geometryMode():
    want2exit = False

    while not want2exit:
        command = input(
            "\nEnter a geometry command (see all with 'help', or type 'back'): ")
        print("\n")
        # Back to regular commands
        if command == geometryCommands[0]:
            print("Returning to main commands...")
            want2exit = True
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
                add_shape(shape.lower(), input("Enter a name for your Trapezoid: "), [input(
                    "Enter side a: "), input("Enter side b: "), input("Enter side c: "), input("Enter side d: ")])
            # Make an isosceles trapezoid
            elif shape.lower() == twoDimensionalShapes[1]:
                add_shape(shape.lower(), input("Enter a name for your Isosceles Trapezoid: "), [
                          input("Enter side a: "), input("Enter side b: "), input("Enter height: ")])
            # Make a parallelogram
            elif shape.lower() == twoDimensionalShapes[2]:
                add_shape(shape.lower(), input("Enter a name for your Parallelogram: "), [
                          input("Enter side a: "), input("Enter side b: "), input("Enter height: ")])
            # Make a rhombus
            elif shape.lower() == twoDimensionalShapes[3]:
                add_shape(shape.lower(), input("Enter a name for your Rhombus: "), [
                          input("Enter side length: "), input("Enter height: ")])
            # Make a rectangle
            elif shape.lower() == twoDimensionalShapes[4]:
                add_shape(shape.lower(), input("Enter a name for your Rectangle: "), [
                          input("Enter width: "), input("Enter height: ")])
            # Make a square
            elif shape.lower() == twoDimensionalShapes[5]:
                add_shape(shape.lower(), input("Enter a name for your Square: "), [
                          input("Enter side length: ")])
            # Make a triangle
            elif shape.lower() == twoDimensionalShapes[6]:
                add_shape(shape.lower(), input("Enter a name for your Triangle: "), [
                          input("Enter side a: "), input("Enter side b: "), input("Enter side c: ")])
            # Make an ellipse
            elif shape.lower() == twoDimensionalShapes[7]:
                add_shape(shape.lower(), input("Enter a name for your Ellipse: "), [
                          input("Enter radius 1: "), input("Enter radius 2: ")])
            # Make a circle
            elif shape.lower() == twoDimensionalShapes[8]:
                add_shape(shape.lower(), input("Enter a name for your Circle: "), [
                          input("Enter radius: ")])
            # No proper shape entered
            else:
                print(BAD_INPUT)
        # Area command
        elif command == geometryCommands[3]:
            display_shapes()
            shape = input("\nWhich shape would you like to get the area of? ")
            if shape in myShapes:
                print("Area = " + str(myShapes[shape].get_area()) + "\n")
            else:
                print("Shape not found.\n")
        # Perimeter command
        elif command == geometryCommands[4] or command == "circumference":
            display_shapes()
            shape = input(
                "\nWhich shape would you like to get the perimeter/circumference of? ")
            if shape in myShapes:
                print("Perimeter = " +
                      str(myShapes[shape].get_perimeter()) + "\n")
            else:
                print("Shape not found.\n")
        # Shapes command (lists all current shapes)
        elif command == geometryCommands[5]:
            print("Current shapes:")
            display_shapes()
        # View command (see dimensions of a shape)
        elif command == geometryCommands[6]:
            display_shapes()
            shape = input(
                "\nWhich shape would you like to see the dimensions of? ")
            if shape in myShapes:
                print("\n" + str(myShapes[shape]))
            else:
                print("\nNo shape by that name found")
        # Command not recognized
        else:
            print("No command by that name. Try typing 'list'\n")
    return


def add_shape(shape, shapeName, shapeProperties):
    if all(value.replace(".", "").isnumeric() for value in shapeProperties):
        shape2add = TwoDimensionalShape()
        # Trapezoid
        if shape == twoDimensionalShapes[0]:
            shape2add = Trapezoid(shapeName, float(shapeProperties[0]), float(
                shapeProperties[1]), float(shapeProperties[2]), float(shapeProperties[3]))
        # Isosceles Trapezoid
        elif shape == twoDimensionalShapes[1]:
            shape2add = IsoscelesTrapezoid(shapeName, float(shapeProperties[0]), float(
                shapeProperties[1]), float(shapeProperties[2]))
        # Parallelogram
        elif shape == twoDimensionalShapes[2]:
            shape2add = Parallelogram(shapeName, float(shapeProperties[0]), float(
                shapeProperties[1]), float(shapeProperties[2]))
        # Rhombus
        elif shape == twoDimensionalShapes[3]:
            shape2add = Rhombus(shapeName, float(
                shapeProperties[0]), float(shapeProperties[1]))
        # Rectangle
        elif shape == twoDimensionalShapes[4]:
            shape2add = Rectangle(shapeName, float(
                shapeProperties[0]), float(shapeProperties[1]))
        # Square
        elif shape == twoDimensionalShapes[5]:
            shape2add = Square(shapeName, float(shapeProperties[0]))
        # Triangle
        elif shape == twoDimensionalShapes[6]:
            shape2add = Triangle(shapeName, float(shapeProperties[0]), float(
                shapeProperties[1]), float(shapeProperties[2]))
        # Ellipse
        elif shape == twoDimensionalShapes[7]:
            shape2add = Ellipse(shapeName, float(
                shapeProperties[0]), float(shapeProperties[1]))
        # Circle
        elif shape == twoDimensionalShapes[8]:
            shape2add = Circle(shapeName, float(
                shapeProperties[0]), float(shapeProperties[0]))
        # Now decide if the shape is actually a shape
        if shape2add.exists:
            myShapes[shapeName] = shape2add
            print("\n" + str(myShapes[shapeName]))
        else:
            print(BAD_SHAPE)
    else:
        print(BAD_INPUT)


def display_shapes():
    for item in myShapes:
        print(item + " (" + myShapes[item].shape + ")")
