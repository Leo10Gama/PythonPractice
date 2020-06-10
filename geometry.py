import math

# Define some classes for shapes


class Shape:
    def __init__(self):
        self.exists, self.shape, self.name = False, "", ""

    def __str__(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def get_surface_area(self):
        pass

    def get_volume(self):
        pass


class Trapezoid(Shape):
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


class Triangle(Shape):
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


class Ellipse(Shape):
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


class Ellipsoid(Shape):
    def __init__(self, name, a=0, b=0, c=0):
        self.exists = a > 0 and b > 0 and c > 0
        self.name = name
        self.a, self.b, self.c = a, b, c
        if a != b != c:
            self.shape = "Ellipsoid"
        elif a == b == c:
            self.shape = "Sphere"
        else:
            self.shape = "Spheroid"

    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nRadius a = " + str(self.a) + "\nRadius b = " + str(self.b) + "\nRadius c = " + str(self.c)

    def get_surface_area(self):
        p = 1.6075
        return 4 * math.pi * (((((self.a ** p) * (self.b ** p)) + ((self.a ** p) * (self.c ** p)) + ((self.b ** p) * (self.c ** p))) / 3) ** (1 / p))

    def get_volume(self):
        return (4 / 3) * math.pi * self.a * self.b * self.c


class Spheroid(Ellipsoid):
    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nRadius a = " + str(self.a) + "\nRadius c = " + str(self.c)


class Sphere(Spheroid):
    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nRadius r = " + str(self.a)


class Cone(Shape):
    def __init__(self, name, r=0, h=0):
        self.exists = r > 0 and h > 0
        self.name = name
        self.shape = "Cone"
        self.r, self.h = r, h
        self.l = math.sqrt((r ** 2) + (h ** 2))

    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nRadius r = " + str(self.r) + "\nHeight h = " + str(self.h) + "\nSlant height l = " + str(self.l)

    def get_surface_area(self):
        return (math.pi * self.r * self.r) + (math.pi * self.r * self.l)

    def get_volume(self):
        return (1 / 3) * math.pi * self.r * self.r * self.h


class Cylinder(Shape):
    def __init__(self, name, r=0, h=0):
        self.exists = r > 0 and h > 0
        self.name = name
        self.shape = "Cylinder"
        self.r, self.h = r, h

    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nRadius r = " + str(self.r) + "\nHeight h = " + str(self.h)

    def get_surface_area(self):
        return (2 * math.pi * self.r) * (self.h + self.r)

    def get_volume(self):
        return math.pi * self.r * self.r * self.h


class Prism(Shape):
    def __init__(self, name, n=0, s=0, h=0):
        self.exists = n > 2 and s > 0 and h > 0
        self.name = name
        self.shape = str(n) + "-sided face Prism"
        self.n, self.s, self.h = n, s, h

    def __str__(self):
        return "Dimensions of " + self.shape + " " + self.name + "\nSide length s = " + str(self.s) + "\nHeight h = " + str(self.h)

    def get_surface_area(self):
        return (self.n / 2) * self.s * self.s * (math.cos(math.pi / self.n) / math.sin(math.pi / self.n)) + self.n * self.s * self.h

    def get_volume(self):
        return (self.n / 4) * self.h * self.s * self.s * (math.cos(math.pi / self.n) / math.sin(math.pi / self.n))


class Pyramid(Prism):
    def __init__(self, name, n=0, s=0, h=0):
        super().__init__(name, n, s, h)
        self.shape = str(n) + "-sided face Pyramid"

    def get_surface_area(self):
        p = self.n * self.s
        a = self.s / (2 * math.tan((2 * math.pi) / self.n))
        l = math.sqrt((a ** 2) + (self.h ** 2))
        B = (p * a) / 2
        return ((p * l) / 2) + B

    def get_volume(self):
        return (self.n / 12) * self.h * self.s * self.s * (math.cos(math.pi / self.n) / math.sin(math.pi / self.n))


geometryCommands = ["back", "help", "create",
                    "area", "perimeter", "shapes", "view", "surface area", "volume"]
twoDimensionalShapes = ["trapezoid", "isosceles trapezoid",
                        "parallelogram", "rhombus", "rectangle", "square", "triangle", "ellipse", "circle"]
threeDimensionalShapes = ["ellipsoid",
                          "spheroid", "sphere", "cone", "cylinder", "prism", "pyramid"]
myShapes = {}
BAD_INPUT = "Improper input. Returning to geometry menu...\n"
BAD_SHAPE = "Dimensions create an improper shape. Returning to geometry menu...\n"
NO_SHAPE = "No shape by that name found\n"


# Actual function to begin doing geometry
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
            dimensions = input(
                "\nHow many dimensions will your shape have? (2 or 3): ")
            # Make a 2D Shape
            if dimensions == "2":
                for item in twoDimensionalShapes:
                    print(item)
                shape = input(
                    "\nWhat type of shape would you like to create? ")
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
            # Make a 3D shape
            elif dimensions == "3":
                for item in threeDimensionalShapes:
                    print(item)
                shape = input(
                    "\nWhat type of shape would you like to create? ")
                # Make an ellipsoid
                if shape.lower() == threeDimensionalShapes[0]:
                    add_shape(shape.lower(), input("Enter a name for your Ellipsoid: "), [input(
                        "Enter radius a: "), input("Enter radius b: "), input("Enter radius c: ")])
                # Make a spheroid
                elif shape.lower() == threeDimensionalShapes[1]:
                    add_shape(shape.lower(), input("Enter a name for your Spheroid: "), [
                              input("Enter radius a: "), input("Enter radius c: ")])
                # Make a sphere
                elif shape.lower() == threeDimensionalShapes[2]:
                    add_shape(shape.lower(), input("Enter a name for your Sphere: "), [
                              input("Enter a radius: ")])
                # Make a cone
                elif shape.lower() == threeDimensionalShapes[3]:
                    add_shape(shape.lower(), input("Enter a name for your Cone: "), [
                              input("Enter radius: "), input("Enter height: ")])
                # Make a cylinder
                elif shape.lower() == threeDimensionalShapes[4]:
                    add_shape(shape.lower(), input("Enter a name for your Cylinder: "), [
                              input("Enter radius: "), input("Enter height: ")])
                # Make a prism
                elif shape.lower() == threeDimensionalShapes[5]:
                    add_shape(shape.lower(), input("Enter a name for your Prism: "), [input(
                        "How many sides will the prism's face have? "), input("How long will each side of the face be? "), input("Enter height: ")])
                # Make a pyramid
                elif shape.lower() == threeDimensionalShapes[6]:
                    add_shape(shape.lower(), input("Enter a name for your Pyramid: "), [input(
                        "How many sides will the pyramid's face have? "), input("How long will each side of the face be? "), input("Enter height: ")])
                # No proper shape entered
                else:
                    print(BAD_INPUT)
            # No proper shape entered
            else:
                print(BAD_INPUT)
        # Area command
        elif command == geometryCommands[3]:
            display_shapes()
            shape = input("\nWhich shape would you like to get the area of? ")
            if shape in myShapes:
                print("\nArea = " + str(myShapes[shape].get_area()) + "\n")
            else:
                print(NO_SHAPE)
        # Perimeter command
        elif command == geometryCommands[4] or command == "circumference":
            display_shapes()
            shape = input(
                "\nWhich shape would you like to get the perimeter/circumference of? ")
            if shape in myShapes:
                print("\nPerimeter = " +
                      str(myShapes[shape].get_perimeter()) + "\n")
            else:
                print(NO_SHAPE)
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
                print(NO_SHAPE)
        # Surface Area command
        elif command == geometryCommands[7]:
            display_shapes()
            shape = input(
                "\nWhich shape would you like to get the surface area of? ")
            if shape in myShapes:
                print("\nSurface Area = " +
                      str(myShapes[shape].get_surface_area()))
            else:
                print(NO_SHAPE)
        # Volume command
        elif command == geometryCommands[8]:
            display_shapes()
            shape = input(
                "\nWhich shape would you like to get the volume of? ")
            if shape in myShapes:
                print("\nVolume = " + str(myShapes[shape].get_volume()))
            else:
                print(NO_SHAPE)
        # Command not recognized
        else:
            print("No command by that name. Try typing 'help'\n")
    return


def add_shape(shape, shapeName, shapeProperties):
    if all(value.replace(".", "").isnumeric() for value in shapeProperties):
        shape2add = Shape()
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
        # Ellipsoid
        elif shape == threeDimensionalShapes[0]:
            shape2add = Ellipsoid(shapeName, float(shapeProperties[0]), float(
                shapeProperties[1]), float(shapeProperties[2]))
        # Spheroid
        elif shape == threeDimensionalShapes[1]:
            shape2add = Spheroid(shapeName, float(shapeProperties[0]), float(
                shapeProperties[0]), float(shapeProperties[1]))
        # Sphere
        elif shape == threeDimensionalShapes[2]:
            shape2add = Sphere(shapeName, float(shapeProperties[0]), float(
                shapeProperties[0]), float(shapeProperties[0]))
        # Cone
        elif shape == threeDimensionalShapes[3]:
            shape2add = Cone(shapeName, float(
                shapeProperties[0]), float(shapeProperties[1]))
        # Cylinder
        elif shape == threeDimensionalShapes[4]:
            shape2add = Cylinder(shapeName, float(
                shapeProperties[0]), float(shapeProperties[1]))
        # Prism
        elif shape == threeDimensionalShapes[5]:
            shape2add = Prism(shapeName, int(shapeProperties[0]), float(
                shapeProperties[1]), float(shapeProperties[2]))
        # Pyramid
        elif shape == threeDimensionalShapes[6]:
            shape2add = Pyramid(shapeName, int(shapeProperties[0]), float(
                shapeProperties[1]), float(shapeProperties[2]))
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
