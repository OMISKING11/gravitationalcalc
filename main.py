print("This is a program which will help you find the value of gravitational force")
print("Made by Om Kumar")
print("Which value you want to find out?\n"
      " 1.force\n"
      " 2.distance")
G = 6.673 * 10 ** -11
ask = int(input("Which one: "))
if ask == 1:
  m1 = float(input("Enter the value of mass of the first object: "))
  m1exp = int(input("Enter the exponent on mass of the first object: "))
  m2 = float(input("Enter the value of mass of the second object: "))
  m2exp = int(input("Enter the exponent on mass of the second object: "))
  r = float(input("Enter the value of distance between the two objects: "))
  rexp = int(input("Enter the exponent on distance between the two objects: "))
  gravforce()

elif ask == 2:
  m1 = float(input("Enter the value of mass of the first object: "))
  m1exp = int(input("Enter the exponent on mass of the first object: "))
  m2 = float(input("Enter the value of mass of the second object: "))
  m2exp = int(input("Enter the exponent on mass of the second object: "))
  f = float(input("Enter the value of force between the two objects: "))
  fexp = int(input("Enter the exponent on force between the two objects: "))
  gravdistance()
def gravforce():
  F = G * m1 * 10**m1exp * m2 * 10**m2exp / (r * 10**rexp)**2
  print("The value of gravitational force is", F)

def gravdistance():
  R = G * m1 * 10**m1exp * m2 * 10**m2exp / f * 10**fexp
  print("The value of distance is", R)
