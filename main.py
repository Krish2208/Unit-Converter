from files import length,area,time,hel,speed,volume,mass
ty = input("Enter the type of conversion : ")
print("\nFirst input the current unit then the unnit iin which it is to be converted.\nfor eg- m km for converting m to km and then numeric value in next input.\n")
if ty.lower()=="length":
    length.length()
elif ty.lower()=="time":
    time.time()
elif ty.lower()=="area":
    area.area()
elif ty.lower() in ["speed","velocity"]:
    speed.speed()
elif ty.lower()=="energy":
    energy.energy()
elif ty.lower()=="volume":
    volume.volume()
    area.area()
elif ty.lower() in ["mass","weight"]:
    mass.mass()    
elif ty.lower()=="help" :
    hel.hel()
else:
    print("type help for knowing how this works")
    print("Type of conversion-length,time,area,speed,energy,volume,mass")
