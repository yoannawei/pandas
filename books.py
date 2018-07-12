import functools

order_number = [34587, 98762, 77226, 88112]
book_title_author = ['Learning Python, Mark Lutz', 'Programming Python, Mark Lutz',
              'Head First Python, Paul Barry', 'Einführung in Python3, Bernd Klein']
quantity = [4,5,3,3]
price = [40.95, 56.80, 32.95, 24.99]

price_adjustment = list(map(lambda x, y : x * y + 10 if x * y < 100 else x * y, quantity, price))
print(order_number, price_adjustment)

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80],
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),
                          map(lambda x: (x[0],x[2] * x[3]), orders)))

print(invoice_totals)

def get_tuple(list1, list2):
    my_list = []
    for i in range(len(list1)):
        my_list.append((list1[i], list2[i]))
    return my_list


print(get_tuple(order_number, price_adjustment))
