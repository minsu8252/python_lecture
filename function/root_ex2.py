a=float(input("A입력: "))
b=float(input("B입력: "))
c=float(input("C입력: "))
# (a*x^2)+(b*x)+c
# r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
# r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
# print(r1, r2)
def print_root_ex(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print(r1, r2)
print_root_ex(1,2,-8)