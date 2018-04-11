message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

def reverse_words(msg):
    size = len(msg)
    space = [size]

    for i in range(size-1, -1, -1):
            # print(i, msg[i])
        if msg[i] == ' ' or i == 0:
            space.append(i)

    for j in range(len(space)-1):
        sub_word = msg[space[j+1]:space[j]]
        for k in sub_word:
            print(k, end='')

reverse_words(message)

# Prints: 'steal pound cake'
