# this is a recursive function
# that generates all permutations of an input string
# it returns them as a set

def shuffle(word):

    # base case
    if len(word) == 1:
        return set([word])

    # split last character off the word
    first = word[:-1]
    last = word[-1]

    # recursively call the shuffle function
    perms_first = shuffle(first)

    # insert the last character into every
    # possible position of the remaining word
    perms = set()

    for perm_first in perms_first:
        for j in range(len(first)+1):
            perm = perm_first[:j] + last + perm_first[j:]
            perms.add(perm)

    return perms

if __name__ == '__main__':
    print(shuffle("blah"))
