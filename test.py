row = [1]
for i in range(8):
    print(" " * (7 - i), *row, sep=" ")
    row = [1] + [x + y for x, y in zip(row[:-1], row[1:])] + [1]
