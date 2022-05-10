def add (x,y):
    mask = 0xffffffff
    while (y & mask) != 0:
        carry = x & y
        x = x ^ y 
        y = carry << 1
    print(y)
    return (x & mask) if y > 0 else x

c = add(-100,88)
print(c)