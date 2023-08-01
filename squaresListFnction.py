def squares(n):
    squares = []
    for i in range(n):
        i*=i
        squares.append(i)
    return squares

print(squares(11))