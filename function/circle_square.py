r = float(input("반지름 입력 : "))

def circle_square(r):
    x = r**2 * 3.14
    print('원의 면적은 {}이다.'.format(x))
    return r

circle_square(r)