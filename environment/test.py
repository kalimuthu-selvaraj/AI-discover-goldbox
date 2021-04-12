locations = {(x, y): (100 * (x + 1) + 0 * x, (100 * (y + 1) + 0 * y))
             for y in range(10) for x in range(10)}

print(locations[(0, 1)])
