import sys
import json
from pprint import pprint
 def test(users_dump, venues_dump):
     global places_to_avoid
    places_to_avoid = {}
     for z in range(len(users_dump)):
        if len(users_dump[z]['wont_eat']) is not 0:
            to_avoid_food(users_dump[z], venues_dump)
        if len(users_dump[z]['drinks']) is not 0:
            to_avoid_drinks(users_dump[z], venues_dump)
     places_to_go = to_go(venues_dump)
    outputs(places_to_go)
 def to_avoid_food(user, venues_dump):
     for venues_item in venues_dump:
        for item in range(len(user['wont_eat'])):
            if sorted(user['wont_eat']) == sorted(venues_item['food']):
                value = ("There is nothing for {} to eat".format(user['name']))
                places_to_avoid.setdefault(venues_item['name'], []).append(value)
 def to_avoid_drinks(user, venues_dump):
     user_drinks = [item.capitalize() for item in user['drinks']]
    user_drinks_set = set(user_drinks)
    #print("USER DRINKS: {}".format(user_drinks_set))
     for venues_item in venues_dump:
        venues_item_drinks = [item.capitalize() for item in venues_item['drinks']]
        venus_item_set = set(venues_item_drinks)
        #print("VENUS DRINKS: {}".format(venus_item_set))
         if not (user_drinks_set & venus_item_set):
            #print("There is nothing for {0} to drink in {1}".format(user['name'], venues_item['name']))
            value = ("There is nothing for {} to drink".format(user['name']))
            key = venues_item['name']
            places_to_avoid.setdefault(venues_item['name'], []).append(value)
 def to_go(venues_dump):
     places_to_go = []
     for z in range(len(venues_dump)):
        places_to_go.append(venues_dump[z]['name'])
     for key in places_to_avoid:
        places_to_go.remove(key)
     return places_to_go
 def outputs(places_to_go):
     print("Places to go:")
     for item in places_to_go:
        print("\n\t- {}".format(item))
     print("\nPlaces to avoid:")
     for key, value in places_to_avoid.items():
        print("\n\t - {}".format(key))
        for item in value:
            print("\t\t\t - {}".format(item))

