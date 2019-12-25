import csv
def area():
    with open('resources/length.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}
        u1,sq,u2,sq2 = input("Enter the conversion to be done : ").split()
        in2 = float(input("Enter the numeric value : "))
        u1 = u1.lower()
        u2 = u2.lower()
        try:
            if u1=='m':
                in1 = u1 + " to " + u2 
                cf =float(mydict[in1])
                print(in2*(cf**2), u2," sq")
            elif u2 == 'm':
                in1 = "m to " + u1
                cf = float(mydict[in1])
                print(in2*((1/cf)**2),u2," sq")
            else:
                in1 = "m to " + u1
                cf1 = float(mydict[in1])
                tv = in2*((1/cf1)**2)
                in3 = "m to " + u2
                cf2 = float(mydict[in3])
                print(tv*(cf2**2),u2," sq")
        except:
            print("Conversion not possible")
