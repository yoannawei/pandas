# given a string of characters embedded with matching parentheses
# this program returns the position of the closing parenthesis

# initialize
word = "do(nut(yoanna)prin)cess"
word_stack = []
par_stack = []

# position of the opening parenthesis (not needed)
# openPos = 2

def make_word_stack(word):
    # same as:
    # for i in word:
        # word_stack.append(i)
    return list(map(lambda x: word_stack.append(x), word))

def closingPos(word_stack):
    # print the position of the closing parenthesis
    for j in range(len(word_stack)):
        if word_stack[j] == '(':
            par_stack.append(j)
        elif word_stack[j] == ')':
            par_stack.pop()
            if len(par_stack) == 0:
                return j

make_word_stack(word)
print(closingPos(word_stack))



