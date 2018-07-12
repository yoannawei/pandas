# this program randomly displays one of Jay's random thoughts

import random

jays_thoughts = ["I wish I was a tuba",
                 "Do penguins like spaghetti?"
                 "Yoanna is confusing"
                 "I love bread",
                 "VenueBook forever",
                 "I love VenueBook more than i love yoanna",
                 "yes wei",
                 "do sushi dream of electric fish?"
                 ]

def prompt_until(prompt, retry):
    if retry is True:
        display_prompt("yes")
    else:
        retry(False)


def isTrue(answer):
    if str(answer).isnumeric:
        print(answer, "is not a valid input")
        return False
    else:
        return True

def display_prompt(answer):
    if isTrue():
        print("would you like to hear one more of Jay's random thoughts?\n")
    else:
        retry(isTrue(answer))

def retry(isTrue):
    if isTrue is False:
        print("invalid input, please try again")
        return False
    else:
        return True

if __name__ == '__main__':
    user_answer = input("would you like to hear one of Jay's random thoughts?\n")
    prompt_until("", retry(isTrue(user_answer)))