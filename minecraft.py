import requests
from bs4 import BeautifulSoup
import re

DEFAULT_LINK = "https://minecraft.gamepedia.com"
commandList = ["help", "back", "brewing", "mob", "block", "item"]
potions = {}
mobs = {}
blocks = {}


def minecraft_mode():
    want2exit = False
    while not want2exit:
        command = input(
            "\nPlease enter a Minecraft command (or 'help' to see all): ").lower().strip()
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
                potion_types = ["Base potions", "Positive effect potions",
                                "Negative effect potions", "Mixed effect potions"]
                for potion_type in potion_types:
                    table_rows = content.find(
                        "table", attrs={"data-description": potion_type}).find_all("tr")
                    for i in range(1, len(table_rows)):
                        add_potion_to_dict(potions, table_rows[i])
            # Display available potions to read up on
            print("\n")
            for item in potions.keys():
                print(item)
            potion = input(
                "\nWhich potion would you like to know how to brew? ").strip()
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
                mob_types = ["Passive mobs", "Neutral mobs",
                             "Hostile mobs", "Boss mobs"]
                for mob_type in mob_types:
                    for base_item in content.find_all("table", attrs={"data-description": mob_type}):
                        for item in base_item.find_all("tr")[1].find_all("td"):
                            anchor_tag = item.find("a")
                            mobs[anchor_tag.text.lower()] = anchor_tag["href"]
            # Display available mobs to view
            print("\n")
            for item in mobs.keys():
                print(item)
            mob = input("\nWhich mob would you like to see? ").lower().strip()
            if mob in mobs:
                mob_info = BeautifulSoup(requests.get(
                    DEFAULT_LINK + mobs[mob]).content, 'html.parser').find("table", class_="infobox-rows").find_all("tr")
                print("\n\n" + mob.upper() + "\n")
                for row in mob_info:
                    print(row.find("th").text.replace("\n", "") + ": ")
                    for paragraph in row.find("td").find_all("p"):
                        for span in paragraph.find_all("span"):
                            span.replace_with("")
                        for br in paragraph.find_all("br"):
                            br.replace_with("\n")
                        print("\t" + re.sub(r"\n+", "\n",
                                            paragraph.text).replace("\n", "\n\t"))
            else:
                print("\nNo mob by that name found")
        # Block / Item command
        elif command == commandList[4] or command == commandList[5]:
            # Fill array with links if need be
            if blocks == {}:
                blocks_array = BeautifulSoup(requests.get(
                    DEFAULT_LINK + "/Block").content, 'html.parser').find("div", class_="collapsible-content").find_all("li")
                for block in blocks_array:
                    blocks[block.text.lower().strip()] = block.find_all("a")[
                        len(block.find_all("a")) - 1]["href"]
                items_array_temp = BeautifulSoup(requests.get(DEFAULT_LINK + "/Item").content, 'html.parser').find_all(
                    "div", class_="div-col columns column-width")
                items_array = []
                for thing in items_array_temp:
                    items_array = items_array + thing.find_all("li")
                for item in items_array:
                    blocks[item.text.lower().strip()] = item.find_all("a")[
                        len(item.find_all("a")) - 1]["href"]
            block = input("What block/item would you like to see? ").strip()
            if block in blocks:
                block_page = BeautifulSoup(requests.get(
                    DEFAULT_LINK + blocks[block]).content, 'html.parser')
                block_table_info = block_page.find(
                    "table", class_="infobox-rows").find_all("tr")
                # Display the block
                print("\n\n" + "~" * 20 + "\n" + block_page.find("div",
                                                                 class_="mcwiki-header infobox-title").text.upper().strip() + "\n" + "~" * 20 + "\n")
                # Display info from infobox
                for row in block_table_info:
                    print(row.find("th").text.replace("\n", "") + ": ")
                    for paragraph in row.find("td").find_all("p"):
                        for span in paragraph.find_all("span"):
                            try:
                                if span["class"] is ["sprite", "inv-sprite"] or ["sprite", "slot-sprite"]:
                                    pass
                                else:
                                    span.replace_with("")
                            except:
                                span.replace_with("")
                        for br in paragraph.find_all("br"):
                            br.replace_with("_")
                        if paragraph.find("span", class_="sprite slot-sprite") is not None:
                            print("\t" + paragraph.find("a")["title"])
                        if paragraph.find("span", class_="sprite inv-sprite") is not None:
                            print("\t" + paragraph.find("span",
                                                        class_="sprite inv-sprite").parent["title"])
                        else:
                            print("\t" + re.sub(r"\n+", "",
                                                paragraph.text).replace("_", "\n\t"))
                # Display info from crafting/smelting (if possible)
                try:
                    for tag in block_page.find("span", id="Obtaining").parent.next_siblings:
                        if tag.name == "table":
                            # Crafting recipes exist
                            if tag.has_attr("data-description"):
                                # Crafting recipes exist
                                if tag["data-description"] == "Crafting recipes":
                                    craft_rows = tag.find_all("tr")
                                    print("Crafting:")
                                    for recipe in craft_rows:
                                        print_crafting_recipe(recipe)
                                # Smelting recipes exist
                                elif tag["data-description"] == "Smelting recipes":
                                    smelt_rows = tag.find_all("tr")
                                    print("\nSmelting:")
                                    for recipe in smelt_rows:
                                        print_smelting_recipe(recipe)
                                # Stonecutting recipes exist
                                elif tag['data-description'] == "Cutting recipes":
                                    cut_rows = tag.find_all("tr")
                                    print("\nStonecutting:")
                                    for recipe in cut_rows:
                                        print_stonecutting_recipe(recipe)
                            # Not the right div
                            else:
                                continue
                        elif tag.name == "h2":
                            break
                except:
                    print("Something went wrong :/")
            else:
                print("\nNo block/item by that name found")
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


# Pre: table_row is a <tr> element that contains table data for crafting recipes
# Post: The crafting recipe in the <tr> is printed
def print_crafting_recipe(table_row):
    if bool(table_row.find_all("td")):
        print("\t_______\n\t|1|2|3|\n\t-------\n\t|4|5|6| -> 10\n\t-------\n\t|7|8|9|\n\t-------")
        counter = 1
        output = {}
        recipe_input = table_row.find("span", class_="mcui-input")
        # Get table input
        for row in recipe_input.children:
            for invslot in row.children:
                if "animated" in invslot["class"]:
                    return_val = []
                    for item in invslot.children:
                        if bool(item.find("span", class_="sprite inv-sprite")):
                            return_val.append(
                                item.find("span", class_="sprite inv-sprite")["title"])
                        else:
                            return_val.append(item.find("a")["title"])
                    output[counter] = " / ".join(return_val)
                elif bool(invslot.find("span", class_="sprite inv-sprite")):
                    output[counter] = invslot.find(
                        "span", class_="sprite inv-sprite")["title"] or return_val.append(item.find("a")["title"])
                else:
                    if bool(list(invslot.children)):
                        if bool(invslot.find("span", class_="sprite inv-sprite")):
                            output[counter] = invslot.find(
                                "span", class_="sprite inv-sprite")["title"]
                        else:
                            output[counter] = invslot.find("img")["alt"]
                counter += 1
        recipe_output = table_row.find("span", class_="mcui-output")
        # Get table output
        if "animated" in recipe_output.find("span")["class"]:
            return_val = []
            for item in recipe_output.find("span", class_="invslot animated invslot-large").children:
                if bool(item.find("span", class_="sprite inv-sprite")):
                    return_val.append(
                        item.find("span", class_="sprite inv-sprite")["title"])
                else:
                    return_val.append(item.find("a")["title"])
            if bool(recipe_output.find("span", class_="invslot-stacksize")):
                output[10] = " / ".join(return_val) + " x " + recipe_output.find(
                    "span", class_="invslot-stacksize").text
            else:
                output[10] = " / ".join(return_val)
        else:
            if bool(recipe_output.find("span", class_="invslot-stacksize")):
                if bool(recipe_output.find("span", class_="sprite inv-sprite")):
                    output[10] = recipe_output.find("span", class_="sprite inv-sprite")[
                        "title"] + " x " + recipe_output.find("span", class_="invslot-stacksize").text
                else:
                    output[10] = recipe_output.find("img")[
                        "alt"] + " x " + recipe_output.find("span", class_="invslot-stacksize").text
            else:
                if bool(recipe_output.find("span", class_="sprite inv-sprite")):
                    output[10] = recipe_output.find(
                        "span", class_="sprite inv-sprite")["title"]
                else:
                    output[10] = recipe_output.find("img")["alt"]
        for key in output.keys():
            print("\t" + str(key) + " - " + output[key])


# Pre: table_row is a <tr> element that contains the data necessary to produce a smelting recipe
# Post: The input and output for smelting a block is provided
def print_smelting_recipe(table_row):
    if bool(table_row.find_all("td")):
        output = {}
        recipe_input = list(table_row.find(
            "span", class_="mcui-input").children)[0]
        if "animated" in recipe_input["class"]:
            temp = []
            for item in recipe_input.children:
                temp.append(
                    item.find("span", class_="sprite inv-sprite")["title"])
            output["Input"] = " / ".join(temp)
        else:
            output["Input"] = recipe_input.find(
                "span", class_="sprite inv-sprite")["title"]
        recipe_output = list(table_row.find(
            "span", class_="mcui-output").children)[0]
        if "animated" in recipe_output["class"]:
            temp = []
            for item in recipe_output.children:
                temp.append(
                    item.find("span", class_="sprite inv-sprite")["title"])
            output["Output"] = " / ".join(temp)
        else:
            output["Output"] = recipe_output.find(
                "span", class_="sprite inv-sprite")["title"]
        for key in output.keys():
            print("\t" + key + ": " + output[key])

# Pre: table_row is a <tr> element that contains the data necessary to produce a stonecutting recipe
# Post: The input and output for cutting a block is provided


def print_stonecutting_recipe(table_row):
    if bool(table_row.find_all("td")):
        output = {}
        recipe_input = list(table_row.find(
            "span", class_="mcui-input").children)[0]
        if "animated" in recipe_input["class"]:
            temp = []
            for item in recipe_input.children:
                if bool(item.find("span", class_="sprite inv-sprite")):
                    temp.append(
                        item.find("span", class_="sprite inv-sprite")["title"])
                else:
                    temp.append(item.find("img")["alt"])
            output["Input"] = " / ".join(temp)
        else:
            if bool(recipe_input.find("span", class_="sprite inv-sprite")):
                output["Input"] = recipe_input.find(
                    "span", class_="sprite inv-sprite")["title"]
            else:
                output["Input"] = recipe_input.find("img")["alt"]
        recipe_output = list(table_row.find(
            "span", class_="mcui-output").children)[0]
        if "animated" in recipe_output["class"]:
            temp = []
            for item in recipe_output.children:
                if bool(item.find("span", class_="sprite inv-sprite")):
                    temp.append(
                        item.find("span", class_="sprite inv-sprite")["title"])
                else:
                    temp.append(item.find("img")["alt"])
            output["Output"] = " / ".join(temp)
        else:
            if bool(recipe_output.find("span", class_="sprite inv-sprite")):
                output["Output"] = recipe_output.find(
                    "span", class_="sprite inv-sprite")["title"]
            else:
                output["Output"] = recipe_output.find("img")["alt"]
        for key in output.keys():
            print("\t" + key + ": " + output[key])
        print("\n")
