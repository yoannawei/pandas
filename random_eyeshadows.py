import random

# this program picks a random assortment of makeup to wear

eyeshadows = ['blonde', 'bathwater', 'skimp', 'steady', 'punk',
              'baby', 'anaheim', 'stark', 'zone', 'serious',
              'pop', 'harajuku', 'danger', '1987', 'blackout',
              'kinky', 'freestyle', 'mushroom', 'backdoor', 'blackout',
              'barlust', 'rockstar', 'evidence', 'loaded', 'asphalt',
              'revolt', 'gonzo', 'slowburn', 'savage', 'fringe',
              'chaos', 'jilted', 'urban', 'freak', 'thrash',
              'smog', 'mildew', 'oil slick', 'last call', 'chopper',
              'maui wowie', 'shattered', 'polyester bride', 'grifter',
              'sin', 'filament', 'whirling', 'era', 'woodwinked',
              'unwind', 'lady fingers', 'twelve chimes', 'showstopper',
              'beyond gorgeous', 'brulee', 'sugar', 'spoiled brat browbone',
              'spoiled brat crease', 'spoiled brat eyelid', 'kitten', 'buck',
              'coastal scent blush', 'coastal scent bronzer']

eyeliners = ['perversion', 'superfine', 'prestige black', 'prestige blue',
             'rimmel brown', 'stay all day']

blushes = ['wisteria', 'songbird', 'snapdragon', 'paaarty', 'naked flushed',
           'luminoso', 'be my highlight', 'twinkle pink', 'organsm']

bronzers = ['chocolate solei', 'naked flushed']

highlighters = ['kitten', 'naked flushed', 'be my highlight', 'blonde', 'bathwater']

lipsticks = ['in the nude', 'satin mauve', 'fab fushsia',
             'firebird', '714', 'rocksteady',
             'london', 'birthday suit', 'seduction', 'rikugien',
             'patina', 'mauve outta here', 'backtalk', 'belle',
             'quince', 'beetroot', 'cruella', 'kate moss 107', 'vixen',
             'super strawberry', 'adjust your tiara', 'anarchy', 'electric pink',
             'ingenue', 'pink frosting', 'toast of new york']

def random_pick(collection, num):
    return random.sample(collection, num)

def print_choice(choice):
    for i in choice:
        print(i)

if __name__ == '__main__':
    # generate a random combination of eyeshadows
    num_eyeshadow = int(input("how many eyeshadows are you using? "))
    print("eyeshadows: ")
    print_choice(random_pick(eyeshadows, num_eyeshadow))

    # randomly picks a bronzer, a blush and a highlighter
    print("bronzer:")
    print_choice(random_pick(bronzers, 1))
    print("blush:")
    print_choice(random_pick(blushes, 1))
    print("highlighter:")
    print_choice(random_pick(highlighters, 1))

    # randomly picks a combination of lipsticks
    num_lipstick = int(input("How many lipsticks are you using? "))
    print("lipsticks:")
    print_choice(random_pick(lipsticks, num_lipstick))


