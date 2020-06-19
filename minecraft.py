import requests
from bs4 import BeautifulSoup
import re

DEFAULT_LINK = "https://minecraft.gamepedia.com"
commandList = ["help", "back", "brewing", "mob"]


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
            page = requests.get(DEFAULT_LINK + "/Brewing")
            content = BeautifulSoup(page.content, 'html.parser')
            potions = {}
            # Get content from base potions
            potion_types = ["Base potions", "Positive effect potions", "Negative effect potions", "Mixed effect potions"]
            for potion_type in potion_types:
                table_rows = content.find("table", attrs={"data-description": potion_type}).find_all("tr")
                for i in range(1, len(table_rows)):
                    add_potion_to_dict(potions, table_rows[i])
            # Display available potions to read up on
            print("\n")
            for item in potions.keys():
                print(item)
            potion = input(
                "\nWhich potion would you like to know how to brew? ")
            # Get potion info
            if potion in potions.keys():
                print("\nName: " + potions[potion]["name"] + "Brewing ingredient: " + potions[potion]
                      ["ingredient"].title() + "\nBase potion(s): " + " or ".join(potions[potion]["reagents"]))
            else:
                print("\nPotion not found")
        # Mob command
        elif command == commandList[3]:
            page = requests.get(DEFAULT_LINK + "/Mob")
            content = BeautifulSoup(page.content, 'html.parser')
            mobs = {}
            # Retrieve passive mobs
            mob_types = ["Passive mobs", "Neutral mobs", "Hostile mobs", "Boss mobs"]
            for mob_type in mob_types:
                for base_item in content.find_all("table", attrs={"data-description": mob_type}):
                    for item in base_item.find_all("tr")[1].find_all("td"):
                        anchor_tag = item.find("a")
                        mobs[anchor_tag.text.lower()] = anchor_tag["href"]
            # Display available mobs to view
            print("\n")
            for item in mobs.keys(): print(item)
            mob = input("\nWhich mob would you like to see? ").lower()
            if mob in mobs:
                mob_info = BeautifulSoup(requests.get(DEFAULT_LINK + mobs[mob]).content, 'html.parser').find("table", class_="infobox-rows").find_all("tr")
                print("\n" + mob.title())
                for row in mob_info:
                    print(row.find("th").text.replace("\n","") + ": ")
                    for paragraph in row.find("td").find_all("p"):
                        print("\t" + paragraph.text.replace("\n",""))
            else:
                print("\nNo mob by that name found")



def add_potion_to_dict(dict, table_row):
    potion = table_row.find("th").text
    short_potion = re.sub(r"\(\s*[0-9]*:[0-9]*\)", "", re.sub(
        "(potion of )|( potion)", "", potion.lower())).replace("\n", "")
    ingredient = table_row.find(
        "span", class_="mcui-input").find("span", class_="sprite inv-sprite")["title"].lower()
    temp_reagents = table_row.find(
        "span", class_="mcui-output").find_all("span", class_="invslot-item")
    reagents = []
    for item in temp_reagents:
        reagents.append(item.find("a")["title"])
    dict[short_potion] = {
        "name": potion, "ingredient": ingredient, "reagents": reagents}
