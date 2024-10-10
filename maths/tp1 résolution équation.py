import math

a = 3
b = -6
c = -2

delta = b**2 - 4*a*c

if delta < 0:
    print("pas de solution réelle")
elif delta == 0 :
    x0 = -b / (2*a)
    print(f"unique solution : x0={x0:.2f}")
else : 
    x1 = (-b - math.sqrt(a) / (2 * a))
    x2 = (-b + math.sqrt(a) / (2 * a))
    print(f"deux solution distinctes : x1={x1:.2f} et x2={x2:.2f}")