def root_ex(a, b, c):
    r_1 = (-b + (b**2 -4 * a * c)**(1/2)) / (2 * a)
    r_2 = (-b - (b**2 -4 * a * c)**(1/2)) / (2 * a)
    print('해는',r_1,'또는',r_2)
    return r_1, r_2

root_ex(2, -1, -6)