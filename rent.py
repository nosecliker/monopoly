base=int(input("base number"))
house =int(input("house number"))

def rentc(base, house):
    if house == 1:
        rent= base *2
    elif house==2:
        rent=base*5
    elif house == 3:
        rent = base * 15
    elif house ==4:
        rent = base * 45
    elif house == 5:
        rent = base *80
    else:
        rent = base
    return rent
print (rentc(base,house))


