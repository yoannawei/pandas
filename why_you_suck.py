import re

num_reasons = 9

def get_name():
    print('What\'s your name?')
    name = input()
    return name

def if_jay(name):
    searchName = re.search(r'jay', name, re.I)
    if searchName != None:
        return True
    else:
        return False

def main():
    name = get_name()
    if if_jay(name) == True:
        print('You suck\nWanna know why?\nY/N')
        answer = input()
        print_reason(answer)
    else:
        print('You\'re alright')

def reason(picker):
    reasons = {1: 'You don\'t text me often enough',
               2: 'You don\'t call me often enough',
               3: 'You only want to hang out on the weekend',
               4: 'You only brought me flowers once even though you know I love flowers',
               5: 'You never seem to remember when exactly we first met',
               6: 'You don\'t clean your apartment even though I come over so often ',
               7: 'You are not interested in subjects other than programming',
               8: 'You tell your best friend too much about me',
               9: 'You are not talkative at all in restaurants.'
               }
    return print(reasons[picker])


def invalid():
    print('That\'s an invalid input.')

def check_range(picker):
    if picker > num_reasons:
        return False
    else:
        return True


def repeat():
    print('Continue? (Y/N)')
    answer = input()
    if answer.upper() == 'N':
        goodbye()
    elif answer.upper() == 'Y':
        print_reason(answer)
    else:
        invalid()

def print_reason(answer):
    if answer.upper() == 'Y':
        print('Input a number between 1 and', num_reasons)

        picker = input()
        if picker.isnumeric():
            index = int(picker)
            if check_range((index)):
                reason(index)
                repeat()
            else:
                invalid()
                goodbye()
        else:
            invalid()
            goodbye()
    elif answer.upper() == 'N':
        goodbye()
    else:
        invalid()


def goodbye():
    print('Hasta la vista baby')

main()

