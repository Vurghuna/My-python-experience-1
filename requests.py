import requests
import json
import pprint

url = "https://opentdb.com/api.php?amount=1"
endgame=""

while endgame !="quit":
      r = requests.get(url)
      if (r.status_code !=200):
            endgame=input("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game'")
      else:
            data = json.loads(r.text)
            pprint.pprint(data)
            input("Press enter to get a new question")
