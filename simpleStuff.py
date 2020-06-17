import random
import math
import geometry
import convert
import piglatin
import coin_search as coins
import minecraft as mc

commandList = ["help", "exit", "math", "dice", "palindrome", "geometry", "convert", "piglatin", "coin", "minecraft"]
geometryList = ["back"]
want2exit = False

# Here is the main function
while not want2exit:
    command = input("Please enter a command (or type 'help'): ").lower()
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
            geometry.geometryMode()
        # Convert command
        elif command == commandList[6]:
            convert.do_a_conversion()
        # Pig Latin command
        elif command == commandList[7]:
            print(piglatin.to_piglatin(input("Enter a phrase: ").lower()))
        # Coin command
        elif command == commandList[8]:
            coins.browse_catalogue()
        # Minecraft command
        elif command == commandList[9]:
            print("Entering Minecraft mode...")
            mc.minecraft_mode()
        # TODO: Add more commands here
        # This line should technically never run but just in case it's here
        else:
            print("Something happened that shouldn't have happened...?")
    else:
        print("Command not found")
    print("\n")
