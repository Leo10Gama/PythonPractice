import requests
from bs4 import BeautifulSoup
import re

DEFAULT_LINK = "https://minecraft.gamepedia.com/"
commandList = ["help", "back", "brewing"]


def minecraft_mode():
    want2exit = False
    while not want2exit:
        command = input(
            "\nPlease enter a Minecraft command (or 'help' to see all): ").lower()
        # List all commands
        if command == commandList[0]:
            print("\n")
            for item in commandList:
                print(item)
            else:
                print("\n")
        # Back command
        elif command == commandList[1]:
            want2exit = True
            print("Exiting Minecraft mode...\n")
        # Brewing command
        elif command == commandList[2]:
            page = requests.get(DEFAULT_LINK + "Brewing")
            content = BeautifulSoup(page.content, 'html.parser')
            potions = {}
            # Get content from base potions
            base_table_rows = content.find(
                "table", attrs={"data-description": "Base potions"}).find_all("tr")
            for i in range(1, len(base_table_rows)):
                add_potion_to_dict(potions, base_table_rows[i])
            # Get content from positive effect potions
            pos_table_rows = content.find(
                "table", attrs={"data-description": "Positive effect potions"}).find_all("tr")
            for i in range(1, len(pos_table_rows)):
                add_potion_to_dict(potions, pos_table_rows[i])
            # Get content from negative effect potions
            neg_table_rows = content.find(
                "table", attrs={"data-description": "Negative effect potions"}).find_all("tr")
            for i in range(1, len(neg_table_rows)):
                add_potion_to_dict(potions, neg_table_rows[i])
            # Get content from mixed effect potions
            mix_table_rows = content.find(
                "table", attrs={"data-description": "Mixed effect potions"}).find_all("tr")
            for i in range(1, len(mix_table_rows)):
                add_potion_to_dict(potions, mix_table_rows[i])
            # Display available potions to read up on
            print("\n")
            for item in potions.keys():
                print(item)
            potion = input("\nWhich potion would you like to know how to brew? ")
            if potion in potions.keys():
                print("\nName: " + potions[potion]["name"] + "Brewing ingredient: " + potions[potion]["ingredient"].title() + "\nBase potion(s): " + " or ".join(potions[potion]["reagents"]))


def add_potion_to_dict(dict, table_row):
    potion=table_row.find("th").text
    short_potion = re.sub(r"\(\s*[0-9]*:[0-9]*\)", "", re.sub("(potion of )|( potion)", "", potion.lower())).replace("\n","")
    ingredient=table_row.find(
        "span", class_="mcui-input").find("span", class_="sprite inv-sprite")["title"].lower()
    temp_reagents=table_row.find(
        "span", class_="mcui-output").find_all("span", class_="invslot-item")
    reagents=[]
    for item in temp_reagents:
        reagents.append(item.find("a")["title"])
    dict[short_potion]={
        "name": potion, "ingredient": ingredient, "reagents": reagents}