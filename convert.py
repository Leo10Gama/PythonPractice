types = ["temperature", "length", "weight"]
temperature = ["celsius", "fahrenheit"]
length = ["metres", "inches", "feet", "yards", "miles"]
weight = ["grams", "ounces", "pounds", "tonnes"]
BAD_INPUT = "Invalid entry"
SAME_TYPE = "The units you entered are the same, so there is no conversion"

def do_a_conversion():
    for s in types: print(s)
    convertType = input("\nWhich type would you like to convert? ").lower()
    # Convert temperature
    if convertType == types[0]:
        print("\n")
        for s in temperature: print(s)
        print("\n[type1] [type2] [value (of type1)]\n")
        type1 = input("Enter type1: ").lower()
        type2 = input("Enter type2: ").lower()
        value = input("Enter numeric value: ")
        try: print(temperature_conversion(type1, type2, float(value)))
        except: print(BAD_INPUT)
    # Convert length
    elif convertType == types[1]:
        print("\n")
        for s in length: print(s)
        print("\n[type1] [type2] [value (of type1)]\n")
        type1 = input("Enter type1: ").lower()
        type2 = input("Enter type2: ").lower()
        value = input("Enter numeric value: ")
        try: print(length_conversion(type1, type2, float(value)))
        except: print(BAD_INPUT)
    # Convert weight
    elif convertType == types[2]:
        print("\n")
        for s in weight: print(s)
        print("\n[type1] [type2] [value (of type1)]\n")
        type1 = input("Enter type1: ").lower()
        type2 = input("Enter type2: ").lower()
        value = input("Enter numeric value: ")
        try: print(weight_conversion(type1, type2, float(value)))
        except: print(BAD_INPUT)
    # Something else
    else:
        print("\n" + BAD_INPUT)
    
def temperature_conversion(type1, type2, value):
    # Celsius to Fahrenheit
    if type1 == temperature[0] and type2 == temperature[1]:
        return str(value) + "\u00B0C = " + str((value * 9 / 5) + 32) + "\u00B0F"
    # Fahrenheit to Celsius
    elif type1 == temperature[1] and type2 == temperature[0]:
        return str(value) + "\u00B0C = " + str((value - 32) * 5 / 9) + "\u00B0C"
    # Same type
    elif type1 == type2:
        return SAME_TYPE
    # Something went wrong
    else:
        return BAD_INPUT

def length_conversion(type1, type2, value):
    # Metres to inches
    if type1 == length[0] and type2 == length[1]:
        return str(value) + "m = " + str(value * 39.37) + "in"
    # Inches to metres
    elif type1 == length[1] and type2 == length[0]:
        return str(value) + "in = " + str(value / 39.37) + "m"
    # Metres to feet
    elif type1 == length[0] and type2 == length[2]:
        return str(value) + "m = " + str(value * 3.28084) + "ft"
    # Feet to metres
    elif type1 == length[2] and type2 == length[0]:
        return str(value) + "ft = " + str(value / 3.28084) + "m"
    # Metres to yards
    elif type1 == length[0] and type2 == length[3]:
        return str(value) + "m = " + str(value * 1.09361) + "yd"
    # Yards to metres
    elif type1 == length[3] and type2 == length[0]:
        return str(value) + "yd = " + str(value * 1.09361) + "m"
    # Metres to miles
    elif type1 == length[0] and type2 == length[4]:
        return str(value) + "m = " + str(value / 1609) + " miles"
    # Miles to metres
    elif type1 == length[4] and type2 == length[0]:
        return str(value) + " miles = " + str(value * 1609) + "m"
    # Inches to feet
    elif type1 == length[1] and type2 == length[2]:
        return str(value) + "in = " + str(value / 12) + "ft"
    # Feet to inches
    elif type1 == length[2] and type2 == length[1]:
        return str(value) + "ft = " + str(value * 12) + "in"
    # Inches to yards
    elif type1 == length[1] and type2 == length[3]:
        return str(value) + "in = " + str(value / 36) + "yd"
    # Yards to inches
    elif type1 == length[3] and type2 == length[1]:
        return str(value) + "yd = " + str(value * 36) + "in"
    # Inches to miles
    elif type1 == length[1] and type2 == length[4]:
        return str(value) + "in = " + str(value / 63360) + " miles"
    # Miles to inches
    elif type1 == length[4] and type2 == length[1]:
        return str(value) + " miles = " + str(value * 63360) + "in"
    # Feet to yards
    elif type1 == length[2] and type2 == length[3]:
        return str(value) + "ft = " + str(value / 3) + "yd"
    # Yards to feet
    elif type1 == length[3] and type2 == length[2]:
        return str(value) + "yd = " + str(value * 3) + "ft"
    # Feet to miles
    elif type1 == length[2] and type2 == length[4]:
        return str(value) + "ft = " + str(value / 5280) + " miles"
    # Miles to feet
    elif type1 == length[4] and type2 == length[2]:
        return str(value) + " miles = " + str(value * 5280) + "ft"
    # Yards to miles
    elif type1 == length[3] and type2 == length[4]:
        return str(value) + "yd = " + str(value / 1760) + " miles"
    # Miles to yards
    elif type1 == length[4] and type2 == length[3]:
        return str(value) + " miles = " + str(value * 1760) + "yd"
    # Same type
    elif type1 == type2:
        return SAME_TYPE
    # Error
    else:
        return BAD_INPUT

def weight_conversion(type1, type2, value):
    # Grams to ounces
    if type1 == weight[0] and type2 == weight[1]:
        return str(value) + "g = " + str(value / 28.35) + "oz"
    # Ounces to grams
    elif type1 == weight[1] and type2 == weight[0]:
        return str(value) + "oz = " + str(value * 28.35) + "g"
    # Grams to pounds
    elif type1 == weight[0] and type2 == weight[2]:
        return str(value) + "g = " + str(value / 454) + "lbs"
    # Pounds to grams
    elif type1 == weight[2] and type2 == weight[0]:
        return str(value) + "lbs = " + str(value * 454) + "g"
    # Grams to tonnes
    elif type1 == weight[0] and type2 == weight[3]:
        return str(value) + "g = " + str(value / 1000000) + "t"
    # Tonnes to grams
    elif type1 == weight[3] and type2 == weight[0]:
        return str(value) + "t = " + str(value * 1000000) + "g"
    # Ounces to pounds
    elif type1 == weight[1] and type2 == weight[2]:
        return str(value) + "oz = " + str(value / 16) + "lbs"
    # Pounds to ounces
    elif type1 == weight[2] and type2 == weight[1]:
        return str(value) + "lbs = " + str(value * 16) + "oz"
    # Ounces to tonnes
    elif type1 == weight[1] and type2 == weight[3]:
        return str(value) + "oz = " + str(value / 35274) + "t"
    # Tonnes to ounces
    elif type1 == weight[3] and type2 == weight[1]:
        return str(value) + "t = " + str(value * 35274) + "oz"
    # Pounds to tonnes
    elif type1 == weight[2] and type2 == weight[3]:
        return str(value) + "lbs = " + str(value / 2205) + "t"
    # Tonnes to pounds
    elif type1 == weight[3] and type2 == weight[2]:
        return str(value) + "t = " + str(value * 2205) + "lbs"
    # Same type
    elif type1 == type2:
        return SAME_TYPE
    # Error
    else:
        return BAD_INPUT