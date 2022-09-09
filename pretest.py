def midpoint(x,x1,y,y1):
  xm =(x+x1)/2
  ym =(y+y1)/2
  return xm,ym

list = []
#------------------
num = int(input("Give me a number"))
if num%3 == 0:
    print("boogers")
else:
    print("squirrels")
#------------------
for i in range(10,31,5):
    print(i,end = ' ')
print()
#------------------
x = int(input("Give me a x value"))
x1 = int(input("Give me a x1 value"))
y = int(input("Give me a y value"))
y1 = int(input("Give me a y1 value"))
print(midpoint(x,x1,y,y1))
#------------------
for j in range(5):
    list.append(input("give me 5 of your friends names "))
list.sort()
for k in range(5):
    if list[k] == "Mo":
        print("Nerd Alert")
    else:
        print("Cool Kids only")
