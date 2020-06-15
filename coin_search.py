import requests
from bs4 import BeautifulSoup
import re

DEFAULT_URL = "http://en.numista.com/catalogue/index.php?mode=simplifie"
country_dictionary = {
    "canada": "canada_section",
    "united states": "united-states",
    "us": "united-states",
    "usa": "united-states"

}


def map_country(country):
    for item in country_dictionary.keys():
        if country == item:
            return country_dictionary[country]


def browse_catalogue():
    country = input("Enter country: ").lower()
    search = input("Search: ")
    search = "+".join(search.lower().split())
    browsing = True
    try:
        page = requests.get(DEFAULT_URL + "&l=" +
                        map_country(country) + "&r=" + search)
        while browsing:
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id="resultats_recherche")
            coins = results.find_all('div', class_='resultat_recherche')
            i = 0
            print('\n')
            next_exists = bool(re.search("Next", results.find('div', class_='catalogue_navigation').text))
            prev_exists = bool(re.search("Previous", results.find('div', class_='catalogue_navigation').text))
            for coin in coins:
                print("<" + str(i) + "> " + ' '.join(coin.find('strong').text.split()))
                i += 1
            if prev_exists:
                print("<p> Previous page")
            if next_exists:
                print("<n> Next page")
            num = input("\nWhich coin would you like to see? (Enter the number): ")
            if num == "p" and prev_exists:
                prev_link = results.find('div', class_='catalogue_navigation').find('a', rel='prev')['href']
                page = requests.get('http://en.numista.com/catalogue/' + prev_link)
            elif num == "n" and next_exists:
                next_link = results.find('div', class_='catalogue_navigation').find('a', rel='next')['href']
                print(next_link)
                page = requests.get('http://en.numista.com/catalogue/' + next_link)
            else:
                num = int(num)
                if num < len(coins):
                    browsing = False
                else:
                    print("Index out of bounds")
                    return
        else:
            try:
                link_extension = coins[num].find('a')['href']
                coin_page = requests.get(
                    'http://en.numista.com' + link_extension)
                soup = BeautifulSoup(coin_page.content, 'html.parser')
                coin_attributes = soup.find('table').find_all('tr')
                print('\n')
                for item in coin_attributes:
                    if item.find('th').text != "References":
                        print(item.find('th').text + ": " +
                              ' '.join(item.find('td').text.split()))
            except:
                print("Something went wrong :(")
    except:
        print("Something went wrong :(")
