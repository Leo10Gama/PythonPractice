import requests
from bs4 import BeautifulSoup
import re

DEFAULT_LINK = "https://minecraft.gamepedia.com"
commandList = ["help", "back", "brewing", "mob", "block"]
potions = {}
mobs = {}
blocks = {}

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
            if potions == {}:
                page = requests.get(DEFAULT_LINK + "/Brewing")
                content = BeautifulSoup(page.content, 'html.parser')
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
            if mobs == {}:
                page = requests.get(DEFAULT_LINK + "/Mob")
                content = BeautifulSoup(page.content, 'html.parser')
                # Retrieve the mobs
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
                print("\n\n" + mob.upper() + "\n")
                for row in mob_info:
                    print(row.find("th").text.replace("\n","") + ": ")
                    for paragraph in row.find("td").find_all("p"):
                        for span in paragraph.find_all("span"):
                            span.replace_with("")
                        for br in paragraph.find_all("br"):
                            br.replace_with("\n")
                        print("\t" + re.sub(r"\n+", "\n", paragraph.text).replace("\n","\n\t"))
            else:
                print("\nNo mob by that name found")
        # Block command
        elif command == commandList[4]:
            # Fill array with links if need be
            if blocks == {}:
                blocks_array = BeautifulSoup(requests.get(DEFAULT_LINK + "/Block").content, 'html.parser').find("div", class_="collapsible-content").find_all("li")
                for block in blocks_array:
                    blocks[block.text.lower().strip()] = block.find_all("a")[len(block.find_all("a")) - 1]["href"]
            block = input("What block would you like to see? ")
            if block in blocks:
                block_page = BeautifulSoup(requests.get(DEFAULT_LINK + blocks[block]).content, 'html.parser')
                block_table_info = block_page.find("table", class_="infobox-rows").find_all("tr")
                # Display the block
                print("\n\n" + "~" * 20 + "\n" + block_page.find("div", class_="mcwiki-header infobox-title").text.upper().strip() + "\n" + "~" * 20 + "\n")
                # Display info from infobox
                for row in block_table_info:
                    print(row.find("th").text.replace("\n","") + ": ")
                    for paragraph in row.find("td").find_all("p"):
                        for span in paragraph.find_all("span"):
                            try:
                                if span["class"] is ["sprite", "inv-sprite"] or ["sprite", "slot-sprite"]: pass
                                else: span.replace_with("")
                            except:
                                span.replace_with("")
                        for br in paragraph.find_all("br"):
                            br.replace_with("_")
                        if paragraph.find("span", class_="sprite slot-sprite") is not None: 
                            print("\t" + paragraph.find("a")["title"])
                        if paragraph.find("span", class_="sprite inv-sprite") is not None: 
                            print("\t" + paragraph.find("span", class_="sprite inv-sprite").parent["title"])
                        else: 
                            print("\t" + re.sub(r"\n+", "", paragraph.text).replace("_","\n\t"))
                # Display info from crafting/smelting (if possible)
                try:
                    for tag in block_page.find("span", id="Obtaining").parent.next_siblings:
                        if tag.name == "table":
                            # Crafting recipes exist
                            if tag.has_attr("data-description"): 
                                if tag["data-description"] == "Crafting recipes":
                                    craft_rows = tag.find_all("tr")
                                    print("Crafting:")
                                    for recipe in craft_rows:
                                        if bool(recipe.find_all("td")):
                                            print("\t_______\n\t|1|2|3|\n\t-------\n\t|4|5|6| -> 10\n\t-------\n\t|7|8|9|\n\t-------")
                                            counter = 1
                                            output = {}
                                            recipe_input = recipe.find("span", class_="mcui-input")
                                            # Get table input
                                            for row in recipe_input.children:
                                                for invslot in row.children:
                                                    if "animated" in invslot["class"]:
                                                        return_val = []
                                                        for item in invslot.children:
                                                            return_val.append(item.find("a")["title"])
                                                        output[counter] = " / ".join(return_val)
                                                    elif bool(invslot.find("a")):
                                                        output[counter] = invslot.find("a")["title"]
                                                    else:
                                                        if bool(list(invslot.children)):
                                                            output[counter] = invslot.find("span", class_="sprite inv-sprite")["title"]
                                                    counter += 1
                                            recipe_output = recipe.find("span", class_="mcui-output")
                                            # Get table output
                                            if "animated" in recipe_output.find("span")["class"]:
                                                return_val = []
                                                return_val.append(recipe_output.find("span", class_="invslot-item animated-active").find("a")["title"])
                                                for item in recipe_output.find("span", class_="invslot-item animated-active").next_siblings:
                                                    return_val.append(item.find("a")["title"])
                                                if bool(recipe_output.find("span", class_="invslot-stacksize")):
                                                    output[10] = " / ".join(return_val) + " x " + recipe_output.find("span", class_="invslot-stacksize").text
                                                else:
                                                    output[10] = " / ".join(return_val)
                                            else:
                                                if bool(recipe_output.find("span", class_="invslot-stacksize")):
                                                    output[10] = recipe_output.find("span", class_="sprite inv-sprite")["title"] + " x " + recipe_output.find("span", class_="invslot-stacksize").text
                                                else:
                                                    output[10] = recipe_output.find("span", class_="sprite inv-sprite")["title"]
                                            for key in output.keys():
                                                print("\t" + str(key) + " - " + output[key])
                            # Smelting recipes exist
                            elif bool(tag.find("table", attrs={"data-description": "Smelting recipes"})):
                                # TODO: Get smelting recipes if possible
                                pass
                            # Not the right div
                            else:
                                continue
                        elif tag.name == "h2":
                            break
                except:
                    print("fucked up somehow")
            else:
                print("\nNo block by that name found")
        # Command not found
        else:
            print("Command not found. Type 'help' to see all available commands")



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
