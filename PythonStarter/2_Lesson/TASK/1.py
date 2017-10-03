a =float(input("side a = "))
b =float(input("side b = "))
c =float(input("side c = "))

def triagle_areas(a, b, c):
  p =(a+b+c)/2
  S =(p*(p-a)*(p-b)*(p-c))**0.5
  return S

if a + b > c and a + c > b and b + c > a :
    S = triagle_areas(a, b, c)
    print(S)
else:
 print("Error")  


