import math

x=int(input("Enter the size:"))
center_x=math.ceil(x/2)
width_l=center_x
width_h=center_x
for length in range(1,x+1):
    for width in range(1,x+1):
        if(width>=width_l and width<=width_h):
            print("*",end='')
        else:
            print(" ",end='')
    print("")
    if(length<center_x):
        width_l-=1
        width_h+=1
    else:
        width_l+=1
        width_h-=1
