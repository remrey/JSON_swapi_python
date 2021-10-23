import json
import requests

class Character:
    def __init__(self, dictt):
        self.name = dictt['name']
        self.height = dictt['height']
        self.mass = dictt['mass']
        self.hair_color = dictt['hair_color']
        self.skin_color = dictt['skin_color']
        self.eye_color = dictt['eye_color']
        self.birth_year = dictt['birth_year']
        self.gender = dictt['gender']
        self.homeworld = self.check_home(dictt['homeworld'])
        self.films = self.check_films(dictt['films'])
        self.attributes = list(dictt.keys())[0:10]

    def check_home(self, url):
        obj = requests.get(url).json()
        return obj['name']

    def check_films(self, film_list):
        temp = []
        for url in film_list:
            obj = requests.get(url).json()
            temp.append(obj['title'])

        return temp;


    def jsonEncoder(self):
        temp = {}
        for attribute in self.attributes:
            val = getattr(self, attribute)
            if attribute != "attributes":
                temp[attribute] = val


        return temp

    def fprint(self):
        for attribute in self.attributes:
            temp = getattr(self, attribute)
            if attribute != "name":
                print('\t', end = '')
            if attribute == "films":
                print(f"{attribute.upper()} is: ", end= '')
                print(*temp, sep = ", ")
            else:
                print(f"{attribute.upper()} is: {temp}")
