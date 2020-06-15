import requests
from bs4 import BeautifulSoup
import re

DEFAULT_URL = "http://en.numista.com/catalogue/index.php?mode=simplifie"
country_dictionary = {
    "canada": "canada_section",
    "united states": "united-states",
    "us": "united-states",
    "usa": "united-states",
    "algeria": "algerie",
    "armenia": "armenie",
    "australia": "australia_section",
    "the bahamas": "bahamas",
    "bahrain": "bahrein",
    "barbados": "barbade",
    "belarus": "bielorussie",
    "belize": "belize_section",
    "bermuda": "bermudes",
    "bolivia": "bolivie",
    "bosnia and herzegovina": "bosnia_herzegovina_section",
    "bosnia & herzegovina": "bosnia_herzegovina_section",
    "brazil": "brazil_section",
    "bulgaria": "bulgaria_section",
    "cameroon": "cameroon_section",
    "cayman islands": "iles_caimanes",
    "cayman isles": "iles_caimanes",
    "chile": "chili",
    "colombia": "colombie",
    "cook islands": "iles_cook",
    "cook isles": "iles_cook",
    "costa rica": "costa_rica",
    "cyprus": "chypre",
    "czech republic": "czech",
    "czechoslovakia": "tchecoslovaquie",
    "ecuador": "equateur",
    "egypt": "egypte",
    "estonia": "estonia_section",
    "fiji": "fidji",
    "finland": "finlande",
    "france": "france_section",
    "georgia": "georgia_section",
    "ghana": "ghana_section",
    "iceland": "islande",
    "iraq": "irak",
    "ireland": "irlande",
    "isle of man": "ile_de_man",
    "israel": "israel_section",
    "jamaica": "jamaique",
    "japan": "japon",
    "malta": "malte",
    "new zealand": "nouvelle_zelande",
    "nigeria": "nigeria_section",
    "north korea": "coree_du_nord",
    "north macedonia": "macedoine",
    "oman": "oman_section",
    "papua new guinea": "papua-new-guinea",
    "peru": "perou",
    "poland": "poland_section",
    "portugal": "portugal_section",
    "romania": "roumanie",
    "san marino": "saint-marin",
    "saudi arabia": "saudi-arabia",
    "serbia": "serbia_section",
    "slovakia": "slovaquie",
    "slovenia": "slovenie",
    "south africa": "south-africa",
    "south korea": "coree_du_sud",
    "sri lanka": "sri-lanka",
    "sweden": "sweden_section",
    "syria": "syrie",
    "thailand": "thailande",
    "trinidad and tobago": "trinite-et-tobago_section",
    "turkey": "turquie",
    "united arab emirates": "uae",
    "united kingdom": "united-kingdom",
    "uk": "united-kingdom",
    "vatican city": "vatican",
    "venezuela": "venezuela_section",
    "vietnam": "viet-nam",
    "yemen": "yemen_section",
    "yugoslavia": "yougoslavie",
    "zimbabwe": "zimbabwe_section",
}


def map_country(country):
    for item in country_dictionary.keys():
        if country == item:
            return country_dictionary[country]
    else:
        return False


def browse_catalogue():
    country = input("Enter country: ").lower()
    search = input("Search: ")
    search = "+".join(search.lower().split())
    search_country = map_country(country)
    if not search_country: search_country = country
    browsing = True
    try:
        page = requests.get(DEFAULT_URL + "&l=" +
                            search_country + "&r=" + search)
        # This section displays the search list of coins
        while browsing:
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id="resultats_recherche")
            coins = results.find_all('div', class_='resultat_recherche')
            i = 0
            print('\n')
            next_exists = bool(re.search("Next", results.find(
                'div', class_='catalogue_navigation').text))
            prev_exists = bool(re.search("Previous", results.find(
                'div', class_='catalogue_navigation').text))
            for coin in coins:
                print("<" + str(i) + "> " +
                      ' '.join(coin.find('strong').text.split()))
                i += 1
            if prev_exists:
                print("<p> Previous page")
            if next_exists:
                print("<n> Next page")
            num = input(
                "\nWhich coin would you like to see? (Enter the number): ")
            if num == "p" and prev_exists:
                prev_link = results.find('div', class_='catalogue_navigation').find(
                    'a', rel='prev')['href']
                page = requests.get(
                    'http://en.numista.com/catalogue/' + prev_link)
            elif num == "n" and next_exists:
                next_link = results.find('div', class_='catalogue_navigation').find(
                    'a', rel='next')['href']
                page = requests.get(
                    'http://en.numista.com/catalogue/' + next_link)
            else:
                num = int(num)
                if num < len(coins):
                    browsing = False
                else:
                    print("Index out of bounds")
                    return
        else:
            # This section is to display the actual information about the coins
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
