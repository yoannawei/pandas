import pandas as pd

data = {'item': ['cake', 'pie', 'cupcake', 'croissant', 'shortbread cookie'],
        'flavor': ['chocolate', 'crack', 'brooklyn blackout', 'pistachio', 'mint chocolate chip'],
        'price': [5, 5, 4, 4, 2]
        }

bakery = pd.DataFrame(data)
print(bakery)