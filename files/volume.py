import csv
def volume():
    with open('resources/volume.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}
        u1,u2 = input("Enter the conversion to be done : ").split()
        in2 = float(input("Enter the numeric value : "))
        u1 = u1.lower()
        u2 = u2.lower()
        try:
            if u1=='cubicm':
                in1 = u1 + " to " + u2 
                cf =float(mydict[in1])
                print(in2*cf, u2)
            elif u2 == 'cubicm':
                in1 = "cubicm to " + u1
                cf = float(mydict[in1])
                print(in2*(1/cf), u2)
            else:
                in1 = "cubicm to " + u1
                cf1 = float(mydict[in1])
                tv = in2*(1/cf1)
                in3 = "cubicm to " + u2
                cf2 = float(mydict[in3])
                print(tv*cf2, u2)
        except:
            print("Conversion not Possible")
