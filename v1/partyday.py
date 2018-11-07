import sys
import json
from pprint import pprint
import checks
import utils
 def open_json(payload):
     with open(payload) as json_file:
            return json.load(json_file)
 def main():
     try:
        users_info = open_json(sys.argv[1])
        venues_info = open_json(sys.argv[2])
         users_key = ["name", "wont_eat", "drinks"]
        venues_key = ["name", "food", "drinks"]
         users_check = checks.check(users_info, users_key, sys.argv[1])
        venues_check = checks.check(venues_info, venues_key, sys.argv[2])
         if users_check and venues_check:
            utils.test(users_info, venues_info)
        else:
            print("KO")
     except Exception as e:
        print("\nOops! An error occurred {}\n".format(e))
 if __name__ == "__main__":
    main()

