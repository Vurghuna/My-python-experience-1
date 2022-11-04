import requests
import json
import pprint
import random
import html
from string import ascii_uppercase
answer_number = 0

url = "https://opentdb.com/api.php?amount=3"
endGame= ""

while endGame !="quit":
      r = requests.get(url)
      if (r.status_code !=200):
            endGame = input ("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game.")
      else:
            answer_number = 0
            data = json.loads(r.text)
            question = data['results'][0]['question']
            answers = data['results'][0]['incorrect_answers']
            correct_answer = data['results'][0]['correct_answer']
            answers.append(correct_answer)
            random.shuffle(answers)
            answer_number = 0
            print(html.unescape(question) + "\n")

            for answer in answers:
                  print(ascii_uppercase[answer_number] + " - " + html.unescape(answer))
                  answer_number +=1

            user_answer = input("\nType the option of the correct answer: ")
            user_answer = answers[(user_answer)-1]

            if user_answer == correct_answer :
                  print("\nCongratulations! You answered correctly! The correct answer was : " + html.unescape(correct_answer))
            else:
                  print("Sorry, " + html.unescape(user_answer) + " is incorrect. The correct answer is: " + html.unescape(correct_answer))
