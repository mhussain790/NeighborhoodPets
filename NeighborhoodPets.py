"""
Author: Masud Hussain
Course: CS162
Assignment: 5D
"""
import json


class NeighborhoodPets():
    def __init__(self):
        self._pet_owner = None
        self._pet_species = None
        self._pet_name = None
        self._pet_list = {}

    # add pet
    def add_pet(self, a_pet_name, a_pet_species, a_pet_owner):

        # creates a count variable that adds 1 to the length of the pet list and used when adding new keys to pet list
        count = len(self._pet_list) + 1

        for key, value in list(self._pet_list.items()):
            if a_pet_name == value["name"]:
                return "Pet already added"

        self._pet_list['pet ' + str(count)] = {'name': a_pet_name, 'species': a_pet_species, 'owner': a_pet_owner}

        # print(self._pet_list)

    # delete pet
    def delete_pet(self, a_pet_name):
        for key, value in list(self._pet_list.items()):
            if a_pet_name == value["name"]:
                self._pet_list.pop(key)
                # print(a_pet_name + " removed")
        return self._pet_list

    # search for pet owner
    def get_owner(self, a_pet_name):
        for key, value in self._pet_list.items():
            if a_pet_name == value["name"]:
                # print(value["owner"])
                return value["owner"]

    def save_as_json(self, file_name):
        with open(file_name, 'w') as outfile:
            json.dump(self._pet_list, outfile)

    def read_json(self, file_name):
        with open(file_name, "r") as infile:
            self._pet_list = json.load(infile)
        # print(self._pet_list)

    # get a set of all pet species
    def get_all_species(self):
        owner_set = set()
        for key, value in self._pet_list.items():
            owner_set.add(value["species"])
        return owner_set
