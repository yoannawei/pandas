# this program displays the reasons that I love you
import random

reasons = ["You call me a cat. I am a cat. You get me.",
           "You get me flowers.",
           "You bring me chips when I am sick.",
           "You snuggle me often."]

def add_reason(string):
    reasons.append(string)
    return reasons

def random_reason():
    return random.choice(reasons)

def cont():
    answer = input("wanna hear more?")
    if(answer == 'y'):
        print(random_reason())
    else:
        print("ok, fine, bye")

if __name__ == '__main__':
    answer = input("press any key to hear a reason that I love you")
    print(random_reason())
    cont()

