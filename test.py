a=int(input("Enter number of sides: "))
if a==3:
    print("Triangle")
elif a==4:
    print("Square")
elif a==5:
    print("Pentagon")
elif a==6:
    print("Hexagon")
elif a==7:
    print("Heptagon")
elif a==8:
    print("Octagon")
elif a==9:
    print("Nonagon")
elif a==10:
    print("Decagon")
elif a>10:
    print("You are out of range(range=3-10)")
else:
    print("It cannot be")
