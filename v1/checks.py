import sys
import json
from pprint import pprint
 def check(data, keys, file):
     checks = dict()
     for z in range(len(data)):
        for item in keys:
            if item not in data[z]:
                checks[item] = z + 1
     if len(checks) is 0:
        return True
    else:
        print("Please, review the {} file:".format(file))
        for key, value in checks.items():
            print("\tThere is no {0} in item {1}".format(key, str(value)))
        return False

