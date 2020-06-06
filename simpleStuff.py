import random

commandList = ["help", "exit", "math", "dice", "palindrome", "geometry"]
geometryList = ["back"]
want2exit = False

# The following function is called for geometry functionality
def geometryMode():
    want2exit = False
    geometryCommands = ["back", "list", "create"]
    twoDimensionalShapes = ["trapezoid"]
    myShapes = {}
    BAD_INPUT = "Improper input. Returning to geometry menu...\n"

    # Define some classes for shapes
    class Trapezoid:
        def __init__(self, name, top=0, bottom=0, leg1=0, leg2=0, h=0):
            self.shape = "Trapezoid"
            self.name = name
            self.a, self.b = min(top, bottom), max(top, bottom)
            self.c = leg1
            self.d = leg2
            self.h = h

        def __str__(self):
            return "Dimensions of " + self.shape + " " + self.name + ":\nBase a = " + str(self.a) + "\nBase b = " + str(self.b) + "\nSide c = " + str(self.c) + "\nSide d = " + str(self.d) + "\nHeight = " + str(self.height)

        def get_area(self):
            return (self.a + self.b) / 2 * self.h

        def get_perimeter(self):
            return self.a + self.b + self.c + self.d
    #
    #   TODO: Add more shapes (quadrilaterals for now), including isosceles trapezoid, parallelogram, rhombus, kite, rectangle, square
    #

    while not want2exit:
        command = input("Enter a geometry command (see all with 'list', or type 'back'): ")
        print("\n")
        # Back to regular commands
        if command == geometryCommands[0]:
            secondCommand = input("Are you sure you want to go back? You'll lose any shapes you've made here (yes/no): ")
            if secondCommand in ["yes", "YES", "Yes", "Y", "y"]:
                print("Returning to main commands...")
                want2exit = True
            else:
                print("Cancelled")
        # List all commands
        if command == geometryCommands[1]:
            print("Here is a list of all geometry commands:")
            for keyword in geometryCommands:
                print(keyword)
        # Create shape command
        if command == geometryCommands[2]:
            shape = input("What type of shape would you like to create? ")
            # Make a trapezoid
            if shape == twoDimensionalShapes[0]:
                shapeName = input("Enter a name for your Trapezoid: ")
                shapeProperties = [input("Enter side a: "), input("Enter side b: "), input("Enter side c: "), input("Enter side d: "), input("Enter height: ")]
                if all(value.replace(",","").replace(".","").isnumeric() for value in shapeProperties):
                    myShapes[shapeName] = Trapezoid(shapeName, shapeProperties[0], shapeProperties[1], shapeProperties[2], shapeProperties[3], shapeProperties[4])
                    print(myShapes[shapeName])
                else:
                    print(BAD_INPUT)
            # No proper shape entered
            else:
                print(BAD_INPUT)
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

