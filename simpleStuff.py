commandList = ["help", "exit", "math"]
want2exit = False

while not want2exit:
    command = input("Please enter a command (or type 'help'): ")
    if command in commandList:
        if command==commandList[0]:
            print("Here is a list of all commands:")
            for keyword in commandList:
                print(keyword)
        elif command==commandList[1]:
            print("Exiting program...")
            want2exit = True
        elif command==commandList[2]:
            maths = input("Enter an equation in the form [number] [operation] [number]: ").strip().split()
            if len(maths) == 3:
                if maths[1] == "+":
                    print(maths[0] + " " + maths[1] + " " + maths[2] + " = " + str(float(maths[0]) + float(maths[2])))
                elif maths[1] == "-":
                    print(maths[0] + " " + maths[1] + " " + maths[2] + " = " + str(float(maths[0]) - float(maths[2])))
                elif maths[1] == "*":
                    print(maths[0] + " " + maths[1] + " " + maths[2] + " = " + str(float(maths[0]) * float(maths[2])))
                elif maths[1] == "/":
                    print(maths[0] + " " + maths[1] + " " + maths[2] + " = " + str(float(maths[0]) / float(maths[2])))
                elif maths[1] == "%":
                    print(maths[0] + " " + maths[1] + " " + maths[2] + " = " + str(float(maths[0]) % float(maths[2])))
                elif maths[1] == "\\":
                    print(maths[0] + " " + maths[1] + " " + maths[2] + " = " + str(float(maths[0]) // float(maths[2])))
                else:
                    print("Invalid input")
            else:
                print("Invalid operation")
        else:
            print("Something happened that shouldn't have happened...?")
    else:
        print("Command not found")