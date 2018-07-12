data = [(2,3), (3,4), (4,5)]
m = 0
b = 0

def gradientDescent(data, m, b):
  learning_rate = 0.05
  for data_point in data:
    x = data_point[0]
    y = data_point[1]

    guess = m * x + b
    error = y - guess

    # iterate on values of slope and intercept
    m = m + error * x * learning_rate
    b = b + error * learning_rate

    print(m, b, y, error)

gradientDescent(data, m, b)
